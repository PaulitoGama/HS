#comment
# Write your code here
import random

class User:
    def __init__(self):
        self.account_exists = False
        self.card_number = None
        self.pin = None
        self.balance = None
        
    def create_account(self):
        print(
f"""
Your card has been created"
Your card number:
{self.create_card_number()}
"Your card PIN:"
{self.create_card_pin()}
"""
        )
        self.balance = 0
        
    def create_card_number(self):
        self.card_number = self.create_issuer_identification_number() + self.create_customer_account_number() + self.create_checksum()
        return self.card_number

    def create_issuer_identification_number(self):
        return '400000'

    def create_customer_account_number(self):
        self.list_of_numbers = list()
        
        while len(self.list_of_numbers) < 9:
            self.list_of_numbers.append(random.randint(0, 9))

        random.shuffle(self.list_of_numbers)
        return ''.join(list(map(str, self.list_of_numbers)))
        
    def create_checksum(self):
        return str(random.randint(0, 9))
    
    def create_card_pin(self):
        self.card_pin = list()

        while len(self.card_pin) < 4:
            self.card_pin.append(random.randint(0, 9))

        self.pin = ''.join(list(map(str, self.card_pin)))

        return ''.join(list(map(str, self.card_pin)))
        
    def log_in(self):
        print("Enter your card number:")
        print(self.card_number)
        self.card_number_input = input()
        print("Enter your PIN:")
        print(self.card_pin)
        self.card_PIN_input = input()
        
        if self.card_number_input == self.card_number and self.card_PIN_input == self.pin:
            print("You have successfully logged in!")
            while True:
                print(
"""
1. Balance
2. Log out
0. Exit
"""             )

                # user_input = int(input())

                # if user_input == 1:
                #     print('Balance: ' + str(self.balance))
                # elif user_input == 2:
                #     print("You have successfully logged out!")
                #     break

                # Apparently not needed for the exercise
        else:
            print("Wrong card number or PIN!")
            
                
                

user = User()

while True:
    print("""
1. Create an account, 
2. Log into account, 
0. Exit
    """)
        
    user_input = int(input())
    
    if user_input == 0:
        print("Bye!")
        break
    elif user_input == 1:
        user.create_account()
    elif user_input == 2:
        user.log_in()