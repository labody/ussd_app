"""
This is the python code for a ussd application 
Through it, the user is able to check their account balance, send money and buy airtime

"""

balance = 1000.0
short_code = '*123#'
while True: 
    user_short_code = input('Enter Short Code: ')
    
    # Ensure user enters appropriate short code
    while (user_short_code != short_code): 
     user_short_code = input("Enter *123# to access menu: ")

    initial_menu_option =  input("Select Option: \n1.Check Balance \n2.Send Money \n3.Buy Airtime") 
    print(initial_menu_option)

    if (initial_menu_option == "1"):
        print(f"Your account balance is {balance} GHS")
        
    elif (initial_menu_option == "2"):
        recipient_number = input("Enter recipient's number: \n")    
        while (len(recipient_number) != 10 ):
            recipient_number = input('Enter a ten digit mobile number: ')

        re_entered_recipient_number = input("Re-enter recipient's number:")

        while (re_entered_recipient_number != recipient_number):
            re_entered_recipient_number = input("Numbers do not match, kindly enter number again: ")

        amount_to_be_sent = input("Enter amount: ")    
        while (float(amount_to_be_sent) > balance):
            amount_to_be_sent = input('Insufficient funds. Enter amount again: ')

        confirmation_option = input(f"Are you sure you want to send {amount_to_be_sent}GHS to {recipient_number} ? \n1.Yes \n2.No") 

        while (int(confirmation_option) != 1 and int(confirmation_option) != 2):
          confirmation_option =  input('Invalid Option. Choose 1 or 2: ')       

        if (int(confirmation_option) == 1):
             print(f"Payment of {amount_to_be_sent}GHS made to {recipient_number}. Your balance is {balance - float(amount_to_be_sent)}")       
        
        elif (int(confirmation_option) == 2):
            print("Transaction unsuccessful")
  
    elif (initial_menu_option == "3"):
        recharge_amount = input("Enter recharge amount: ") 

        while (float(recharge_amount) == 0 or float(recharge_amount) > balance):
            recharge_amount = input(f"Enter a recharge amount between 1 - {balance}")

        if (float(recharge_amount) >= 1 and float(recharge_amount) <= balance):            
            airtime_confirmation_option = input(f"You are purchashing an airtime of {recharge_amount} for {float(recharge_amount) / 2}GHS. Do you wish to continue? \n1.Yes \n2.No \n")
          
            if(int(airtime_confirmation_option) == 1):
                print(f"Congratulations. Airtime of {recharge_amount} purchased for an amount of {float(recharge_amount) / 2}")
           
            elif(int(airtime_confirmation_option)== 2):
                print("Transaction Unsuccessful. Airtime not purchased.")
        else: 
            recharge_amount = input("Enter a valid recharge amount: ")

