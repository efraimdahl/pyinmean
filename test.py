import sys
import os

print("Hello")
# Adjust path to your .so file
so_dir = os.path.abspath("build")
sys.path.insert(0, so_dir)

print("Looking in:", so_dir)
import pyima
#0,1,4,5,6,7,10,14,20
print("Success! Module loaded.")
print(pyima.get_normalized_ima([0,1,4,5,6,7,10,14,20],False))