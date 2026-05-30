
income=int(input("Enter your income:"))
    
expenses={}
total_kharch=0

while True:
    name=input("Enter your item name:")
    if name=="done":
        break
    amount=int(input("Enter amount:"))
    
    expenses[name]=amount
    expenses.update({name:amount})



total_kharch=sum(expenses.values()) 
savings=income-total_kharch
        
with open ("file.txt","a") as f:
    f.write("\n----Naya Entry---\n")
    for name,amount in expenses.items():
        f.write(f"{name}:{amount}\n")
    f.write(f"Total Kharcha:{total_kharch}\n")
    f.write(f"Savings:{savings}\n")

if savings<0:
    print("Budget cross hogya!")

print("Total items:",expenses)
print("Total Kharcha:",total_kharch)
print("Savings:",savings)

