from cache import NestedDB

def startup(db=None):
    db.create({'Instruction': 'Force', 'unit': 'V', 'data': {'P+': 'IODATA0', 'P-': 'GND', 'value': 0.5e-3}, 'comments': ''})
    
if __name__ == '__main__':
    db = NestedDB()
    startup(db=db)
