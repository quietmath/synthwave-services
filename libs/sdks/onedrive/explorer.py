def onedrive_list_files(conn):
    item_id = 'root'
    items = navigate(conn, item_id)
    count = 0
    for count, item in enumerate(items):
        print("{} {}".format(count + 1, item.name if item.folder is None else "/" + item.name))

def navigate(conn, item_id):
    items = conn.item(id = item_id).children.get()
    return items
