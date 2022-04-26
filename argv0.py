from sys import argv

if  len(argv) == 2:
    print("Hello,", argv[1])
else:
    print("Hello world")

for s in argv:
    print(s)