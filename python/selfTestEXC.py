#takes inputs from user

salary = input("Enter your salary: ")
yos = input ("ENter year of service: ")

#converts inputs into int using int function

salary=int(salary)
yos=int(yos)

#outpting the salary to the user
if yos > 5:
    print("Net bonus is: ", salary+(salary*0.05))
else:
    print("Salary is: ", salary)