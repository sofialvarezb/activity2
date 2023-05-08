exercises=int(input("Enter the number of the exercise you want to run: "))

if exercises==17:
  #A number is positive or negative
  number = float(input("Enter a number: "))
  if (number > 0): 
    print("The number" + str(number) + " Is positive")
  else:
    print("The number " + str(number) + " Is positive")

elif exercises==18:
  #The greatest and least number
  number1 = float(input("Enter a number: "))
  number2 = float(input("Enter another number: "))
  if (number1>number2):
    print("The number", number1, "Is the eldest: ")
  elif (number2>number1):
    print("The number", number1, "Is the eldest:")

elif exercises==19:
  #The largest number and the smallest among three numbers
  number1 = float(input("Enter a number: "))
  number2 = float(input("Enter another number: "))
  number3 = float(input("Enter another number: "))
  if (number1 > number2 > number3):
    print("The number", number1, "It is the largest and the number ", number3, "It is the smallest t")
  elif (number1 > number3 > number2):
    print("The number", number1, "It is the largest and the number ", number2, "It is the smallest ")
  elif (number2 > number1 > number3):
    print("The number", number2, "It is the largest and the number", number3, "It is the smallest ")
  elif (number3 > number1 > number2):
    print("The number", number3, "It is the largest and the number ", number2, "It is the smallest ")
  elif (number2 > number3 > number1):
    print("The number", number2, "It is the largest and the number ", number1, "It is the smallest ")
  else:
    print("The number", number3, "It is the largest and the number ", number1, "It is the smallest ")

elif exercises==20:
  #Employee salary
  name = input("Please enter your name: ")
  hours = float(input("Please Enter normal hours worked: "))
  additional = float(input("Please enter the number of overtime hours worked: "))
  if (additional==0):
    print(name, "his salary is", hours*4)
  elif (additional >0):
    print(name, "his salary is",(hours*4)+(additional*8))

elif exercises==21:
  #Addition or subtraction of two numbers
  number1 = float(input("Please enter a  (A): "))
  number2 = float(input("Please enter another number (B): "))
  if (number1 > number2):
    print("The subtraction of the numbers is: ", number1-number2)
  elif (number2 > number1):
    print("The addition of the numbers is: ", number1+number2)

elif exercises==22:
  #Quotient of two numbers
  number1 = float(input("Please enter a number (A): "))
  number2 = float(input("Please enter another number (B): "))
  if (number2 > 0):
    print("The quotient between these two numbers is:", number1/number2)
  elif (number2 == 0):
    print("The division is not valid since whatever value our answer is, we will have to admit that this value multiplied by 0 is equal to 1, and that cannot be true, because anything multiplied by 0 is 0.")
elif exercises ==23:
  #Day of the week
  numberD = int(input("Enter the number of the day of the week (1-7): "))
  if numberD == 1:
    print("Monday")
  elif numberD == 2:
    print("Tuesday")
  elif numberD == 3:
    print("Wednesday")
  elif numberD == 4:
    print("Thursday")
  elif numberD == 5:
    print("Friday")
  elif numberD == 6:
    print("Saturday")
  elif numberD == 7:
    print("Sunday")
  
elif exercises==24:
  #Equilateral triangle
  number1 = float(input("Please enter the measurement of the first length: "))
  number2 = float(input("Please enter the measurement of the second length: "))
  number3 = float(input("Please enter the measurement of the third length: "))
  if number1 == number2 and number1 == number3:
    print("The triangle is equilateral ")
  elif (number1 != number2 or number1 != number3 or number2 != number3):
    print("The triangle is not equilateral ")

elif exercises==25:
  #Addition or multiplication of two numbers
  number1 = float(input("Please enter a number (A): "))
  number2 = float(input("Please enter another number (B): "))
  if (number1 <0 or number2 <0):
    addition = number1 + number2
    print ("The addition of the two numbers is: ",addition)
  elif (number1 >0 or number2 >0):
    multiplication= number1 * number2
    print ("The multiplication of the two numbers is: ",multiplication)

elif exercises==26:
  #Zodiac signs
  day= int(input("enter your day of birth: "))
  month = int(input("enter the number of the month of your birth: "))
  if (month == 1 and day >= 20) or (month == 2 and day <= 18):
    print("Acuario")
  elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    print("Piscis")
  elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
    print("Aries")
  elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    print("Tauro")
  elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
    print("Geminis")
  elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
    print("Cancer")
  elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    print("Leo")
  elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    print("Virgo")
  elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
    print("Libra")
  elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
    print("Escorpio")
  elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    print("Sagitario")
  elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
    print("Capricornio")

elif exercises==27:
  #Area and perimeter of a quadrilateral
  base = float(input("Please enter the base of the quadrilateral: "))
  height = float(input("Please enter the height of the quadrilateral: "))
  #Squaare
  if (base == height):
    perimeter = base*4
    area = base*height
    print("This figure is a square, its perimeter is ",perimeter, "and its area is ",area)
  #Rectangle
  elif (base != height):
    perimeter1 = (base*2)+(height*2)
    area1 = (base*height)
    print("This figure is a rectangle, its perimeter is ",perimeter1, "and its area is",area1)
    
elif exercises==28:
  #Discounts
    sale = float(input("Please enter the sale price: "))
  #Discount 5%
    if (sale < 100.0):
      discount = sale*5/100
      price = sale - discount
      print("Your discount is 5% which is equivalent to ",discount, "and your purchase remains in ",price)
    #Discount 10%
    elif (sale>100 or sale==100) and (sale<200):
      discount1  = sale*10/100
      price1 = sale - discount1
      print("Your discount is 10% which is equivalent to ",discount1, "and your purchase remains in ",price1)
    elif (sale > 200 or sale == 200):
      discounT = sale*15/100
      pricE = sale - discounT
      print("Your discount is 15% which is equivalent to ",discounT, "and your purchase remains in ",pricE)

elif exercises == 29:
  #Know if a year is a leap year
  year = int(input("Please enter the year: "))
  if not year % 4 and (year % 100 or not year % 400):
    print("The year is leap")
  else:
    print("The year is not a leap year")