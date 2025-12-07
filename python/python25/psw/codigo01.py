a = "a"
b = "b"

c, d = "cd"
e, f = "e", "f"

print(a, b, c, d, e, f)

e, f = f, e

print(a, b, c, d, e, f)

a += b
print(a)

a *= 5
print(a)