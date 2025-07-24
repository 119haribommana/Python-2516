std_name=str(input("Enter the student name:"))
std_grade=int(input("Enter the grade:"))
tuition_fee=int(input("Enter the tuition fee:"))
discount_per=0

if std_grade>=1 and std_grade<=12:
    print("Valid")
else:
    print("Invalid")
academic_topper = input("Is the student an academic topper? (yes/no): ").strip().lower()
if std_grade>=9 and std_grade<=12:
    if academic_topper=="yes":
        discount_per+=20   
    else:
        discount_per+=10
elif std_grade<=6 and std_grade>=8:
    discount_per+=5  
elif std_grade<6:
    print("No discount")
else:
    print("Invalid")
match std_grade:
    case 10:
        discount_per+=3
    case 12:
        discount_per+=5
    case _:
        pass
discount_amount=(tuition_fee*discount_per)/100
final_fee=tuition_fee-discount_amount

print("Student name:",std_name)
print("Student grade:",std_grade)
print("Academic topper:",academic_topper)
print("Tuition fee:",tuition_fee)
print("Discount:",discount_amount)
print("Final Tuition fee after discount:",final_fee)