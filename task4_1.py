def is_prime(n):
    isprime=True
    if n<=1 :
        isprime=False
        return isprime

    for i in range(2,n):
        if n % i==0:
            isprime=False
            return isprime
            break
    return isprime
        
n= int(input("Enter a Number!"))
if is_prime(n):
    print(f"Number {n} is prime")
else:
    print(f"Number {n} is not prime")


