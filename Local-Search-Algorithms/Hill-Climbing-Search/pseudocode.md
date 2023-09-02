```txt
function HILL-CLIMBING(problem) returns a state that is a local maximum
	current <- problem.INITIAL
	while true do
		neighbour <- a highest-valued successor state of current
		if VALUE(neighbour) =< VALUE(current) then return current
		current <- neighbor

Write a Python program for the above algorithm.

To get graph as input with heuristic value for each state. then take initial state, goal state. If node is not reached, then return failure.
```
