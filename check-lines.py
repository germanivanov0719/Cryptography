#! python3
import sys

r = 0
if len(sys.argv) == 1:
    print("Filename is not argument 1.")
    exit(0)


for i in sys.argv:
    try:
        open(i, 'r')
    except Exception:
        print(f"File '{i}' not found.")
        exit(0)

    with open(i, 'r') as f:
        lines = f.read().splitlines()
        for s in lines:
            if s.strip() != "" and s.strip()[0] != '#':
                r += 1
print(r)
