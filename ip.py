import sys

args=sys.argv[1]
print(args)

count=0
with open("ip.txt") as f:
	for line in f:
		if (line.split("\n")[0]==sys.argv[1]):
			count=count+1
	if count==0:
		print("ip not present")
	else:
		print("ip present")
sys.exit()