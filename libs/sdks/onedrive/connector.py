import onedrivesdk_fork
from onedrivesdk_fork.helpers import GetAuthCodeServer

def onedrive_connector(client_id, client_secret, scopes, redirect_url):
    conn = onedrivesdk_fork.get_default_client(client_id = client_id, scopes = scopes)
    auth_url = conn.auth_provider.get_auth_url(redirect_url)
    auth_code = GetAuthCodeServer.get_auth_code(auth_url, redirect_url)
    conn.auth_provider.authenticate(auth_code, redirect_url, client_secret)
    return conn
