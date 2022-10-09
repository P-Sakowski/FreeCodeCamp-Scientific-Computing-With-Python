class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = []

  def __str__(self):
    stars = int((30 - len(self.name)) / 2) * "*"
    result = stars + self.name + stars
    for item in self.ledger:
      result += "\n" + f'{item["description"][:23]: <23}'
      result += f'{item["amount"]:>7.2f}'
    result += "\n" + "Total: " + str(self.get_balance())
    return result

  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description = ""):
    totalAmount = 0
    if(self.check_funds(amount) == True):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def get_balance(self):
    totalAmount = 0
    for record in self.ledger:
      totalAmount += float(record["amount"])
    return totalAmount

  def transfer(self, amount, Category):
    if(self.check_funds(amount) == True):
      self.withdraw(amount, "Transfer to " + Category.name)
      Category.deposit(amount, "Transfer from " + self.name)
      return True
    else:
      return False

  def check_funds(self, amount):
    totalAmount = 0
    for record in self.ledger:
      totalAmount += float(record["amount"])
    if(totalAmount >= amount):
      return True
    else:
      return False

def create_spend_chart(categories):
  chartData = []
  totalAmount = 0
  for category in categories:
    for item in category.ledger:
      if(float(item["amount"] < 0)):
        amount = float(item["amount"])
        chartData.append({"name": category.name, "value": amount})
        totalAmount += amount
  steps = []
  steps.extend(range(0,101,10))
  steps.reverse()

  #print lines of chart
  result = "Percentage spent by category\n"
  for step in steps:
    result += f'{step:>3}|'
    for column in chartData:
      if((float(column["value"]) / totalAmount * 100) >= step):
        result += " o "
      else:
        result += "   "
    result += " \n"

  #print bottom border of chart
  result += (4 * " ") + ((3 * len(chartData) + 1) * "-") + "\n"

  #print column names
  names = []
  i = 0
  maxLength = 0
  for column in chartData:
    names.append(column["name"])
    if(len(column["name"]) > maxLength):
      maxLength = len(column["name"])
  while(i < maxLength):
    result += (4 * " ")
    for name in names:
      if(len(name) > i):
        result += f' {name[i]} '
      else:
        result += '   '
    result += " "
    i += 1
    #don't add \n char in last row
    if(i < maxLength):
      result += "\n"
      
  return result