from atmdemo import runatm 
import sys
import getpass
c=0
while True:
	passwd=getpass.getpass(prompt="Enter Ur Passord to access ATM Operations:")
	if passwd=="atmapp":
		runatm()
	else:
		print("Invalid Password try again")
		c=c+1
		if c==3:
			print("Ur not allowed to enter ur password and ur un-athorized:")
			print("Card blocked")
			sys.exit()
