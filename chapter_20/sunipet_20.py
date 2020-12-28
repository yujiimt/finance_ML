# -*- coding: utf-8 -*-

# ベクトル化されていない直積集合演算
# リストのディクショナリの直積集合

dict0 = {"a":["1", "2"], "b":["+", "*"], "c":["!", "@"]}
for a in dict0["a"]:
    for b in dict0["b"]:
        for c in dict0["c"]:
            print({"a": a, "b":b, "c":c})