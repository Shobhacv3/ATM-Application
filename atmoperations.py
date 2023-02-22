#atmoperations.py
from atmexcept import DepositError,InSufficientFundError,WithdrawError
bal=500.00 #global variable
def deposit():
	damt=float(input("enter ur deposit amout:"))#here pvm raises valueError in case of non-nummerics
	if damt<=0:
		raise DepositError
	else:
		global bal
		bal=bal+damt
		print("\n Ur account  xxxxx123 credited with INR {}".format(damt))
		print("Ur Current Account Balance after deposit INR:{}:".format(bal))

def withdraw():
	wamt=float(input("enter ur withdraw amount:"))#here pvm raises valueError in case of non-nummerics
	global bal
	if wamt<=0:
		raise WithdrawError
	elif (wamt+500)>bal:
		raise InSufficientFundError
	else:
		bal=bal-wamt
		print("\n Ur account  xxxxx123 debited with INR {}".format(wamt))
		print("Ur Current Account Balance after withdraw INR:{}:".format(bal))
		  
def balenq():
	print("Ur Current Account Balance INR:{}".format(bal)) #as we are just accessing global variable so,no need to specify global
