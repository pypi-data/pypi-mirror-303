import json
import sys
import logging

from src.wavin_sentio_proxy.wavin_sentio_proxy import LoginData, WavinSentioProxy
from credentials import Credentials

logging.basicConfig( stream=sys.stderr )
_LOGGER = logging.getLogger( "test_login" )
_LOGGER.setLevel( logging.DEBUG )

def test_login():
    credentials = Credentials()
    
    proxy = WavinSentioProxy(credentials.username, credentials.password)
    proxy.login()
    assert proxy.logindata is not None
    
    strlogindata = json.dumps(proxy.logindata.todict(), default=str)
    _LOGGER.debug(f"Login success: {strlogindata}")

def test_login_refresh():
    credentials = Credentials()
    
    assert credentials.access_token is not None
    assert credentials.refresh_token is not None
    assert credentials.token_type is not None
    
    proxy = WavinSentioProxy(credentials.username, credentials.password)
    proxy.logindata = LoginData({
        "access_token": credentials.access_token,
        "refresh_token": credentials.refresh_token,
        "token_type": credentials.token_type,
        "expires_in": 0,
    })
    proxy.refresh_login()
    
    assert proxy.logindata is not None
    assert proxy.logindata.expires_in != 0
    
    strlogindata = json.dumps(proxy.logindata.todict(), default=str)
    _LOGGER.debug(f"Login success: {strlogindata}")
