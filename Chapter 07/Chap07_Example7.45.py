myl1 = [1,2,3,4,5]
myl2 = myl1[:]
print(id(myl1))
print(id(myl2))
print("Initially")
print(" myl1 is: ", myl1)
print(" myl2 is: ", myl2)
print("--------------------")
myl1[2] = 23
print("Modifying myl1")
print(" myl1 is: ", myl1)
print(" myl2 is: ", myl2)
print("--------------------")
myl2[3] = 24
print("Modifying myl2")
print(" myl1 is: ", myl1)
print(" myl2 is: ", myl2)