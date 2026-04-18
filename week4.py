#function
import array


def add():
    a=10
    b=20
    c=a+b
    print("the sum is: ",c)
add()   

def sum(a,b):
    return a+b  
print(sum(20,30))

#array

arr=array.array('i',[1,2,3,4,5])
print(arr)
arr.append(6)
print(arr)
arr.insert(0,0)
print(arr)
arr.pop()
print(arr)
arr.remove(3)
print(arr)
arr.reverse()
print(arr)
