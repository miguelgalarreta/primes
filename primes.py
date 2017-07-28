import math
def get_primes(n):
    primes=[2]
    for i in range(3,math.ceil(math.sqrt(n))+1,2):    
        if n%i==0:
            primes.append(i)
    return primes

def get_prime_factors(n):
    primes = get_primes(n)
    i=0
    factors =[]
    while n>1:
        if n%primes[i]==0:
            factors.append(primes[i])
            n/=primes[i]
        else:
            i+=1;
    return factors

test_value=20
print("*".join(map(str,get_prime_factors(test_value))))
