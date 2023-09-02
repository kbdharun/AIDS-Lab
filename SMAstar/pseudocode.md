```txt
function SMAstar(root, memory_limit):
    open_list <- empty priority queue
    closed_list <- empty set
    memory_used <- 0

    open_list.insert(root)

    while not open_list.isEmpty() do
        current <- open_list.pop()
        if current is a goal state then
            return current

        if memory_used exceeds memory_limit then
            prune open_list to reduce memory usage

        closed_list.add(current)

        for each successor in current.successors() do
            if successor not in closed_list then
                successor.g <- current.g + cost(current, successor)
                successor.h <- heuristic(successor, goal)
                successor.f <- successor.g + successor.h

                if successor not in open_list or successor.f < open_list.get_priority(successor) then
                    open_list.insert_or_update(successor, successor.f)
                    
    return "No solution found"

function prune(open_list):
    while memory_used exceeds memory_limit do
        node <- open_list.get_lowest_priority()
        open_list.remove(node)
        memory_used <- memory_used - size(node)
```
