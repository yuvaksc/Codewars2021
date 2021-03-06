A = input()
B = input()
C = input()

print(A, "* (" + B, "+", C + ") =", A, "*", B, "+", A, "*", C)
c1 = int(B) + int(C)
c2 = int(A) * int(B)
c3 = int(A) * int(C)

print(A, "*", str(c1), "=", str(c2), "+", str(c3))
c4 = int(A) * c1
c5 = c2 + c3
print(c4, "=", c5)

