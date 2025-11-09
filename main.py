from dfttools.glob import db
from dfttools import *
from Startup import startup
def test1():
    I2C_REG_WRITE(0x38,0x0E,0x01,0)
if __name__ == '__main__':
    # detect_and_handle_main_db()
    db = NestedDB()
    test1(db=db)
    globals()['__cache__'] = db.find({'Instruction':'I2C'})
    print("Final DB dumped to '__cache__'")
    print(globals().get('__cache__'))

