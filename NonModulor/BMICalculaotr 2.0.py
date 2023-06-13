
# BMI Calculator 2.0

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

BMI = round(weight / height ** 2)

print(f"Your BMI is {BMI}")

if BMI < 18.5:
    print("You're underweight.")
elif BMI < 25:
    print("You have a normal weight.")
elif BMI < 30:
    print("You are overweight.")
elif BMI < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")