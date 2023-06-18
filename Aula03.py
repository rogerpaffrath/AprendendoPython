# DATA TYPES
'''
DATA IN PYTHON CAN BE STORED IN 

str FOR TEXTS
int, float, complex FOR NUMERIC
list, tuple, range FOR SEQUENCES
dict FOR MAPPING
set, frozenset FOR SETS
bool FOR BOOLEAN
bytes, bytearray, memoryview FOR BINARIES
NoneType FOR NONE
'''

# CASTING - SET EXPLICITALY THE TYPE
# TEXT
var_string = str("3")
var_string_2 = str('This is also a string.')

# NUMERIC
var_float = float(5)
var_int = int(5)
var_complex = complex(1j)

var_result = var_float + var_int

print(type(var_result), var_result)

# SEQUENCES
var_list = list(["banana", "limão", "batata"])
var_tuple = tuple(("Aula 1", "Aula 2", "Aula 3"))
var_range = range(6)

print(var_list)

# MAPPING
var_dict = dict({"name" : "Roger", "age" : 32})

print(var_dict["name"])

# SET
var_frozenset = frozenset({"banana", "limão", "batata"})

print(var_frozenset)

# BOOLEAN
var_boolean_true = bool(True)
var_boolean_false = bool(False)

# BINARIES
var_bytes = bytes(b"Hello")
var_bytearray = bytearray(5)
var_memoryview = memoryview(var_bytes)

print(var_memoryview)

# NONE
var_none = None

print(var_none)