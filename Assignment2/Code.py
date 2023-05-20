	
rev=[] #For each index i it stores that j such that ((x[i+1]-x[i])/(v[i]-v[i+1]),i) is stored in the jth node of the minheap
arr=[] #For earch node j of the minheap it stores its corresponding i
last=[] #stores the last collision time for every mass in that order

def compare(a,b):
	if (a[0]<b[0]):
		return True
	elif(a[0]>b[0]):
		return False
	elif(a[0]==b[0] and a[1]<=b[1]):
		return True
	else:
		return False

class MinHeap:

	def __init__(self,l) -> None:

		#constructing the heap using the fast build heap method of complexity O(n)
		self.sz=len(l)
		pow=int(1)
		while (pow<self.sz):
			pow*=2
		self.max=pow
		inside=[None]*len(l[0])
		self.heap=[inside]*self.max
		for i in range(self.sz-1,-1,-1):
			self.heap[i]=l[i]
			rev[l[i][1]]=i
			arr[i]=l[i][1]
			pos=i
			while(True):
				if(2*pos+1>=self.sz):
					break
				elif(2*pos+2>=self.sz):
					if(compare(self.heap[2*pos+1],self.heap[pos])):
						self.heap[2*pos+1], self.heap[pos]=self.heap[pos], self.heap[2*pos+1]
						arr[pos]=self.heap[pos][1]
						arr[2*pos+1]=self.heap[2*pos+1][1]
						rev[self.heap[pos][1]]=pos
						rev[self.heap[2*pos+1][1]]=2*pos+1
					break
				elif(compare(self.heap[2*pos+1],self.heap[pos]) and compare(self.heap[2*pos+1],self.heap[2*pos+2])):
					self.heap[2*pos+1], self.heap[pos]=self.heap[pos], self.heap[2*pos+1]
					arr[pos]=self.heap[pos][1]
					arr[2*pos+1]=self.heap[2*pos+1][1]
					rev[self.heap[pos][1]]=pos
					rev[self.heap[2*pos+1][1]]=2*pos+1
					pos=2*pos+1
				elif(compare(self.heap[2*pos+2],self.heap[pos]) and not compare(self.heap[2*pos+1],self.heap[2*pos+2])):
					self.heap[2*pos+2], self.heap[pos]=self.heap[pos], self.heap[2*pos+2]
					arr[2*pos+2]=self.heap[2*pos+2][1]
					arr[pos]=self.heap[pos][1]
					rev[self.heap[2*pos+2][1]]=2*pos+2
					rev[self.heap[pos][1]]=pos
					pos=2*pos+2
				else:
					break
						
	def doubleheap(self):	
		inside=[None]*len(self.heap[0])	
		for i in range(self.max):
			self.heap.append(inside)
		self.max*=2

	def is_heap_empty(self):
		if(self.sz==0):
			return True

	def printheap(self):
		for i in range(self.sz):
			print(self.heap[i],end=" ")

	def heapsize(self):
		return self.sz

	def replace(self,i,x):
		if(not compare(self.heap[i],x)):
			#i is the node value
			#perform heap up as x>self.heap[i]
			self.heap[i]=[x[0], x[1]]
			rev[x[1]] = i
			arr[i] = x[1]
			pos=i
			
			while(pos>0 and compare(self.heap[pos],self.heap[(pos-1)//2])):
				
				self.heap[(pos-1)//2],self.heap[pos]=self.heap[pos],self.heap[(pos-1)//2]
				arr[pos]=self.heap[pos][1]
				arr[(pos-1)//2]=self.heap[(pos-1)//2][1]
				rev[self.heap[pos][1]]=pos
				rev[self.heap[(pos-1)//2][1]]=(pos-1)//2
				pos=(pos-1)//2
		else:
			#perform heap down
			self.heap[i]=[x[0], x[1]]
			rev[x[1]] = i
			arr[i] = x[1]
			pos=i
			while(True):
				if(2*pos+1>=self.sz):
					break
				elif(2*pos+2>=self.sz):
					if(compare(self.heap[2*pos+1],self.heap[pos])):
						self.heap[2*pos+1], self.heap[pos]=self.heap[pos], self.heap[2*pos+1]
						arr[pos]=self.heap[pos][1]
						arr[2*pos+1]=self.heap[2*pos+1][1]
						rev[self.heap[pos][1]]=pos
						rev[self.heap[2*pos+1][1]]=2*pos+1
					break
				elif(compare(self.heap[2*pos+1],self.heap[pos]) and compare(self.heap[2*pos+1],self.heap[2*pos+2])):
					self.heap[2*pos+1], self.heap[pos]=self.heap[pos], self.heap[2*pos+1]
					arr[pos]=self.heap[pos][1]
					arr[2*pos+1]=self.heap[2*pos+1][1]
					rev[self.heap[pos][1]]=pos
					rev[self.heap[2*pos+1][1]]=2*pos+1
					pos=2*pos+1
				elif(compare(self.heap[2*pos+2],self.heap[pos]) and not compare(self.heap[2*pos+1],self.heap[2*pos+2])):
					self.heap[2*pos+2], self.heap[pos]=self.heap[pos], self.heap[2*pos+2]
					arr[pos]=self.heap[pos][1]
					arr[2*pos+2]=self.heap[2*pos+2][1]
					rev[self.heap[pos][1]]=pos
					rev[self.heap[2*pos+2][1]]=2*pos+2
					pos=2*pos+2
				else:
					break


	def enqueue(self,x):
		#putting x in the first unoccupied node of the almost complete binary tree and performing heap up
		if(self.max==self.sz):
			self.doubleheap()
		pp=[x[0],x[1]]
		self.heap[self.sz]=pp
		arr[self.sz]=x[1]
		rev[x[1]]=self.sz
		self.sz+=1
		pos=self.sz-1
		while(pos>0 and compare(self.heap[pos],self.heap[(pos-1)//2])):
			self.heap[(pos-1)//2],self.heap[pos]=self.heap[pos],self.heap[(pos-1)//2]
			arr[pos]=self.heap[pos][1]
			arr[(pos-1)//2]=self.heap[(pos-1)//2][1]
			rev[self.heap[pos][1]]=pos
			rev[self.heap[(pos-1)//2][1]]=(pos-1)//2
			pos=(pos-1)//2
			
	def removemin(self):

		min=self.heap[0]
		if(self.sz==1):
			rev[min[1]]=None
			arr[0]=None
			self.sz-=1
			return min

		else:
			rev[min[1]]=None
			rev[self.heap[self.sz-1][1]]=0
			arr[0]=self.heap[self.sz-1][1]
			arr[self.sz-1]=None
			pp=[self.heap[self.sz-1][0],self.heap[self.sz-1][1]]
			self.heap[0]=pp
			self.heap[self.sz-1]=None
			self.sz-=1
			pos=int(0)
			while(True):
				if(2*pos+1>=self.sz):
					break
				elif(2*pos+2>=self.sz):
					if(compare(self.heap[2*pos+1],self.heap[pos])):
						self.heap[2*pos+1], self.heap[pos]=self.heap[pos], self.heap[2*pos+1]
						arr[pos]=self.heap[pos][1]
						arr[2*pos+1]=self.heap[2*pos+1][1]
						rev[self.heap[pos][1]]=pos
						rev[self.heap[2*pos+1][1]]=2*pos+1
					break
				elif(compare(self.heap[2*pos+1],self.heap[pos]) and compare(self.heap[2*pos+1],self.heap[2*pos+2])):
					self.heap[2*pos+1], self.heap[pos]=self.heap[pos], self.heap[2*pos+1]
					arr[pos]=self.heap[pos][1]
					arr[2*pos+1]=self.heap[2*pos+1][1]
					rev[self.heap[pos][1]]=pos
					rev[self.heap[2*pos+1][1]]=2*pos+1
					pos=2*pos+1
				elif(compare(self.heap[2*pos+2],self.heap[pos]) and not compare(self.heap[2*pos+1],self.heap[2*pos+2])):
					self.heap[2*pos+2], self.heap[pos]=self.heap[pos], self.heap[2*pos+2]
					arr[pos]=self.heap[pos][1]
					arr[2*pos+2]=self.heap[2*pos+2][1]
					rev[self.heap[pos][1]]=pos
					rev[self.heap[2*pos+2][1]]=2*pos+2
					pos=2*pos+2
				else:
					break
			return min

def listCollisions(M,x,v,m,T):

	arr.clear()
	rev.clear()
	last.clear()
	
	n=len(M)
	collisiontime=[]
	for i in range(n-1):
		if(v[i+1]-v[i]<0):
			collisiontime.append([(x[i+1]-x[i])/(v[i]-v[i+1]),i])

	for i in range(n):
		arr.append(None)
		rev.append(None)
		last.append(float(0))

	collisions=int(0)
	el=float(0)
	ans=[]
	if(len(collisiontime)!=0):
		heap=MinHeap(collisiontime)

		while(collisions<m and el<T):
			if(heap.is_heap_empty()):
				break
			pa=heap.removemin()
			if(pa[0]>T):
				break			
			el=pa[0]
			collisions+=1
			i=pa[1]
			x[i]=x[i]+(el-last[i])*v[i]
			x[i+1]=x[i+1]+(el-last[i+1])*v[i+1]
			last[i]=el
			last[i+1]=el
			v1=((M[i]-M[i+1])*v[i]+2*M[i+1]*v[i+1])/(M[i]+M[i+1])
			v2=((M[i+1]-M[i])*v[i+1]+2*M[i]*v[i])/(M[i]+M[i+1])
			v[i]=v1
			v[i+1]=v2
			ans.append((round(pa[0],4),pa[1],round(x[i],4)))


			if(i-1>=0):
				xtemp=x[i-1]+v[i-1]*(el-last[i-1])
				if(rev[i-1]==None and v[i]-v[i-1]<0):
					heap.enqueue([(x[i]-xtemp)/(v[i-1]-v[i])+el,i-1])
				elif(rev[i-1]!=None and v[i]-v[i-1]<0):
					heap.replace(rev[i-1],[(x[i]-xtemp)/(v[i-1]-v[i])+el,i-1])

			if(i+2<n):
				xtemp=x[i+2]+v[i+2]*(el-last[i+2])
				if(rev[i+1]==None and v[i+2]-v[i+1]<0):
					heap.enqueue([(xtemp-x[i+1])/(v[i+1]-v[i+2])+el,i+1])
				elif(rev[i+1]!=None and v[i+2]-v[i+1]<0):
					#print((xtemp-x[i+1])/(v[i+1]-v[i+2])+el)
					heap.replace(rev[i+1],[(xtemp-x[i+1])/(v[i+1]-v[i+2])+el,i+1])


	return ans



