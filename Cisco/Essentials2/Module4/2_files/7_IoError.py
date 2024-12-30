import errno#to diagnose the problem
try:
    s = open("randomfile", "r")
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")#The file doesn't exist.
    else:
        print("The error number is:", exc.errno)