#! python3

r = 0
for i in ["main.py", "connections.py", "sha_methods.py", "fernet_methods.py", "md5_methods.py"]:
    r += exec("check_lines.py", i)
