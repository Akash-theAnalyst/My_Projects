
#Write a program in Python to prompt the user to input their name, employee number, week ending date, hours worked, rate per hour, standard and overtime tax percentage rate.
#Use the data input to calculate gross pay, tax deductions and net pay. Output the results as a formatted payslip. Assume that a standard working week is 37.5 hours.
#E.g. Ask the user to enter the following data:
#Employee Name: Employee Number: Week ending:
#Number of hours worked: Hourly Rate:
#Overtime Rate: Standard Tax Rate: Overtime Tax Rate:
#(sample input – Mark Bate) (sample input – 123456789A) (sample input - 26/01/2018) (sample input – 42.5) (sample input – 10.50) (time-and-a-half as 1.5) (sample input – 20)
#(sample input – 50)
#Once the above data has been entered the program should display the employee’s payslip as per the following example:


def PaySlip():
  empName = input("Enter the Employee Name: ")
  empNumber = input("Enter the Employee Number: ")
  weekEnding = input("Enter the Week Ending: ")

  standardWorkingWeek = 37.50 #Since Standard working week is 37.5 hours, We are keeping it as constant.
  hoursWorked = float(input("Enter the Number of Hours Worked by Employee: "))
  overTimeHours = hoursWorked-standardWorkingWeek

  hourlyRate = float(input("Enter the Hourly Rate for the Employee: "))
  overtimeRate = hourlyRate*1.5
  standardTaxRate = float(input("Enter the Standard Tax Rate for the Employee: "))
  overtimeTaxRate = float(input("Enter the Overtime Tax Rate for the Employee: "))


  normalTotal = round(standardWorkingWeek*hourlyRate,2)
  overtimeTotal = round(overTimeHours*overtimeRate,2)

  normalDeductions = round(normalTotal * (standardTaxRate/100),2)
  overtimeDeductions = round(overtimeTotal * (overtimeTaxRate/100),2)

  netPay = round((normalTotal+overtimeTotal)-(normalDeductions+overtimeDeductions),2)



  print("                                             PAYSLIP                                            ")

  print("WEEK ENDING: ", weekEnding)
  print("Employee: ", empName)
  print("Employee Number", empNumber)
  print("\n")
  print("                               Earnings","            Deductions")
  print("                      Hours","     Rate","       Total")
  print("\n")
  print("Hours(Normal)        ", standardWorkingWeek,"    ",hourlyRate,"       ",normalTotal, " Tax @ ",standardTaxRate,"%  ",normalDeductions)
  print("Hours(Overtime)      ", overTimeHours,"    ",overtimeRate,"       ",overtimeTotal, "    Tax @ ",overtimeTaxRate,"%  ",overtimeDeductions)
  print("\n")
  print("                         Total Pay:           ",round(normalTotal+overtimeTotal,2))
  print("                  Total Deductions:           ",round(normalDeductions+overtimeDeductions,2))
  print("                           Net Pay:           ",round(netPay,2))


PaySlip()