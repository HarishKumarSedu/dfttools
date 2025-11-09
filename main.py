from cache import NestedDB,detect_and_handle_main_db

from Startup import startup
def test1(db=None):
    db.create({'Instruction': 'I2C', 'unit': 'W', 'data': {'Reg': 0x0f, 'data': 0x1E}, 'comments': ''})
    db.create({'Instruction': 'I2C', 'unit': 'W', 'data': {'Reg': 0x0B, 'data': 0x1E}, 'comments': ''})
    db.create({'Instruction': 'I2C', 'unit': 'W', 'data': {'Reg': 0x0C, 'data': 0x1E}, 'comments': ''})
    startup(db=db)
if __name__ == '__main__':
    # detect_and_handle_main_db()
    db = NestedDB()
    test1(db=db)
    globals()['__cache__'] = db.find({'Instruction':'I2C'})
    print("Final DB dumped to '__cache__'")
    print(globals().get('__cache__'))

