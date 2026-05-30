rent=int(input("Enter rent of the hostel:"))
food=int(input("Enter food amount:"))
electricity=int(input("Enter electricity spend:"))
charge_per_unit=int(input("Enter charge per unit for electricity:"))
persons=int(input("Enter total persons in room:"))

electricity_bill=electricity*charge_per_unit
total_pay_per=(rent+food+electricity_bill)//persons  #isse fix amount me value ati hai

print("Total amount you've to pay is:",total_pay_per)



