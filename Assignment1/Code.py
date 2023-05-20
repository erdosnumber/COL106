#Code for Assignment 1 of COL106


class ArrayStack:


	#Creating a stack of size 100 of sz-tuples

	def __init__(self,sz) -> None:


		#self.last stores the last position occupied of the list

		self.size=sz
		l=[0]*self.size
		self.data=[l]*100
		self.last=0
		self.length=100

	def doublesize(self):

			l1=[0]*self.size
			l2=[l1]*self.length
			self.data=self.data+l2
			self.length*=2


	def push(self,e):

		if(self.last==self.length-1):
			self.doublesize()

		self.data[self.last+1]=e
		self.last+=1


	def pop(self):

		l1=[0]*self.size

		self.data[self.last]=l1
		self.last-=1


	def top(self):

		l1=self.data[self.last]
		return l1

	def is_empty(self):

		if(self.last==-1):
			return True


	def stacksize(self):

		return self.last+1




		

		

	






def findPositionandDistance(s):




	#We create a list of 5-tuple that would be used as a stack

	#For the string 99(+X-Y-Z)32(+X63(-Y-Z)), we define the coefficients to be the numbers 99,32 and 63, basically all those m's mentioned in the
	#7th instruction of the drone program in the assignment


	#The stack is of {coefficient of current paranthesis,displacement in x for current paranthesis,displacement in y for current paranthesis,
	# displacement in z for current paranthesis, distance travelled in current paranthesis}
	#Whenever a paranthesis gets opened we add a new 5-tuple to the stack=[coefficient,0,0,0,0]
	#Whenever a paranthesis gets closed, we pop a tuple from the stack, let it be [a,b,c,d,e]. And after popping let the topmost element
	#now be [A,B,C,D,E]. Then we update [A,B,C,D,E] to [A,B+a*b,C+a*c,D+a*d,E+a*e]

	Stack=ArrayStack(5)



	#for finding coefficients, we need to convert string to int, so let num be a string that first collects the digits of a coefficient
	#in a string which we then convert to int
	num='0'



	for i in range(len(s)):

		if (s[i]!='(' and s[i]!=')' and s[i]!='+' and s[i]!='-' and s[i]!='X' and s[i]!='Y' and s[i]!='Z'):

			num=num+s[i]

		elif (s[i]=='('):

			coeff=int(num)
			num='0'

			Stack.push([coeff,0,0,0,0])

		elif (s[i]=='+' and s[i+1]=='X'):

			l1=Stack.top()
			Stack.pop()

			l1[1]+=1
			l1[4]+=1

			Stack.push(l1)
			i+=1

		elif (s[i]=='+' and s[i+1]=='Y'):

			l1=Stack.top()
			Stack.pop()

			l1[2]+=1
			l1[4]+=1

			Stack.push(l1)
			i+=1
			

		elif (s[i]=='+' and s[i+1]=='Z'):

			l1=Stack.top()
			Stack.pop()

			l1[3]+=1
			l1[4]+=1

			Stack.push(l1)
			i+=1

		elif (s[i]=='-' and s[i+1]=='X'):

			l1=Stack.top()
			Stack.pop()

			l1[1]-=1
			l1[4]+=1

			Stack.push(l1)
			i+=1

		elif (s[i]=='-' and s[i+1]=='Y'):

			l1=Stack.top()
			Stack.pop()

			l1[2]-=1
			l1[4]+=1

			Stack.push(l1)
			i+=1

		elif (s[i]=='-' and s[i+1]=='Z'):

			l1=Stack.top()
			Stack.pop()

			l1[3]-=1
			l1[4]+=1

			Stack.push(l1)
			i+=1

		elif(s[i]==')'):

			l1=Stack.top()
			Stack.pop()
			l2=Stack.top()
			Stack.pop()

			l2[1]+=(l1[1]*l1[0])
			l2[2]+=(l1[2]*l1[0])
			l2[3]+=(l1[3]*l1[0])
			l2[4]+=(l1[4]*l1[0])

			Stack.push(l2)




	ans=Stack.top()

	return [ans[1],ans[2],ans[3],ans[4]]
			











