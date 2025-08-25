# command line arguments
import sys

x = sys.argv
if len(x)==4:
    server_name = x[1]
    user_name = x[2]
    password = x[3]
    print(server_name, user_name, password)
else:
    print(f"not sufficient arguments")
