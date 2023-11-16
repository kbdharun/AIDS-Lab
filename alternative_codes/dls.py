#DLS
graph = {
    'a': ['b','c'],
    'b': ['d','e'],
    'c': ['f','g'],
    'd': [],
    'e': ['h','i'],
    'f': [],
    'g': [],
    'h': [],
    'i': []}

initial=input("Enter the initial state: ")
goal=input("Enter the goal state: ")
depth_limit=int(input("Enter the depth limit: "))

def dls(current_state,goal_state,depth_limit):
    explored=[]
    if current_state not in explored and depth_limit>=0:
        if current_state == goal_state:
            print(current_state)
            return True
        else:
            print(current_state)
        explored.append(current_state)
    
    adj=graph[current_state]
    if depth_limit>0:
        goal=False
        for child in adj:
            if dls(child,goal_state,depth_limit-1):
                goal=True
                break
        return goal
    return False

def depth_limited_search(initial,goal,depth_limit):
    if not dls(initial,goal,depth_limit):
        print("Goal state not reached")
    if dls(initial,goal,depth_limit):
        print("Goal state reached")

depth_limited_search(initial,goal,depth_limit)