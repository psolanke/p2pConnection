import shelve

STORAGE_FILE = 'store.txt'

class StorageManager(object):
    @staticmethod
    def open_db():
        return shelve.open(STORAGE_FILE)

    @staticmethod
    def close_db(db):
        db.close()

    @staticmethod
    def update_registry(public_ip, port_num, device_id):
        db = StorageManager.open_db()
        db[device_id] = {'public_ip': public_ip , 'port_num': port_num}
        StorageManager.close_db(db)

    @staticmethod
    def get_device(device_id):
        db = StorageManager.open_db()
        device_data = db[device_id]
        StorageManager.close_db(db)
        return device_data


if __name__ == '__main__':
    storage_manager = StorageManager()
    storage_manager.update_registry('192.168.0.0','2000','123abc')
    storage_manager.get_device('123abc')
        

