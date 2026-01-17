_dic = {"a":1, "b":2, "c":3}

print(_dic)
print(_dic.get("a"))

#del _dic["c"]
#print(_dic)

_dic["c"] = 3
print(_dic)


print(list(_dic.keys()))
print(list(_dic.values()))
print(list(_dic.items()))