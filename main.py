def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                    print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
            
    return amount 

def get_number_of_lines():

def main():
    balance = deposit(0)
   
main() 
    
    