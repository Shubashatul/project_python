import random

a=int(input("Enter lower limit: "))
b=int(input("Enter upper limit: "))
x=random.randint(a,b)
print("\n")
print("Range is (%d,%d) and randomly picked number is %d"%(a,b,x))

# checking for positive and negitive.
if (x==0):
    print("%d is neither positive nor negitive"%x)
elif (x>0):
    print("%d is positive number"%x)
else:
    print("%d is negitive number"%x)

# checking for odd and even.
if(x%2==0):
    print("%d is an even number"%x)
else:
    print("%d is an odd number"%x)

# checking for prime and composite.
def prime(x):
    for i in range(2,x):
        if(x%i==0):
            return False
    return True
if(x==1 or x==0):
    print("%d is netiher a prime number nor composite number"%x)
elif(prime(x)):
    print("%d is a prime number"%x)
else:
    print("%d is a composite number"%x)