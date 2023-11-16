
H={'a':12,'b':4,'c':7,'d':3,'e':8,'f':2,'g':0,'h':4,'i':9,'s':13}
graph={
    's':[(3,'a'),(2,'b')],
    'a':[(4,'c'),(1,'d')],
    'b':[(3,'e'),(1,'f')],
    'c':[],
    'd':[],
    'e':[(5,'h')],
    'f':[(2,'i'),(3,'g')],
    'g':[],
    'h':[],
    'i':[]
}
initial=input("Enter the initial state: ")
goal=input("Enter the goal state: ")

def gbfs(initial,H,goal):
    frontier=[]
    explored=[]
    frontier.append(initial)
    while frontier:
        node=frontier.pop(0)
        explored.append(node)
        if node==goal:
            return explored
        adj=graph[node]
        for child in adj:
            if child not in frontier and child not in explored:
                frontier.append(child)
                frontier.sort(key=lambda child:H[child])
ans=gbfs(initial,H,goal)
print("The optimal path is: ",ans)