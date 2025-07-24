car_name="Mahindra BE 6"
car_price=1987380
down_payment=300000
loan_amount=car_price-down_payment
interest_rate=9.5
years=5
total_loan_months=years*12
month_intrest=interest_rate/(12*100)

P=loan_amount
R=month_intrest
N=total_loan_months

EMI=P*R*(1+R)**N/((1+R)**N-1)
print("Car_Name : ",car_name)
print("Car_Price :",car_price)
print("Down_payment : ",down_payment)
print("loan_amount : ",loan_amount)
print("interest_rate : ",interest_rate)
print("NO.Of_Years : ",years)
print("Calculated EMI is : ", round(EMI,2))

