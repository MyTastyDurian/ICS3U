'''
Richard Feng
ICS3U - November 19, 2021
Task: Take user information about payroll and return gross pay, their tax deduction, bi-weekly net pay, 
and united way deductions. User should be able to specify in the beginning how many different employees’ payroll they want to determine and 
if they want to edit the employee's information
'''
# function payroll which will determine/calculate that employee's payroll
def payroll(profile, c):
    employee_payroll = [profile[0]]
    number = []


    # calculate gross_pay, this would apply to both ot and normal as if there is no overtime, it just results in 0 which cancels out the places that aren't needed
    # profile [employee num, hourly rate, hours worked, contribution]
    if(profile[2] >= 80):
        gross_pay = 80 * profile[1] + (profile[2] - 80) * 1.5 * profile[1]
        employee_payroll.append(gross_pay)

    # same calculation, but no overtime
    else:
        gross_pay = profile[2] * profile[1]
        employee_payroll.append(gross_pay)

    # decision making ot detemrine whether or not they would like $20 deducted forom their net pay
    if(c == 0):
        employee_payroll.append(0.00)
    
    else:
        employee_payroll.append(20.00)

    # this calculates the tax deduction, obviously depending on what tax bracket they fall under is a different percent of their gross pay deducted
    if(gross_pay < 616):
        employee_payroll.append(0.00)

    elif(616 <= gross_pay <= 1885):
        employee_payroll.append(0.15 * gross_pay)
    
    elif(1885 <= gross_pay <= 3770):
        employee_payroll.append((gross_pay - 1885) * 0.205 + 282.75)
    
    elif(3770 <= gross_pay <= 5845):
        employee_payroll.append((gross_pay - 3770) * 0.26 + 669.18)

    elif(5845 <= gross_pay <= 8327):
        employee_payroll.append((gross_pay - 5845) * 0.29 + 1208.68)

    else:
        employee_payroll.append(gross_pay * 0.33)

    # employee payroll = [employee num, gross pay, united way, tax, net]
    employee_payroll.append(employee_payroll[1] - employee_payroll[3] - employee_payroll[2])

    # this is the output or in other words formatting the payroll
    print("Employee #:", end = " " * 4)
    print("Gross Pay:", end = " " * 4)
    print("United Way Deductions:", end = " " * 4)
    print("Tax Deductions:", end = " " * 4)
    print("Net Pay:")

    # i had some formatting issues, os I am taking the tax deduction, only the number of digits that are non decimal and taking that into consideration during formatting
    for index in range(len(str(employee_payroll[3]))):
        number.append(str(employee_payroll[3])[index])

        if(number[-1] == "."):
            number.remove(".")
            break


    # output, the way I formatted it was printing the first row first, each one sperated by four spaces
    # the second row of output is directly under the subheading
    print(employee_payroll[0], end = " " * (15 - len(str(employee_payroll[0]))))
    print("${:.2f}".format(employee_payroll[1]), end = " " * (12 - len(str(employee_payroll[1]))))
    print("${:.2f}".format(employee_payroll[2]), end = " " * (24 - len(str(employee_payroll[2]))))
    print("${:.2f}".format(employee_payroll[3]), end = " " * (15 - len(number)))
    print("${:.2f}".format(employee_payroll[4]))

    return

# employee profile which will store the raw data of the employee
# profile = [employee number, employee hourly rate, number of hours worked, united way contribution]
profile = [] 
user_continue = True

# this is how many employee payroll needs to be determined or in the other words how many times to loop the for loop
n = int(input("Enter the number of employees that you want to determine the payroll of:\n"))

# this gets the raw input from the employees n times, each time after getting it, calling the payroll() function and executing it to determine that employees payroll, then moving on to the next one
for i in range(n):
    # raw input
    profile.append(int(input("Enter the Employee Number:\n")))
    profile.append(float(input("Enter the Employee Hourly Rate:\n")))
    profile.append(int(input("Enter the Number of Hours Worked:\n")))
    print("0 for No Contribution")
    print("1 for Yes, Contribute")
    profile.append(int(input("Contribution:\n")))

    # if they want to change somethin
    change_info = input("Would you like to change anything: (y/n)\n")

    # while true (infinite loop)
    while(user_continue):
        # if they want to change something
        if(change_info.lower() == "y"):
            print("Employee Number - 0, Employee Hourly Rate - 1, Number of Hours Worked - 2, United Way Contribution - 3")
            change = int(input("Enter the number corresponding to the category you would like to change:\n"))

            profile[change] = int(input("Enter the correct data:\n"))

        # if they don't want to, exit the loop
        elif(change_info.lower() == "n"):
            break

        # invalid input
        else:
            print("Please enter one of the following: (y/n)")

        change_info = str(input("Would you like to change anything: (y/n)\n"))
        
    # calling function payroll() which will calculate their payroll 
    payroll(profile, profile[3])
    # this will just clear the list because I don't actually need to store the data, but just temporailry store it for that present employees information
    profile.clear()
