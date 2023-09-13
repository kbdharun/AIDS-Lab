```txt
function SIMULATED-ANNEALING(problem, schedule) returns a solution state
	current <- problem.INITIAL
	for t= 1 to infinity do
		T <- schedule(t)
		if T=0 then return current
		next <- a randomly selected successor of current
		delta E <- VALUE(current) - VALUE(next)
		if delta E > 0 then current <- next
		else current <- next only with probability e^-△ E/T
```
