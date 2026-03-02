print("======= BMI Calculator =======")

name = str(input("\nEnter your Name: "))
measure = float(input("Enter your measure: "))
height = float(input("Enter your height: "))

(bmi) = height / (measure * measure)

print(f"\nYour BMI is: {bmi:.2f}")

print("\n------- Your Status -------")
if(bmi >= 18.5 and bmi <= 24,9):
    print("Normal Height")
elif (bmi > 24.9 and bmi <= 29.9):
    print("Overweight")
else:
    print("Obese")