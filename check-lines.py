import sys

r = 0
if len(sys.argv) == 1:
    print("Filename is not argument 1.")
    exit(0)
    
try:
    open(sys.argv[1], 'r')
except Exception:
    print(f"File '{sys.argv[1]}' not found.")
    exit(0)

with open(sys.argv[1], 'r') as f:
    lines = f.read().splitlines()
    for s in lines:
        if s.strip() != "" and s.strip()[0] != '#':
            r += 1
print(r)
