print("Welcome to the tip calculator!")
bill = input("What was the total bill?\n")

tipping_option = input("Choose your tipping option: type 1 to pay a percentage of the bill as a tip, type 2 to choose how much to tip\n")
if tipping_option == str(1):
  tip = input("How much of a tip percentage would you like to give? (if percentage is less than 10% put a 0 before the number)\n")
  tip_2 = str(1) + "." + tip

if tipping_option == str(2):
  tip_20 = input("How many dollars would you like to tip?")
  print(tip_20)

People = input("How many people are splitting the bill?\n")

if tipping_option == str(1):
  total_bill = (float(bill) / int(People)) * float(tip_2)
  how_much_each = round(total_bill, 2)
if tipping_option == str(2):
  total_bill_ver_2 = (float(bill) + float(tip_20)) / int(People)
  how_much_each_ver_2 = round(total_bill_ver_2, 2)

if tipping_option == str(1):
  print("Each person will pay" + " " + "$" + str(how_much_each) + ".")
if tipping_option == str(2):
  print("Each person will pay" + " " + "$" + str(how_much_each_ver_2) + ".")
