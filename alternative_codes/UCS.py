#ucs
graph={
    'A':[('S',1),('G',10)],
    'B':[('S',5),('G',5)],
    'C':[('S',15),('G',5)],
    'G':[('A',10),('G',5),('C',5)],
    'S':[('A',1),('B',5),('C',15)]
}
initial=input("Enter the initial state: ")
goal=input("Enter the goal state:  ")
def ucs(initial,goal):
    frontier=[]
    explored=[]
    frontier.append([0,initial])
    while frontier:
        frontier.sort()
        node=frontier.pop(0)
        explored.append(node[-1])
        if node[-1]==goal:
            return node
        for state,weight in graph[node[-1]]:
            if state not in frontier and state not in explored:
                frontier.append([node[0]+weight,]+node[1:]+[state])
            elif state in frontier:
                if(node[0]+weight)<node[0]:
                    i=frontier.index('node')
                    frontier[i]=frontier.append([node[0]+weight]+node[1:]+[state])
ans=ucs(initial,goal)
node=ans[1:]
print("The optimal path is: ",node)
print(ans[0])