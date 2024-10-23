# -*- coding: utf-8 -*-
"""The module for the DataSignals pandas accessor containing the main class
and the methods to authenticate, get metrics, and get data from the 24SEA API.
"""
import datetime
import logging
from typing import Dict, List, Optional, Union
from warnings import simplefilter

import pandas as pd
import requests as req
from pydantic import validate_call

# Local imports
from .. import core as C
from .. import exceptions as E
from .. import utils as U

try:
    # delete the accessor to avoid warning
    del pd.DataFrame.datasignals
except AttributeError:
    pass

# This filter is used to ignore the PerformanceWarning that is raised when
# the DataFrame is modified in place. This is the case when we add columns
# to the DataFrame in the get_data method.
# This is the only way to update the DataFrame in place when using accessors
# and performance is not an issue in this case.
# See https://stackoverflow.com/a/76306267/7169710 for reference.
simplefilter(action="ignore", category=pd.errors.PerformanceWarning)


logging.basicConfig(format="%(message)s", level=logging.INFO)


@pd.api.extensions.register_dataframe_accessor("datasignals")
class DataSignals:
    """Accessor for working with data signals coming from the 24SEA API."""

    def __init__(self, pandasdata: pd.DataFrame):
        self._obj = pandasdata
        self.base_url: str = f"{U.BASE_URL}datasignals/"
        self.username: Optional[str] = None
        self.password: Optional[str] = None
        self.auth: Optional[req.auth.HTTPBasicAuth] = None
        self.authenticated: bool = False
        self._selected_metrics: Optional[pd.DataFrame] = None
        self.__api = C.API()

    @validate_call
    def authenticate(self, username: str, password: str) -> None:
        """Authenticate the user with the 24SEA API. Additionally, define
        the ``metrics_overview`` dataframe as __api.metrics_overview.

        Parameters
        ----------
        username : str
            The username to authenticate.
        password : str
            The password to authenticate.
        """
        self.username = username
        self.password = password
        self.auth = req.auth.HTTPBasicAuth(username, password)
        self.authenticated = self.__api.authenticate(username, password)

    @property
    @U.check_authentication
    def selected_metrics(self) -> pd.DataFrame:
        """Return the selected metrics for the query."""
        # Get the selected metrics as the self._obj columns that are available
        # in the metrics_overview DataFrame
        if self._selected_metrics is not None:
            # Check that the index is set to the metric column
            if "metric" not in self._selected_metrics.index:
                if "metric" not in self._selected_metrics.columns:
                    raise E.DataSignalsError(
                        "\033[31mThe \033[1mselected_metrics\033[22m DataFrame "
                        "must have the \033[1mmetric\033[22m column as the index."
                    )
                self._selected_metrics.set_index("metric", inplace=True)
            return self._selected_metrics
        return self.__api.selected_metrics(self._obj)

    @selected_metrics.setter
    @U.check_authentication
    def selected_metrics(self, value: pd.DataFrame) -> None:
        """Set the selected metrics for the query."""
        self._selected_metrics = value

    @U.check_authentication
    @validate_call
    def __get_data(
        self,
        sites: Optional[Union[List, str]],
        locations: Optional[Union[List, str]],
        metrics: Union[List, str],
        start_timestamp: Union[str, datetime.datetime],
        end_timestamp: Union[str, datetime.datetime],
        outer_join_on_timestamp: bool = False,
        headers: Optional[Union[Dict[str, str]]] = None,
    ):
        """Get the data signals from the 24SEA API.

        Parameters
        ----------
        sites : Optional[Union[List, str]]
            The site name or List of site names. If None, the site will be
            inferred from the metrics.
        locations : Optional[Union[List, str]]
            The location name or List of location names. If None, the location
            will be inferred from the metrics.
        metrics : Union[List, str]
            The metric name or List of metric names. It must be provided.
            They do not have to be the entire metric name, but can be a part
            of it. For example, if the metric name is
            ``"mean_WF_A01_windspeed"``, the user can equivalently provide
            ``sites="wf"``, ``locations="a01"``, ``metric="mean windspeed"``.
        start_timestamp : Union[str, datetime.datetime]
            The start timestamp for the query. It must be in ISO 8601 format,
            e.g., ``"2021-01-01T00:00:00Z"`` or a datetime object.
        end_timestamp : Union[str, datetime.datetime]
            The end timestamp for the query. It must be in ISO 8601 format,
            e.g., ``"2021-01-01T00:00:00Z"`` or a datetime object.
        outer_join_on_timestamp : bool, optional
            If True, the data will be joined on the timestamp which will be the
            index of the DataFrame. If False, the data will be concatenated
            without any join. Default is False.
        headers : Optional[Union[Dict[str, str]]], optional
            The headers to pass to the request. If None, the default headers
            will be used as ``{"accept": "application/json"}``. Default is None.

        Returns
        -------
        pd.DataFrame
            The DataFrame containing the data signals.
        """
        return self.__api.get_data(
            sites=sites,
            locations=locations,
            metrics=metrics,
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            outer_join_on_timestamp=outer_join_on_timestamp,
            headers=headers,
            data=self._obj,
            as_dict=False,
        )

    @U.check_authentication
    def as_dict(self) -> Dict[str, Dict[str, pd.DataFrame]]:
        """Return the DataFrames as a dictionary where the keys are the sites
        and the values are a dictionary where the keys are locations and the
        values are dataframes for each location.

        This operation is only possible when get_data has been called with the
        outer_join_on_timestamp parameter set to False.

        To identify this, the following conditions must be met in self._obj:
        * The index must be the default RangeIndex,
        * The site, location, and timestamp columns must be available.

        Returns
        -------
        Dict[str, Dict[str, pd.DataFrame]]
            The dictionary containing the dataframes for each site.
        """

        if self._obj.empty:
            raise E.DataSignalsError(
                "\033[31mThe \033[1mas_dict \033[22mmethod can only be called "
                "when the DataFrame is not empty."
            )
        if not isinstance(self._obj.index, pd.RangeIndex):
            raise E.DataSignalsError(
                "\033[31mThe \033[1mas_dict \033[22mmethod can only be called "
                "when the index is a \033[1mRangeIndex.\033[0m"
            )
        if not all(
            c_ in self._obj.columns for c_ in ["site", "location", "timestamp"]
        ):
            raise E.DataSignalsError(
                "\033[31mThe \033[1mas_dict \033[22mmethod can only be called "
                "when the site, location, and timestamp columns are available."
            )
        groups = self._obj.groupby(["site", "location"])
        __dict: Dict[str, Dict[str, pd.DataFrame]] = {}
        for (s_, l_), group in groups:
            if s_ not in __dict:
                __dict[s_] = {}
            # Manipulate the group to remove columns with all NaN values
            # and set the index to the timestamp column.
            # This operation cannot be done safely in api-24sea.
            __df: pd.DataFrame = group.dropna(axis=1, how="all")
            __df.set_index("timestamp", inplace=True)
            __df.index = pd.to_datetime(__df.index)
            if l_ not in __dict[s_]:
                __dict[s_][l_] = __df
                # Pass also the authentication, and __api to the DataFrame
                __dict[s_][l_].datasignals.base_url = self.base_url
                __dict[s_][l_].datasignals.username = self.username
                __dict[s_][l_].datasignals.password = self.password
                __dict[s_][l_].datasignals.auth = self.auth
                __dict[s_][l_].datasignals.authenticated = self.authenticated
                __dict[s_][l_].datasignals.__api = self.__api
        return __dict

    @U.check_authentication
    def get_data(
        self,
        sites: Optional[Union[List, str]],
        locations: Optional[Union[List, str]],
        metrics: Union[List, str],
        start_timestamp: Union[str, datetime.datetime],
        end_timestamp: Union[str, datetime.datetime],
        as_dict: bool = True,
    ) -> Union[pd.DataFrame, Dict[str, Dict[str, pd.DataFrame]]]:
        """Get the data signals from the 24SEA API.

        Parameters
        ----------
        sites : Optional[Union[List, str]]
            The site name or List of site names. If None, the site will be
            inferred from the metrics.
        locations : Optional[Union[List, str]]
            The location name or List of location names. If None, the location
            will be inferred from the metrics.
        metrics : Union[List, str]
            The metric name or List of metric names. It must be provided.
            They do not have to be the entire metric name, but can be a part
            of it. For example, if the metric name is
            ``"mean_WF_A01_windspeed"``, the user can equivalently provide
            ``sites="wf"``, ``locations="a01"``, ``metric="mean windspeed"``.
        start_timestamp : Union[str, datetime.datetime]
            The start timestamp for the query. It must be in ISO 8601 format,
            e.g., ``"2021-01-01T00:00:00Z"`` or a datetime object.
        end_timestamp : Union[str, datetime.datetime]
            The end timestamp for the query. It must be in ISO 8601 format,
            e.g., ``"2021-01-01T00:00:00Z"`` or a datetime object.
        outer_join_on_timestamp : bool, optional
            If True, the data will be joined on the timestamp which will be the
            index of the DataFrame. If False, the data will be concatenated
            without any join. Default is False.
        headers : Optional[Union[Dict[str, str]]], optional
            The headers to pass to the request. If None, the default headers
            will be used as ``{"accept": "application/json"}``. Default is None.

        Returns
        -------
        pd.DataFrame | Dict[str, Dict[str, pd.DataFrame]]
            The DataFrame containing the data signals, or the dictionary
            containing the dataframes for each site.
        """
        if as_dict:
            self.__get_data(
                sites=sites,
                locations=locations,
                metrics=metrics,
                start_timestamp=start_timestamp,
                end_timestamp=end_timestamp,
                outer_join_on_timestamp=not as_dict,
            )
            return self.as_dict()
        return self.__get_data(
            sites=sites,
            locations=locations,
            metrics=metrics,
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            outer_join_on_timestamp=not as_dict,
        )
