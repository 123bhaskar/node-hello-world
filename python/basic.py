import sys
def square(x):
    return x**2
if len(sys.argv)==2:
    out=square(int(sys.argv[1]))
    print(out)
else:
    print("error")
