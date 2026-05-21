import sys
import ctypes

print("Python has three numeric types: int, float, and complex")
myValue=2003
print(myValue)
print(type(myValue))
print(sys.getsizeof(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

myValue=2003 #3.14
print(myValue)
print(type(myValue))
#print(str(myValue) + " is of the data type " + str(type(myValue)))
print(f"{(myValue)}is of the the data type " + str(type(myValue)))
print(sys.getsizeof(myValue))
myValue = ctypes.c_int(100)
print(ctypes.sizeof(myValue))

myValue=5j
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
print(sys.getsizeof(myValue))


myValue=True
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
print(sys.getsizeof(myValue))