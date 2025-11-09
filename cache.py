import uuid
import time
from collections import defaultdict
from copy import deepcopy

class NestedDB:
    def __init__(self):
        self.records = {}
        self.reverse_index = defaultdict(lambda: defaultdict(set))

    def _flatten_dict(self, d, parent_key=''):
        items = {}
        for k, v in d.items():
            new_key = f"{parent_key}.{k}" if parent_key else k
            if isinstance(v, dict):
                items.update(self._flatten_dict(v, new_key))
            else:
                items[new_key] = v
        return items

    def _index_record(self, record):
        flat_record = self._flatten_dict(record)
        for key, val in flat_record.items():
            if key != '_id':
                self.reverse_index[key][val].add(record['_id'])

    def _deindex_record(self, record):
        flat_record = self._flatten_dict(record)
        for key, val in flat_record.items():
            if key != '_id':
                self.reverse_index[key][val].discard(record['_id'])

    def create(self, record_data):
        rec = deepcopy(record_data)
        rec['_id'] = str(uuid.uuid4())
        rec['_created'] = time.time()
        self.records[rec['_id']] = rec
        self._index_record(rec)
        return rec['_id']

    def read(self, _id):
        rec = self.records.get(_id)
        return deepcopy(rec) if rec else None

    def update(self, _id, update_data):
        if _id not in self.records:
            raise KeyError(f"Record with _id {_id} not found")
        old_rec = self.records[_id]
        self._deindex_record(old_rec)
        old_rec.update(update_data)
        self.records[_id] = old_rec
        self._index_record(old_rec)

    def delete(self, _id):
        rec = self.records.pop(_id, None)
        if not rec:
            return False
        self._deindex_record(rec)
        return True

    def _match_criteria(self, record, criteria):
        flat_record = self._flatten_dict(record)
        for key, val in criteria.items():
            if flat_record.get(key) != val:
                return False
        return True

    def find(self, criteria):
        candidate_sets = []
        for ck, cv in criteria.items():
            ids = self.reverse_index.get(ck, {}).get(cv)
            if ids:
                candidate_sets.append(ids)
            else:
                return []
        candidate_ids = set.intersection(*candidate_sets) if candidate_sets else set(self.records.keys())
        return [deepcopy(self.records[_id]) for _id in candidate_ids if self._match_criteria(self.records[_id], criteria)]

    def find_last_record(self, criteria):
        matched = self.find(criteria)
        if not matched:
            return None
        return max(matched, key=lambda r: r.get('_created', 0))

    # def dump(self):
    #     return deepcopy(list(self.records.values()))
    def dump(self):
        """
        Return list of records with '_id' and '_created' fields excluded.
        """
        all_records = deepcopy(list(self.records.values()))
        filtered_records = []
        for rec in all_records:
            filtered = {k: v for k, v in rec.items() if k not in ('_id', '_created')}
            filtered_records.append(filtered)
        return filtered_records


    def count(self, criteria=None):
        if criteria:
            return len(self.find(criteria))
        return len(self.records)
    
    def delete_by_criteria(self, criteria):
        records_to_delete = self.find(criteria)
        count = 0
        for rec in records_to_delete:
            if self.delete(rec['_id']):
                count += 1
        return count
    
    def find_modify_update(self, criteria, modify_func):
        """
        Finds all records matching criteria, applies modify_func(record) to each,
        updates and returns updated records list.
        """
        records = self.find(criteria)
        updated = []
        for rec in records:
            modified = deepcopy(rec)
            modified = modify_func(modified)
            if modified and modified != rec:
                self.update(rec['_id'], modified)
                updated.append(self.read(rec['_id']))
        return updated
    
    def clear(self):
        self.records.clear()
        self.reverse_index.clear()


import inspect

def detect_and_handle_main_db():
    frame = inspect.currentframe()
    try:
        caller_globals = frame.f_back.f_globals
        # Check if the caller's module is running as __main__
        if caller_globals.get('__name__') == '__main__':
            # Find NestedDB instance(s) in caller globals
            db_instances = [v for v in caller_globals.values() if type(v).__name__ == 'NestedDB']
            if db_instances:
                db = db_instances[0]  # assume first instance
                # print("Detected main module, clearing database...")
                if hasattr(db, 'clear'):
                    db.clear()
                else:
                    db.records.clear()
                    db.reverse_index.clear()
                # Logic to accumulate data goes in main module
                # At end dump db to __cache__
                # caller_globals['__cache__'] = db.dump()
                # print("Database dumped to '__cache__' global")
    finally:
        del frame

# Example usage demonstrating all APIs
if __name__ == "__main__":
    db = NestedDB()

    # Create
    id1 = db.create({'Instruction': 'I2C', 'unit': 'W', 'data': {'Reg': 0x0f, 'data': 0x1E}, 'comments': ''})
    id2 = db.create({'Instruction': 'Force', 'unit': 'V', 'data': {'P+': 'IODATA0', 'P-': 'GND', 'value': 0.5e-3}, 'comments': ''})
    
    print("All records after creation:")
    print(db.dump())

    # Read
    print("\nRead record id1:")
    print(db.read(id1))

    # Find
    criteria = {'Instruction': 'I2C', 'data.Reg': 0x0f}
    found = db.find(criteria)
    print("\nFind records matching criteria", criteria)
    for item in found:
        print(item)

    # Find last record
    last = db.find_last_record(criteria)
    print("\nLast record matching criteria:")
    print(last)

    # Update
    print("\nUpdate record id1 - add comment and change data:")
    db.update(id1, {'comments': 'Updated comment', 'data': {'Reg': 0x0f, 'data': 0x2F}})
    print(db.read(id1))

    # Find-modify-update in one step
    print("\nFind-modify-update each 'Force' record by appending '[MODIFIED]' to comments:")
    def modify_func(rec):
        rec['comments'] = rec.get('comments', '') + ' [MODIFIED]'
        return rec
    updated_list = db.find_modify_update({'Instruction': 'Force'}, modify_func)
    for rec in updated_list:
        print(rec)

    # Count
    print("\nCount records with Instruction='I2C':", db.count({'Instruction': 'I2C'}))

    # Delete by id
    print("\nDelete record id2:")
    db.delete(id2)
    print(db.dump())

    # Delete by criteria
    print("\nDelete remaining 'I2C' records by criteria:")
    deleted_count = db.delete_by_criteria({'Instruction': 'I2C'})
    print("Deleted count:", deleted_count)
    print(db.dump())
