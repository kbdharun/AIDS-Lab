#DFS
graph={ 'A':['B','C','D'],
        'B':['D'],
        'C':['D','L'],
        'D':['L'],
        'E':['A','B','F'],
        'F':['L'],
        'L':['M'],
        'M':[]
}
initial=input("Enter the initial state: ")
goal=input("Enter the goal state ")

def DFS(initial,goal):
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
                frontier.reverse()
ans=DFS(initial,goal)
print("The Depth first traversal is: ",ans)