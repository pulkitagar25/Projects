name = input("What is your name: ")

birth_Year = int(input("Enter your birth year: "))

Current_time = 2022

def age_calc():
    Age_calculated = (Current_time - birth_Year)
    print ('Hey {} your age is {}'.format(name, Age_calculated))
age_calc()
