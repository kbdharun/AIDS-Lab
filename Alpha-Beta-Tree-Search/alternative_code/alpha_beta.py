from collections import defaultdict
import math


class Heap:

    def __init__(self):
        self.edges = defaultdict(list)
        self.alpha_beta_values = {}

    def addEdge(self, u, v):
        self.edges[u].append(v)

    def terminal(self, node):
        if node in self.edges:
            return False
        return True

    def evaluate(self, node):
        return int(node)

    def abprune(self, node, alpha, beta, MAX):
        if self.terminal(node):
            return self.evaluate(node)

        if MAX:
            max_temp = -math.inf
            for child in self.edges[node]:
                temp = self.abprune(child, alpha, beta, False)
                max_temp = max(temp, max_temp)
                alpha = max(alpha, max_temp)
                if beta <= alpha:
                    print('Pruned :', node, '-->', child)
                    break
            self.alpha_beta_values[node] = (alpha, beta)
            return max_temp

        else:
            min_temp = math.inf
            for child in self.edges[node]:
                temp = self.abprune(child, alpha, beta, True)
                min_temp = min(temp, min_temp)
                beta = min(beta, min_temp)
                if beta <= alpha:
                    print('Pruned :', node, '-->', child)
                    break
            self.alpha_beta_values[node] = (alpha, beta)
            return min_temp

    def get_alpha_beta_values(self):
        return self.alpha_beta_values


g = Heap()

for _ in range(int(input())):
    u, v = input().split()
    g.addEdge(u, v)

print('\n\nAlpha value to start :', g.abprune('a', -math.inf, math.inf, True))

alpha_beta_values = g.get_alpha_beta_values()
for i in alpha_beta_values:
    print(i, alpha_beta_values[i])

"""
30
a b
a c
b d
b e
c f
c g
d h
d i
e j
e k
f l
f m
g n
g o
h 10
h 5
i 7
i 11
j 12
j 8
k 9
k 8
l 5
l 12
m 11
m 12
n 9
n 8
o 7
o 10

6
a b
a c
b 5
b 6
c 7
c 4
"""

{a: [b, c], b: [5, 6], c: [7, 4]}
