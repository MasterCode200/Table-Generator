print("Table Generator- It can print the table of a number")
table=int(input("Which number's table do you want?  "))
for number in range(1,11):
    result=table*number
    print(table,'x',number,'=',result)

for number in range(10,1,-2):
    print("number")