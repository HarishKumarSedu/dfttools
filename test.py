import sys
import inspect
from dfttools import *
# def is_main_caller():
#     # Inspect call stack to get the first frame outside tartools
#     for frame_info in inspect.stack():
#         # frame_info.frame.f_globals is the global namespace of the caller
#         # print(frame_info.frame.f_globals.get('glob'))
#         glob_module = frame_info.frame.f_globals.get('glob')
#         # print(inspect.getmembers(glob_module))
#         classes = [member for member in inspect.getmembers(glob_module, inspect.isclass)]
#         instance = glob_module.()  # or get the instance you want to inspect

#         # Get all attributes on the instance including properties evaluated
#         members = inspect.getmembers(instance)

#         # Filter to find your property value
#         callback_keys_value = dict(members).get('callback_keys')

#         print(callback_keys_value)
#         # print(classes)

#         if frame_info.frame.f_globals.get("__name__") == "__main__":
#             return True
#     return False

if __name__ == '__main__':
    from dfttools import *

    cls = g
    import inspect

    # Get all properties in the class
    properties = [member for member in inspect.getmembers(cls, lambda o: isinstance(o, property))]
    
    # This will include ('callback_keys', <property object at ...>)
    print(properties)
    instance = cls()
    value = instance.callback_keys  # This executes the @property getter
    print(value)  # Should print the keys of hardware_callbacks

# import inspect
# import dfttools.glob

# class GlobalContext(dfttools.glob.GlobalContext):
#     def __init__(self):
#         super().__init__()
#         self.cache = {}

#     def cache_callback_keys(self):
#         # Access the @property value
#         keys = self.callback_keys
#         # Store in a dedicated cache dictionary
#         self.cache['callback_keys'] = list(keys)

#     def dump_cache(self):
#         global dumped_cache
#         dumped_cache = self.cache.copy()
#         self.cache.clear()


# if __name__ == '__main__':
#     # Create instance of extended GlobalContext
#     instance = GlobalContext()

#     # Inspect properties on class
#     properties = [member for member in inspect.getmembers(type(instance), lambda o: isinstance(o, property))]
#     print("Properties in GlobalContext class:", properties)  # Should include callback_keys property

#     # Cache the callback_keys property value into cache dict
#     instance.cache_callback_keys()

#     # Access cached keys
#     print("Cached callback_keys:", instance.cache['callback_keys'])

#     # Dump cache globally at end
#     instance.dump_cache()
#     print("Dumped cache globally:", dumped_cache)
