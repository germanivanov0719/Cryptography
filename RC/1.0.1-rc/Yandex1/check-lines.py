#! python3

# How to use:
# ./check-lines.py main.py connections.py methods/compare_methods.py methods/databases_methods.py \
# methods/fernet_methods.py \
# methods/md5_methods.py methods/sha_methods.py resources/show_keys_dialogue.py \
# resources/dynamic_translations.py resources/translation.py

import sys

r = 0
if len(sys.argv) == 1:
    print("Filenames not detected.")
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
