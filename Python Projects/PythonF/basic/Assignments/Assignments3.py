#Name : Eugene Parker
#Task : Given the number is a prime

user_prime = 100
prime_flag = True

for i in range(2,user_prime-1):
    if user_prime%i == 0:
        prime_flag = False
if(prime_flag):
    print("Prime Number")
else:
    print("Not a prime number")
