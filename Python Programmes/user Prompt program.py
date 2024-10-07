
#Write a program in Python that prompts the user to enter a number of integer values.
#The program stores the integers, counts the frequency of each integer and displays the frequency as per Figure


def Console():
 print("#######################\nWELCOME TO DBS CONSOLE\n#######################\n")

 elements = int(input("Please input the Number of Elements to be Stored in the List: "))
 list = []
 frequency = {} # in order to store frequency iam using dictionary
 print("Input ",elements, " into the List")

 for i in range(elements):
  x = input("Element - " + str(i)+ ": ")
  list.append(x)

 print("\n")

 for item in list:
  if item in frequency: #checks if current item is already present
    frequency[item] += 1 #if yes, increments it
  else:
    frequency[item] = 1 #if no, the value will be 1 as constant

 for key,value in frequency.items():
  print(str(key), " occurs ", str(value), " times ")


Console()