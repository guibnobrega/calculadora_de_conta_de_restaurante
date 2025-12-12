import os

def clear_console():
    """Clear the console based on the operating system(for better readability)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def calculator(total_bill, tip_amount,people)  :
    result = round(total_bill*(1+ (tip_amount/100))/people, 2)
    return result




def main():
    clear_console()
    print("Welcome to the tip calculator!")
    total_bill = float(input("What was the total bill? $ "))
    tip_amount = int(input("How much tip would you like to give? 10, 12 or 15? "))
    people = int(input("How many people to split the bill? "))

    total_by_person = calculator(total_bill, tip_amount,people)

    print(f"Each person should pay: ${total_by_person}")
    
main()