import random
import math

#To generate random prime less than N
def randPrime(N):
	primes = []
	for q in range(2,N+1):
		if(isPrime(q)):
			primes.append(q)
	return primes[random.randint(0,len(primes)-1)]

# To check if a number is prime
def isPrime(q):
	if(q > 1):
		for i in range(2, int(math.sqrt(q)) + 1):
			if (q % i == 0):
				return False
		return True
	else:
		return False

#pattern matching
def randPatternMatch(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatch(q,p,x)

#pattern matching with wildcard
def randPatternMatchWildcard(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatchWildcard(q,p,x)

# return appropriate N that satisfies the error bounds
def findN(eps,m):

	#So here is the logic that I am using to find N.
    #Consider any string x and let s1 and s2 be two substrings of it of length m.
    #Then for a prime q, hash of s1 and s2 would be the same if q divides f(s1)-f(s2)

    #now suppose I am choosing N with primes less than it denoted by pi(N)
    #Since a prime is chose uniformly, among these primes, the probability that f(s1) 
    #and f(s2) have same hash is d(f(s1)-f(s2))/pi(N)<=log_2(f(s1)-f(s2))/pi(N)<=log_2(26^m)/pi(N)=mlog_2(26)/pi(N)
    #where d(j) denotes the number of distinct prime divisors of j. Because the max and min values of f are 26^m-1 and 0 respectively,
    #the 26^m term is used.

    #So for any string s of length m that is a substring of x, the probability of it colliding with p is mlog_2(26)/pi(N).
    #We want this <= epsilon. So N/log_2(N) >=2log_2(26)m/epsilon, that is a constant times m/epsilon.

    #Now suppose N=tlogt. Then N/log_2(N)>=t/2. So we set t>= 4log_2(26)m/epsilon . So using log_2(26) as roughly 5, we set t to 
    # be 30m/epsilon. So N=30m/epsilon log_2(30m/epsilon).

    #Moreover any prime that is generated from random prime would be less than N implying log(q)<log(N) which is atmost 2log(m/epsilon).
    #Thus log(q) is linear in log(m/epsilon) and thus would give the space and time complexity that is desired  for rand Pattern match.

    var=m/eps
    var=var*30
    var2=math.log(var,2)
    N=int(var*var2+10)
    return N



# Return sorted list of starting indices where p matches x
def modPatternMatch(q,p,x):
	
    #q is prime number, p is pattern and x is the text.

    #first find f(p) and f(x[0.....(m-1)])

    #m and n requiring O(logn) space (m<=n)
    # logm space for index iterating over p (indexm), logm<=logn
    #log q space for storing f(p)
    #pw for storing power of 26 mod q, again logq space
    #logq space for storing the instantaneous value of f(x[i.....(i+m-1)])
    #indexn for storing the ending of m sized string of the text that is compared with the pattern, requires logn space
    #list L that would be the output, would require O(k) space where k is the size of the output list.

    m=len(p)
    n=len(x)
    indexm=m-1
    fp=int(0)
    pw=int(1)
    fx=int(0)
    indexn=m
    L=[]

    #the while loop is run m times and bit oerations require logq time.(Actually changing indexm
    #would be logm but the assignment has no mention of this)

    while(indexm>=0):
        fp=(fp+pw*(ord(p[indexm])-ord('A')))%q
        fx=(fx+pw*(ord(x[indexm])-ord('A')))%q
        pw=(pw*26)%q
        indexm=indexm-1

     #now pw has the value 26^m mod q

    if(fx%q==fp%q):
        L.append(int(0))


    # now we use the following relation: 26*f(x[i.....(i+m-1)])-26^m(ord(x[i])-ord('A'))+(ord(x[i+m])-ord('A'))=f(x[(i+1)......(i+m)])
    while(indexn<n):

        fx=(fx*26)%q
        fx=(fx-pw*(ord(x[indexn-m])-ord('A')))%q
        fx=(fx+q)%q  #just in case fx is negative
        fx=(fx+ord(x[indexn])-ord('A'))%q
        if(fx%q==fp%q):
            L.append(indexn-m+1)
        indexn=indexn+1

    return L

# Return sorted list of starting indices where p matches x
def modPatternMatchWildcard(q,p,x):

	#The idea for this is exactly same as the above function, just that we ignore the character at the position of ? in the m sized 
    #substring  of x that we are currently comparing with p

    m=len(p)
    n=len(x)
    indexm=m-1
    pw=int(1)
    fx=int(0)
    fp=int(0)
    indexn=m
    L=[]

    #a variable for storing 26^i mod q where the (i+1)th position from right contains ?
    #a variable for storing i where the (i+1)th positon from the left contains ?
    sppw=int(0)
    idx=int(0)

    while(indexm>=0):
        if(p[indexm]!='?'):
            fp=(fp+pw*(ord(p[indexm])-ord('A')))%q
        else:
            sppw=pw
            idx=indexm

        fx=(fx+pw*(ord(x[indexm])-ord('A')))%q
        pw=(pw*26)%q
        indexm=indexm-1

    #a dummy variable for calculations
    temp=fx
    temp=(temp-sppw*(ord(x[idx])-ord('A')))%q
    temp=(temp+q)%q
    if(temp%q==fp%q):
        L.append(int(0))

    while(indexn<n):

        fx=(fx*26)%q
        fx=(fx-pw*(ord(x[indexn-m])-ord('A')))%q
        fx=(fx+q)%q  #just in case fx is negative
        fx=(fx+ord(x[indexn])-ord('A'))%q

        temp=fx
        temp=(temp-sppw*(ord(x[indexn-m+1+idx])-ord('A')))%q
        temp=(temp+q)%q
        if(temp%q==fp%q):
            L.append(indexn-m+1)

        indexn=indexn+1

    return L




    

