
#Implement the MYPY Phone Book System in Python as per Figure, which allows users to add, delete, update and lookup phone numbers.
#The MYPY Phone Book System should store the individual’s Full Name and Phone Number. Your program should not allow users to add the same number twice.
#On adding, deleting, updating or looking up a number, your program should let the user know if the operation was successful or not.
#On looking up a number return the full name and number of the individual; if the number is not found give the user the option to add the details they are looking up.
#The user can perform multiple actions; they can add a new entry and subsequently delete an entry without having to stop and start the program until they decide to quit.


def PhoneBook():

  contacts = {}

  while True :
    print("\n#######################\nMYPY PHONE BOOK\n#######################\n")

    print("1 : Add New Entry")
    print("2 : Delete Entry")
    print("3 : Update Entry")
    print("4 : Lookup Number")
    print("5 : Quit Program")

    userInput = int(input("Enter your function: "))

    if userInput == 1:
      fullName = input("Enter Full Name: ")
      mobileNumber = input("Enter Mobile Number: ")

      if mobileNumber in contacts.values():
        print("Phone Number already Exists")
      else:
        contacts[fullName] = mobileNumber
        print("Contact Added Successfully Inside the Phone Book")

    elif userInput == 2:
      fullName = input("Enter the Name of Contact to Delete: ")

      if fullName in contacts:
        del contacts[fullName]
        print("The Contact has been Deleted Successfully!")
      else:
        print("The requested Contact does not Exist!")

    elif userInput == 3:
      fullName = input("Enter the Name of Contact to Update: ")
      new_mobileNumber = input("Enter the Updated Number: ")

      if fullName in contacts:
        contacts[fullName] = new_mobileNumber
        print("The Contact has been Updated Successfully!")
      else:
        print("The requested Contact does not Exist!")

    elif userInput == 4:
      mobileNumber = input("Enter the Phone Number to Lookup: ")
      conFound = False

      for fullName,number in contacts.items():
          if mobileNumber == number:
            print("Full Name : ", fullName,", Phone Number : ", number)
            conFound = True
            break
      if conFound != True:
        print("The requested Contact could not be found")
        choice = input("Do you want to add this contact?, Enter Yes/ No")
        if choice.lower() == "yes":
          fullName = input("Enter the Full Name: ")
          contacts[fullName] = mobileNumber

    elif userInput == 5:
      print("The Phone Book is closing...")
      break

    else:
      print("Invalid Input, Please Try Again!")


PhoneBook()