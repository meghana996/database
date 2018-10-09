import sys

args=sys.argv[1]
print(args)

count=0
with open("iph.txt") as f:
	for line in f:
		a=line.split(" ")
		if args in a:
			count=count+1
	if count==0:
		print("ip not present")
	else:
		print("ip present")
sys.exit()




