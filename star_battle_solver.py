from pulp import *
from collections import defaultdict

def solve_star_battle(inx):
    
    linx = inx.split('\n')
    n = int(linx[0])
    L = [(y,ix,iy) for ix,x in enumerate(linx[1:]) for iy,y in enumerate(x)]    
    s = len(linx[1])
    A = [[[] for y in range(s)] for x in range(s)]
    B = [['.' for y in x] for x in linx[1:]]
    
    LP_variables = []
    LP_constraints = []
    constraints = defaultdict(list)

    for x in L:    
        regio,hori,vert = x[0],str(x[1]),str(x[2])
        st = ','.join([regio,hori,vert])
        v = LpVariable(st,cat='Binary')
        LP_variables += v
        A[x[1]][x[2]] = v
        constraints[regio].append(v)
        constraints['h' + hori].append(v)
        constraints['v' + vert].append(v)
    
    # regions, rows, columns
    for x in constraints.values():
        Ae = LpAffineExpression([(y,1) for y in x])
        Lc = LpConstraint(Ae,sense=0,rhs=n)
        LP_constraints.append(Lc)
    
    # none bordering
    for x in range(s-1):
        for y in range(s-1):
            Ae = LpAffineExpression([(A[x][y],1),
                                     (A[x+1][y],1),
                                     (A[x][y+1],1),
                                     (A[x+1][y+1],1)])
            Lc = LpConstraint(Ae,sense=-1,rhs=1)
            LP_constraints.append(Lc)
    
    prob = LpProblem()
    prob += LpAffineExpression([(x,1) for x in LP_variables])
    
    for x in LP_constraints:
        prob += x
    
    prob.solve(GLPK())    

    for v in prob.variables():
        if v.varValue:
            x,y = list(map(int,v.name[2:].split((','))))
            B[x][y] = '*'
    
    return '\n'.join(''.join(y for y in x) for x in B)


test = """1\nAABBCC\nAABCCC\nAABCCC\nDDBBEE\nDDBBEF\nDDBBFF"""
test2 = "2\nAAAABBCCCC\nADAABBBCBB\nADDBBBBBBB\nDDDDBEEEEB\nDDBBBBBBEB\nFFFFGGHHHH\nFIFFGGGHGG\nFIIGGGGGGG\nIIIIGJJJJG\nIIGGGGGGJG"

sol = solve_star_battle(test2)
print(sol)