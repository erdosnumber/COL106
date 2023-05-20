
#import time
#We will solve the problem using segment trees where each node having left endpoint l and right endpoint r contains the pairs
#  of the form (y,x) sorted in increasing order where (x,y)  is a co-ordinate occuring in the range [l,r] and the segment tree is made
#  after sorting the co-ordinates as pairs

Answer=[]

class PointDatabase:

    def __init__(self,pointlist):

        self.l=[]
        for i in range(len(pointlist)):
            self.l.append(pointlist[i])

        self.l.sort()
        pw=int(1)
        n=len(self.l)
        while(pw<n):
            pw*=2

        pw2=2*pw-1
        self.pow=pw
        self.st=[None]*pw2

        
        if(len(self.l)!=0):
            self.mx=self.l[n-1][0]
            self.my=self.l[n-1][1]
            for i in range(len(self.l)):
                if(self.l[i][1]>self.my):
                    self.my=self.l[i][1]
            for i in range(n,pw):
                self.l.append((self.mx+1,self.my+1))
            self.buildseg(0,self.pow-1,0)

 #Building segtree in nlogn       
    def buildseg(self,left,right,node):

        if(left==right):
            #note here we are putting (y,x) and not (x,y)
            self.st[node]=[]
            self.st[node].append((self.l[left][1],self.l[left][0]))
            #print(self.st[node])
        else:
            mid=(left+right)//2
            self.buildseg(left,mid,2*node+1)
            self.buildseg(mid+1,right,2*node+2)
            #now perform the merging of self.st[2*node+1] and self.st[2*node+2]
            ind1=int(0)
            ind2=int(0)

            self.st[node]=[]
            # print(len(self.st[node]))


            while(ind1<len(self.st[2*node+1]) and ind2<len(self.st[2*node+2])):

                if(self.st[2*node+1][ind1][0]<self.st[2*node+2][ind2][0]):
                    self.st[node].append(self.st[2*node+1][ind1])
                    ind1+=1
                else:
                    self.st[node].append(self.st[2*node+2][ind2])
                    ind2+=1

                if(ind1==len(self.st[2*node+1])):
                    while(ind2<len(self.st[2*node+2])):
                        self.st[node].append(self.st[2*node+2][ind2])
                        ind2+=1
                elif(ind2==len(self.st[2*node+2])):
                    while(ind1<len(self.st[2*node+1])):
                        self.st[node].append(self.st[2*node+1][ind1])
                        ind1+=1

            #print(self.st[node])

    def useseg(self,x,y,d,left,right,node):
            #I have used the fact that using a segment tree to find a property of the subarray[l,r] has logn complexity
        if(self.l[left][0]>=x-d and self.l[right][0]<=x+d):
            #find the upper bound of y-d in self.st[node] and the upper bound of y+d in self.st[node] by binary search
            #giving complexity of logn
            # print(self.l[left][0])
            # print(self.l[right][0])
            # print(self.st[node])
            lower=int(0)
            upper=len(self.st[node])-1
            if(self.st[node][upper][0]<y-d):
                return
            #So there exists at least one index i such that self.st[node][i][0]>=y-d 0<=i<len(self.st[node])
            while(lower<upper):
                mid=(lower+upper)//2
                if(self.st[node][mid][0]<y-d):
                    lower=mid+1
                else:
                    upper=mid
            index1=lower
            lower=int(0) 
            upper=len(self.st[node])-1
            if(self.st[node][lower][0]>y+d):
                return
            while(lower<upper):
                mid=(lower+upper)//2
                if(self.st[node][mid+1][0]<=y+d):
                    lower=mid+1
                else:
                    upper=mid
            index2=lower

            # print(index1)
            # print(index2)
            # print(self.mx)
            # print(self.my)
            if(index1<=index2 and index1>=0 and index2>=0):
                for i in range(index1,index2+1):
                    if(self.st[node][i][0]!= self.my+1 and self.st[node][i][1]!= self.mx+1):
                        Answer.append((self.st[node][i][1],self.st[node][i][0]))

        elif(left==right):
            return
        else:

            mid=(left+right)//2
            if(self.l[mid+1][0]>x+d):
                self.useseg(x,y,d,left,mid,2*node+1)
            elif(self.l[mid][0]<x-d):
                self.useseg(x,y,d,mid+1,right,2*node+2)
            else:
                self.useseg(x,y,d,left,mid,2*node+1)
                self.useseg(x,y,d,mid+1,right,2*node+2)


    def searchNearby(self, q, d):
        Answer.clear()
        if(len(self.l)==0):
            return Answer
        self.useseg(q[0],q[1],d,int(0),self.pow-1,int(0))
        return Answer

    def print_l(self):
        print(self.l)

    def print_st(self):
        print(self.st)

    def prints(self):
        print(len(self.st))
                
# l=[]
# for i in range(1000):
#     l.append((i,i+1))

# s=time.time()
# pointDbObject = PointDatabase(l)
# t=pointDbObject.searchNearby((5,16),100)
# print(t)
# e=time.time()
# print(e-s)

# pointDbObject = PointDatabase([(-8,2),(-7,2),(-6,5),(1,0),(1,1),(0,-1),(0,5),(-6,-1),(0,4),(0,1),(-1,1),(-3,0),(-4,3),(-3,4),(-2,4)])
# t=pointDbObject.searchNearby((-3,2),10)
# print(t)

# pointDbObject = PointDatabase([(1,6), (2,4), (3,7), (4,9), (5,1), (6,3), (7,8), (8,10),(9,2), (10,5)])
# print(pointDbObject.searchNearby((5,5),1))
# print(pointDbObject.searchNearby((4,8),2))
# print(pointDbObject.searchNearby((10,2),1.5))