from collections import deque

JONES = 1
TIGER = 2
MONKEY = 3
COCKROACH = 4

passengers = {JONES, TIGER, MONKEY, COCKROACH }
invalid = ({TIGER, MONKEY},
           {MONKEY, COCKROACH})

def check(solution):
    left = passengers.copy()
    right = set()

    for p in solution:
        if p in left:
            if JONES not in left:
                return False
            right.add(p)
            left.remove(p)
            if p != JONES:
                right.add(JONES)
                left.remove(JONES)
        else:
            if JONES not in right:
                return False
            left.add(p)
            right.remove(p)
            if p != JONES:
                left.add(JONES)
                right.remove(JONES)
        if left in invalid or right in invalid:
            return False
    if not left:
        return True
    return False

def solve():
    q = deque()
    q.append([])
    while q:
        s = q.popleft()
        if check(s):
            return s
        for p in passengers:
            n = s.copy()
            n.append(p)
            q.append(n)

solution = solve()
print(' '.join({1: 'Jones', 2: 'J+Tiger', 3: 'J+Monkey', 4: 'J+Cockroach'}[p] for p in solution))
