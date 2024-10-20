from datetime import datetime, timedelta
from http import HTTPStatus
import requests
from enum import Enum
from typing import Any, Dict
import logging


from .const import ( API, API_VERSION)

_LOGGER = logging.getLogger(__name__)

class NilanProxyConnectionErrorType(Enum):
    TIMEOUT = "timeout"
    AUTHENTICATION_ERROR = "authentication_error"
    UNSUPPORTED_MODEL = "unsupported_model"

class LoginData:
    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int
    # scope: str
    token_expires_datetime: datetime
    
    def __init__(self, data: Dict[str, Any]):
        self.access_token = str(data["access_token"])
        self.refresh_token = str(data["refresh_token"])
        self.token_type = str(data["token_type"])
        self.expires_in = int(data["expires_in"])
        # self.scope = str(data["scope"])
        self.token_expires_datetime = datetime.now() + timedelta(seconds=self.expires_in)
        
    def todict(self) -> Dict[str, str|int|datetime]:
        return {
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
            "token_type": self.token_type,
            "expires_in": self.expires_in,
            # "scope": self.scope,
            "token_expires_datetime": self.token_expires_datetime,
        }

class WavinSentioProxy():
    
    username: str
    password: str
    logindata: LoginData|None = None
    
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        
    def login(self) -> LoginData:
        headers: Dict[str, str] = {
            "Authorization": 'Basic YXBwOnNlY3JldA==',
            "Content-Type": "application/x-www-form-urlencoded",
        }
        post_data: Dict[str, str] = {
            "username": self.username,
            "password": self.password,
            "grant_type": "password",
        }
        requesturl = f"{API}{API_VERSION}/oauth/token"
        response = requests.post(requesturl, data=post_data, headers=headers)
        
        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise UnauthorizedError("Invalid username or password")
        if response.status_code != HTTPStatus.OK:
            try:
                response.raise_for_status()
            except Exception as err:
                raise ConnectionError("Login failed") from err
            raise ConnectionError("Login failed: " + str(response.text))
        
        responsedata = response.json()
        self.logindata = LoginData(responsedata)
        _LOGGER.debug("Login success")
        return self.logindata
    
    def refresh_login(self) -> LoginData:
        if self.logindata is None:
            return self.login()
        
        headers: Dict[str, str] = {
            "Authorization": 'Basic YXBwOnNlY3JldA==',
            "Content-Type": "application/x-www-form-urlencoded",
        }
        post_data: Dict[str, str] = {
            "refresh_token": self.logindata.refresh_token,
            "grant_type": "refresh_token",
        }
        requesturl = f"{API}{API_VERSION}/oauth/token"
        response = requests.post(requesturl, data=post_data, headers=headers)
        if response.status_code != HTTPStatus.OK:
            return self.login()
        
        responsedata = response.json()
        self.logindata = LoginData(responsedata)
        _LOGGER.debug("Login refresh success")
        return self.logindata
    
    def get_location(self, locationid: str):
        return self._request("locations", locationid)
    
    def get_locations(self):           
        return self._request("locations")

    def set_profile(self, locationid:str, profile:str):
        payload: Any = {
            "returnField": ["code"], 
            "room": {"profile": profile}
        }
        return self._patch("rooms", locationid, payload)

    def get_rooms(self, locationid: str):
        params = { 'location': locationid }
        return self._request("rooms", params=params)

    def set_temperature(self, locationid:str, temperature: int):
        payload: Any = {
            "returnField": ["code"],
            "room": {
                "profile": "manual", 
                "tempManual": temperature}
        }
        return self._patch("rooms", locationid, payload)
    
    def _request(self, method:str, id:str|None = None, params: Dict[str, Any]|None = None) -> requests.Response:
        headers: Dict[str,str] = {
            "Authorization": self._get_authorization_token(),
        }
        url = self._build_method_url(method, id)
        return requests.get(url, params, headers=headers)
    
    def _patch(self, method:str, id:str|None = None, payload: Any|None = None) -> requests.Response:
        headers: Dict[str,str] = {
            "Authorization": self._get_authorization_token(),
            "Content-Type": "application/json",
        }
        url = self._build_method_url(method, id)
        return requests.patch(url, json=payload, headers=headers)
        
    def _build_method_url(self, method:str, locationid:str|None) -> str:
        method = method.strip('/ ')
        locationid = locationid.strip('/ ') if locationid is not None else ''
        return f"{API}{API_VERSION}/{method}/{locationid}"
        
    def _get_authorization_token(self):
        logindata = self.logindata
        if logindata is None or datetime.now() >= logindata.token_expires_datetime:
            logindata = self.refresh_login()
        return f"{logindata.token_type} {logindata.access_token}"
    

class UnauthorizedError(Exception):
    pass
