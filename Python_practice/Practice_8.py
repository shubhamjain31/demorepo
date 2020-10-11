class A:
	val = 1
class B(A):
	pass
class C(A):
	pass
	
print(A.val,B.val,C.val)
B.val = 2
print(A.val,B.val,C.val)
A.val = 3
print(A.val,B.val,C.val)