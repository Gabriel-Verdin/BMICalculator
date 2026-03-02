print("======= BMI Calculator =======")

name = str(input("\nEnter your Name: "))
height = float(input("Enter your height (m): "))
weight = float(input("Enter your weight (kg): "))

bmi = weight / (height * height)

print(f"\nYour BMI is: {bmi:.2f}")

print("\n------- Your Status -------")
if bmi >= 18.5 and bmi <= 24.9:
    print("Normal Weight")
elif bmi > 24.9 and bmi <= 29.9:
    print("Overweight")
elif bmi > 29.9:
    print("Obese")
else:
    print("Underweight")