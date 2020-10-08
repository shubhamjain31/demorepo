x = {"a":1,"b":2}
y = {"b":3,"c":4}

#In python 3.5+
z = {**x,**y}
print(z)

#In python 2x
z = dict(x,**y)
print(z)