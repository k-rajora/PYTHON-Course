# main.py
import math_utils          # import the whole module (use module.name)
from math_utils import add, circle_area as area  # selective import + alias
import math_utils as mu    # alias the module

print(math_utils.PI)       # 3.14159
print(add(4, 5))           # 9
print(area(3))             # circle_area via alias
print(mu.Calculator().multiply(2,3))  # 6
print(mu.Calculator().multiply(4,3))