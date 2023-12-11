import random

class CSP():

    def __init__(self, variables, domains, neighbors, constraints):
        self.variables = variables if variables else list(domains.keys())
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints
        self.curr_domains = None
        self.nassigns = 0

    def assign(self, var, val, assignment):
        assignment[var] = val
        self.nassigns += 1

    def unassign(self, var, assignment):
        if var in assignment:
            del assignment[var]

    def nconflicts(self, var, val, assignment):
        def conflict(var2):
            return var2 in assignment and not self.constraints(var, val, var2, assignment[var2])

        return sum(conflict(v) for v in self.neighbors[var])

    def display(self, assignment):
        print(assignment)

    def actions(self, state):
        if len(state) == len(self.variables):
            return []
        else:
            assignment = dict(state)
            var = next((v for v in self.variables if v not in assignment), None)
            return [(var, val) for val in self.domains[var]
                    if self.nconflicts(var, val, assignment) == 0]

    def result(self, state, action):
        (var, val) = action
        return state + ((var, val),)

    def goal_test(self, state):
        assignment = dict(state)
        return (len(assignment) == len(self.variables)
                and all(self.nconflicts(variables, assignment[variables], assignment) == 0
                        for variables in self.variables))

    def support_pruning(self):
        if self.curr_domains is None:
            self.curr_domains = {v: list(self.domains[v]) for v in self.variables}

    def suppose(self, var, value):
        self.support_pruning()
        removals = [(var, a) for a in self.curr_domains[var] if a != value]
        self.curr_domains[var] = [value]
        return removals

    def prune(self, var, value, removals):
        self.curr_domains[var].remove(value)
        if removals is not None:
            removals.append((var, value))

    def choices(self, var):
        return (self.curr_domains or self.domains)[var]

    def infer_assignment(self):
        self.support_pruning()
        return {v: self.curr_domains[v][0]
                for v in self.variables if len(self.curr_domains[v]) == 1}

    def restore(self, removals):
        for B, b in removals:
            self.curr_domains[B].append(b)

    def conflicted_vars(self, current):
        return [var for var in self.variables
                if self.nconflicts(var, current[var], current) > 0]
    


# Functions on Sequences and Iterables
def count(seq):
    return sum(map(bool, seq))

def first(iterable, default=None):
    return next(iter(iterable), default)

def extend(s, var, val):
    try:  
        return eval('{**s, var: val}')
    except SyntaxError:  
        s2 = s.copy()
        s2[var] = val
        return s2

# argmin and argmax
identity = lambda x: x

def argmin_random_tie(seq, key=identity):
    return min(shuffled(seq), key=key)

def argmax_random_tie(seq, key=identity):
    return max(shuffled(seq), key=key)

def shuffled(iterable):
    items = list(iterable)
    random.shuffle(items)
    return items


# CSP Backtracking Search

# Variable ordering
def first_unassigned_variable(assignment, csp):
    return first([var for var in csp.variables if var not in assignment])

def mrv(assignment, csp):
    return argmin_random_tie([v for v in csp.variables if v not in assignment],
                             key=lambda var: num_legal_values(csp, var, assignment))

def num_legal_values(csp, var, assignment):
    if csp.curr_domains:
        return len(csp.curr_domains[var])
    else:
        return count(csp.nconflicts(var, val, assignment) == 0 for val in csp.domains[var])

# Value ordering
def unordered_domain_values(var, assignment, csp):
    return csp.choices(var)

def lcv(var, assignment, csp):
    return sorted(csp.choices(var), key=lambda val: csp.nconflicts(var, val, assignment))

# Inference
def no_inference(csp, var, value, assignment, removals):
    return True

def forward_checking(csp, var, value, assignment, removals):
    csp.support_pruning()
    for B in csp.neighbors[var]:
        if B not in assignment:
            for b in csp.curr_domains[B][:]:
                if not csp.constraints(var, value, B, b):
                    csp.prune(B, b, removals)
            if not csp.curr_domains[B]:
                return False
    return True

def AC3(csp, var, value, assignment, removals):
    def revise(csp, Xi, Xj):
        revised = False
        for x in csp.curr_domains[Xi][:]:
            if not any(csp.constraints(Xi, x, Xj, y) for y in csp.curr_domains[Xj]):
                csp.prune(Xi, x, removals)
                revised = True
        return revised

    queue = [(Xk, var) for Xk in csp.neighbors[var]]
    while queue:
        (Xi, Xj) = queue.pop(0)
        if revise(csp, Xi, Xj):
            if not csp.curr_domains[Xi]:
                return False
            for Xk in csp.neighbors[Xi]:
                if Xk != Xj:
                    queue.append((Xk, Xi))
    return True

# The search, proper
def backtracking_search(csp, select_unassigned_variable=first_unassigned_variable,
                        order_domain_values=unordered_domain_values, inference=no_inference):

    def backtrack(assignment):
        if len(assignment) == len(csp.variables):
            return assignment
        var = select_unassigned_variable(assignment, csp)
        for value in order_domain_values(var, assignment, csp):
            if 0 == csp.nconflicts(var, value, assignment):
                csp.assign(var, value, assignment)
                removals = csp.suppose(var, value)
                if inference(csp, var, value, assignment, removals):
                    result = backtrack(assignment)
                    if result is not None:
                        return result
                csp.restore(removals)
        csp.unassign(var, assignment)
        return None

    result = backtrack({})
    assert result is None or csp.goal_test(result)
    return result