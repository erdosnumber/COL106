
import sys

#increasing recursion depth as it testcases might have large value of m, keeping it 10^6
sys.setrecursionlimit(1000000)

##we will be binary searching on the answer where the binary search is performed on the weights of the edges and for a particular edge
#having weight w, we would be seeing if there exists a path having all edges of weight>=w from u to v. If there exists such then answer<=w
#else answer is >w


#write a dfs function

def dfs(adj,visited,cur,weight,path,destination): 
#adj is the adjacency list, visited is a boolean array storing which all nodes are visited, cur is the
#current node, weight is the value of w described above, path is a list that would give us the desirable path from source
#to destination in reverse order.

    visited[cur]=True

    if(cur==destination):
        path.append(cur)
        return

    for i in range(len(adj[cur])):

        nxt=adj[cur][i][0]
        wt=adj[cur][i][1]
        if(visited[nxt]):
            continue
        if(wt>=weight):
            dfs(adj,visited,nxt,weight,path,destination)
            if(len(path)!=0):
                path.append(cur)
                return


#main function
def findMaxCapacity(nodes,routes,source,destination):

    adj=[None]*nodes
    wt_list=[]

    routes.sort() #this is mlogm
    #we are doing this so as to ensure for an edge (u,v) we only store the maximum weight edge from u to v.
    #push another element to routes that is large just for simpler code

    fake_u=routes[len(routes)-1][0]+nodes
    fake_v=routes[len(routes)-1][1]+nodes
    fake_w=routes[len(routes)-1][2]

    routes.append((fake_u,fake_v,fake_w))
    
    for i in range(len(routes)-1):
        u=routes[i][0]
        v=routes[i][1]
        w=routes[i][2]

        next_u=routes[i+1][0]
        next_v=routes[i+1][1]

        if(u==next_u and v==next_v):
            continue

        if(adj[u]==None):
            adj[u]=[(v,w)]
        else:
            adj[u].append((v,w))

        if(adj[v]==None):
            adj[v]=[(u,w)]
        else:
            adj[v].append((u,w))

        wt_list.append(w)


    wt_list.sort() #complexity of this would be mlogm

    # print(adj)
    # print(wt_list)

    #begin binary search

    low=int(0)
    high=len(wt_list)-1

    while(low<high):

        mid=(low+high)//2
        path=[]
        visited=[]
        for i in range(nodes):
            visited.append(False)

        dfs(adj,visited,source,wt_list[mid+1],path,destination)
        if(len(path)!=0):
                low=mid+1
        else:
                high=mid

    #now we have low=high and wt_list[low] is the value of C required, we just call dfs again to print the path

    final_path=[]
    final_visited=[]
    for i in range(nodes):
        final_visited.append(False)

    dfs(adj,final_visited,source,wt_list[low],final_path,destination)

    final_path.reverse()
    tup=(wt_list[low],final_path)
    return tup

    


#check your dfs function


# nodes=12
# adj=[[(2,1)],[(2,1)],[(0,1),(1,1),(3,1)],[(2,1),(4,1),(9,100),(10,1)],[(3,1),(5,1),(6,1)],[(4,1)],[(4,1),(7,1)],[(6,1),(8,1)],[(7,1),(9,100)],[(8,100),(3,100)],[(3,1),(11,1)],[(10,1)]]
# nodes=4
# adj=[[(3,1),(1,1)],[(0,1),(2,1)],[(1,1),(3,3)],[(0,1),(2,3)]]
# visited=[]

# for i in range(nodes):
#     visited.append(False)

# source=0
# destination=2
# weight=2

# dfs(adj,visited,source)

# print(path)

#print(findMaxCapacity(7,[(0,1,2),(0,2,5),(1,3,4), (2,3,4),(3,4,6),(3,5,4),(2,6,1),(6,5,2)],0,5))