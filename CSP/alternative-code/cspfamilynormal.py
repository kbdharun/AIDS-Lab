def is_valid_assignment(assignments):
    a, b, c, d = assignments
    if (a-d)!=1 or d>=a or b==2 or c==1 or (a-c)!=2:
        return False
    return True

def backtrack(assignments):
    if len(assignments) == 4:
        if is_valid_assignment(assignments):
            return assignments
        return None
    
    for i in range(1, 5):
            result = backtrack(assignments + [i])
            if result:
                return result
    return None

solution = backtrack([])
if solution:
    a, b, c, d = solution
    print(f"A lives in house {a}")
    print(f"B lives in house {b}")
    print(f"C lives in house {c}")
    print(f"D lives in house {d}")
else:
    print("No solution found.")
