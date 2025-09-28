# assignment_3.py
import json
import csv
import yaml
import xml.etree.ElementTree as ET
from typing import TypedDict
from collections import namedtuple
from dataclasses import dataclass
from pydantic import BaseModel
import numpy as np
import time
import pandas as pd

# 1. Example data
user_data = [
    {"id": 1, "name": "Apurav", "email": "apurav@example.com"},
    {"id": 2, "name": "Alice", "email": "alice@example.com"},
]

# JSON
with open("users.json", "w") as f:
    json.dump(user_data, f, indent=4)

# CSV
with open("users.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name", "email"])
    writer.writeheader()
    writer.writerows(user_data)

# YAML
with open("users.yaml", "w") as f:
    yaml.dump(user_data, f)

# XML
root = ET.Element("users")
for user in user_data:
    user_elem = ET.SubElement(root, "user")
    for key, value in user.items():
        elem = ET.SubElement(user_elem, key)
        elem.text = str(value)
tree = ET.ElementTree(root)
tree.write("users.xml")

# 2. User structures
class UserTypedDict(TypedDict):
    id: int
    name: str
    email: str

UserNamedTuple = namedtuple("UserNamedTuple", ["id", "name", "email"])

@dataclass
class UserDataClass:
    id: int
    name: str
    email: str

class UserPydantic(BaseModel):
    id: int
    name: str
    email: str

# 3. Numerical data
py_list = [1, 2, 3, 4, 5]
np_array = np.array([1, 2, 3, 4, 5])

# 4. Decorator for execution time
def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.6f} seconds")
        return result
    return wrapper

# 5. Scalar-vector multiplication
@timeit
def multiply_list(lst, scalar):
    return [x * scalar for x in lst]

@timeit
def multiply_numpy(arr, scalar):
    return arr * scalar

multiply_list(py_list, 1000000)
multiply_numpy(np_array, 1000000)

# 6. Load CSV into Pandas
df = pd.read_csv("users.csv")
print("\nCSV DataFrame contents:")
print(df)
