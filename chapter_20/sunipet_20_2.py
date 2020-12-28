#リストのディクショナリの直積集合
from itertools import  product

dict0 = {"a":["1", "2"], "b":["+", "*"], "c":["!", "@"]}
jobs = (dict(zip(dict0, i)) for i in product(*dict0.values()))
for i in jobs: print(i)