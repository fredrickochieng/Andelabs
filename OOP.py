class BankAccount():
  def deposit():
    pass
  
class Savings(BankAccount):
  def __init__(self):
    self.balance = 10000
    
  
  def deposit(self,deposit):
      if deposit >= 0:
        self.balance += deposit
        return self.balance

      else:
        return 'Invalid deposit amount'

  def withdraw(self,amount):
    if type(amount) == int and amount != "":
      if amount > 0:
        if (self.balance-amount) > 0:
          if (self.balance -amount) > 1000:
            self.balance-=amount
            return self.balance
          else:
            return 'Cannot withdraw beyond the minimum account balance'
        else:
          return 'Cannot withdraw beyond the current account balance'
      else:
        return 'Invalid withdraw amount'
    else:
      raise ValueError()
      
class CurrentAccount(BankAccount):
  def __init__(self):
    self.balance = 0
    
  
  def deposit(self,deposit):
    if type(deposit) == int and deposit !="":
      if deposit >= 0:
        self.balance += deposit
        return self.balance

      else:
        return 'Invalid deposit amount'

    else:
      raise ValueError()

  def withdraw(self,amount):
    if type(amount) ==  int and amount != "":
      if amount > 0:
        if (self.balance-amount) > 0:

          self.balance-=amount
          return self.balance

        else:
          return 'Cannot withdraw beyond the current account balance'
      else:
        return 'Invalid withdraw amount'
    else:
        raise ValueError()