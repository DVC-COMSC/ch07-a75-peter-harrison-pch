
import sys

num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

if len(num1) > len(num2):
	print ('False')
	sys.exit(0)
# ******************************
# Make your Code
# ******************************

for i in range(len(num2)-len(num1) + 1):
	if num1 == num2[i:(i+len(num1))]:
		print("subset")
		break
	else: print("not")

"""
startin = 0
slack = len(num2) - len(num1) + 1
kill = False

for num in num2:
	if num not in num1[startin:slack]:
		kill = True
		break
	beginindex += 1
	lastindex += 1 
"""

# print ('True') or ('False')
