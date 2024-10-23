# -*- coding: utf-8 -*-
"""Utility functions and classes."""
from collections import defaultdict
from typing import DefaultDict, Dict, Optional, Union

import requests as req

# Local imports
from . import exceptions as E

BASE_URL = "https://api.24sea.eu/routes/v1/"


def handle_request(
    url: str,
    params: Dict,
    auth: Optional[req.auth.HTTPBasicAuth],
    headers: Dict,
) -> req.models.Response:
    """Handle the request to the 24SEA API and manage errors.

    Parameters
    ----------
    url : str
        The URL to which to send the request.
    params : dict
        The parameters to send with the request.
    auth : requests.auth.HTTPBasicAuth
        The authentication object.
    headers : dict
        The headers to send with the request.

    Returns
    -------
    requests.models.Response
        The response object if the request was successful, otherwise error.
    """
    if auth is None:
        auth = req.auth.HTTPBasicAuth("", "")
    try:
        r_ = req.get(url, params=params, auth=auth, headers=headers)

        if r_.status_code in [400, 401, 403, 404, 502, 503, 504]:
            print(f"Request failed because: \033[31;1m{r_.text}\033[0m")
            r_.raise_for_status()
        # this will handle all other errors
        elif r_.status_code == 500:
            # fmt: off
            print("\033[31;1mInternal server error. You will need to contact "
                  "support at \033[32;1;4msupport.api@24sea.eu\033[0m")
            # fmt: on
            r_.raise_for_status()
        elif r_.status_code > 400:
            # fmt: off
            print("Request failed with status code: "
                  f"\033[31;1m{r_.status_code}\033[0m")
            # fmt: on
            r_.raise_for_status()
    except (req.exceptions.ConnectionError, req.exceptions.Timeout) as exc:
        print(f" Request failed because: \033[31;1m{exc}\033[0m")
        raise exc
    return r_


def default_to_regular_dict(d_: Union[DefaultDict, Dict]) -> Dict:
    """Convert a defaultdict to a regular dictionary."""
    if isinstance(d_, defaultdict):
        d_ = {k_: default_to_regular_dict(v_) for k_, v_ in d_.items()}
    return dict(d_)


def check_authentication(func):
    """Check authentication before making the request to the 24SEA API."""

    def wrapper(self, *args, **kwargs):
        """Wrapper function to check authentication."""
        # fmt: off
        if not isinstance(self.auth, req.auth.HTTPBasicAuth) or not self.authenticated:
            raise E.AuthenticationError(
                "\033[31;1mAuthentication needed before querying the metrics.\n"
                "\033[0mUse the \033[34;1mdatasignals.\033[0mauthenticate("
                "\033[32;1m<username>\033[0m, \033[32;1m<password>\033[0m) "
                "method."
            )
        return func(self, *args, **kwargs)
        # fmt: on

    return wrapper
