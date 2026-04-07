name = input("Enter Student Name: ")
dob = input("Enter Date of Birth (DD/MM/YYYY): ")
reg_no = input("Enter Registration Number: ")

print("Enter marks for 5 subjects:")
m1 = float(input("Subject 1: "))
m2 = float(input("Subject 2: "))
m3 = float(input("Subject 3: "))
m4 = float(input("Subject 4: "))
m5 = float(input("Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("\n--- Student Details ---")
print("Name:", name)
print("DOB:", dob)
print("Registration Number:", reg_no)
print("Total Marks:", total)
print("Percentage:", percentage, "%")

if percentage >= 90:
    print("Message: Excellent Performance ")
elif percentage >= 75:
    print("Message:  Good ")
elif percentage >= 50:
    print("Message: Good, Keep Improving ")
else:
    print("Message: Needs hardwork")