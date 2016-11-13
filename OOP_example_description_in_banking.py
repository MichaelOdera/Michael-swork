#We first create a class that acts as a blueprint for the children classes that will be associated with the class BankAccount
class BankAccount(object):
	def init(self, balance):
	# This is a construct created to and this is never visible to the user of the program. It is a property of Abstraction.
		self.balance = balance
		
	def deposit(self, amount):
		self.balance += amount
		return self.balance
	
	def withdraw(self, amount):
		self.balance -= amount
		return self.balance

#This class inherits from the above parent class BankAccount		
class SavingsAccount(BankAccount):
	# this is a demonstration of abstraction, since this construct sees to it that the viewer will not see what is at this point
	# It also acts as an encapsulation agent
	 def init(self, balance = 500):

	 	self.balance = balance
	 
	 #This is a method that demonstrates what happens on depositing and the conditions necessary during withdrawal
	 def deposit(self, amount):
	 	if amount >= 0:
	 		return BankAccount.deposit(self, amount)
	 	elif amount < 0:
	 		return "Invalid deposit amount"
	 	else:
	 		pass
	 	
	 def withdraw(self, amount):
	 	if self.balance - amount < 500:
	 		return "Cannot withdraw beyond the minimum account balance"
	 	elif amount > self.balance:
	 	  return "Cannot withdraw beyond the current account balance"
	 	elif amount < 0:
	 		return "Invalid withdraw amount"
	 	else:
	 		return BankAccount.withdraw(self, amount)

# In addition to the subclass above called SavingsAccount, this class is an evidence that the in OOP, it is possible to have polymorphism. The ability of having many subclasses from one blueprint.

class CurrentAccount(BankAccount):
	def init(self, balance = 0):
		self.balance = balance

	def deposit(self, amount):
		 if amount < 0:
			 return "Invalid deposit amount"
		 else:
			 return BankAccount.deposit(self, amount)
			 
	def withdraw(self, amount):
		if amount < 0:
			return "Invalid withdrawal amount."
		elif amount > self.balance:
			return "Cannot withdraw beyond the current account balance"
		else:
			return BankAccount.withdraw(self, amount)