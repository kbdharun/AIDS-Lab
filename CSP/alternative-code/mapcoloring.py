
def is_valid_color(ans):
    p1,p2,p3,p4=ans
    if p1 == p2 or p1 == p3 or p2 == p3 or p2 == p4 or p3 == p4:
        return False
    return True

def backtracking(ans):

    if len(ans) == 4:
        
        if is_valid_color(ans):
            return ans
        return None

    for color in a:
        result=backtracking(ans+[color])
        if result:
            return result
    return None

a = ['Green', 'red', 'blue']
csp_ans = backtracking([])
if csp_ans:
    p1, p2, p3, p4 = csp_ans
    print("color of p1: ",p1)
    print("color of p2: ",p2)
    print("color of p3: ",p3)
    print("color of p4: ",p4)
else:
    print("No solution found")