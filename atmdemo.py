#atmdemo.py
from atmoperations import deposit,withdraw,balenq
from atmexcept import DepositError,InSufficientFundError,WithdrawError
from atmmenu import menu
import sys
def runatm():
	while True:
		menu()
		try:
			ch=int(input("enter your choice:"))
			if ch==1:
				try:
					deposit()
				except ValueError:
					print("Dont try to deposit alpha-nums /strs/ symbols")
				except DepositError:
					print("Dont try to deposit negative or zero values")
				except:
					print("Something went wrong")
			elif ch==2:
				try:
					withdraw()
				except ValueError:
					print("Dont try to withdraw alpha-nums /strs/ symbols")
				except WithdrawError:
					print("Dont try to withdraw negative or zero values")
				except InSufficientFundError:
					print("Ur account does not have sufficient balance to withdraw")
				except:
					print("Something went wrong")
			elif ch==3:
				balenq()
			elif ch==4:
				sys.exit()
			else:
				print("CHoose appropriate option:")
		except ValueError:
			print("dont enter strs/alphanumerics/symbols for choice")

