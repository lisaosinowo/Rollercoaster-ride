# This program determines the price of one rollercoaster ride, depending if the person meets the height requirement.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# This is a nested if/else clause. If the first option is above 120 cm then the next question will be asked (between lines 7 and 16). If the first option is below 120cm then no more questions are asked (line 17).
if height >= 120:
  print("You can ride this rollercoaster!")

  age = int(input("What is your age? "))
  if age < 12:
    print("Child tickets are £5.")
  elif age <= 18:
    print("Youth tickets are £7.")
  elif age >= 45 and age <= 55:
    print("You can ride for free!")
  else:
    print("Adult tickets are £12.")
else:
  print("You cannot ride this rollercoaster.")
