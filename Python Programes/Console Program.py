

#Write a program in Python which prompts the user for their username in the format Domain Name\Username as per Figure
#On entering their domain and username and pressing carriage return, write out to the console window each individual data item as per Figure


def Console():
 print("#######################\nWELCOME TO DBS CONSOLE\n#######################\n")

 userName = input("Please Enter your Username: ")

 sepUserName = userName.split("\\")

 print("Domain: ", sepUserName[0])
 print("User Name: ", sepUserName[1])


Console()