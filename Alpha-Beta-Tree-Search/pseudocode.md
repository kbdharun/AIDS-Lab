```md
function Alpha_Beta_Search (state) returns an action
	v=max_value(state,∞,-∞)
	return the action in Action(state) with value

function max_value(state, α, β) returns a utility value
	if Terminal_Test (state) then return utility (state)
	v=-∞
	for each in a actions (state) do
		V<-MAX(v,min_value(Result(s,a),α,β)
		if v ≥ β then return v
		β<-max(a,v)
	return v

function min_value(state, α, β) returns a utility value
	if Terminal_Test (state) then return Utility(state)
	v = +∞
	for each a in Actions (state) then return Utility(state)
		v <- min(v, max_value(Result(s,a),α,β)
		if v ≤ α then return v
		β <- min(β,v)
	return v
```
