from libs.sdks.onedrive.connector import onedrive_connector
from libs.sdks.onedrive.explorer import onedrive_list_files
from const import ONEDRIVE_CLIENT_ID, ONEDRIVE_SECRET, ONEDRIVE_SCOPES, ONDRIVE_REDIRECT_URL

def run():
    print('Running...')
    conn = onedrive_connector(ONEDRIVE_CLIENT_ID, ONEDRIVE_SECRET, ONEDRIVE_SCOPES, ONDRIVE_REDIRECT_URL)
    onedrive_list_files(conn)

if __name__ == '__main__':
    run()
