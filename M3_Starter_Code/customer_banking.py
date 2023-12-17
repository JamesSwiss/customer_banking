# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account 

# Define the main function. Provided code 
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account. Copied and/or adjusted from started code and class activities
    savings_balance = float(input('What is your initial savings account balance? '))
    savings_interest = float(input('What is the interest rate for your savings account? '))
    savings_months = int(input('What is the number of months for your savings account? '))

    # Call the create_savings_account function and pass the variables from the user. Copied and/or adjusted from started code and class activities
    savings_result = create_savings_account(savings_balance, savings_interest, savings_months)
    
    if savings_result is not None:
        updated_savings_balance, savings_interest_earned = savings_result
        # Print out the interest earned and updated savings account balance with interest earned for the given months. Bing ask combined with class activties from current and previous module.
        print("\nSavings Account Results:")
        print(f"Interest earned on savings account: ${savings_interest_earned}")
        print(f"Updated savings account balance: ${updated_savings_balance}")
    else:
        print("Error in processing savings account.")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account. Copied and/or adjusted from started code and class activities
    cd_balance = float(input('What is your initial CD account balance? '))
    cd_interest = float(input('What is the APR for the CD account? '))
    cd_maturity = int(input('What is the length of months for your CD? '))

    # Call the create_cd_account function and pass the variables from the user.
    cd_result = create_cd_account(cd_balance, cd_interest, cd_maturity)
    
    if cd_result is not None:
        updated_cd_balance, cd_interest_earned = cd_result
        # Print out the interest earned and updated CD account balance with interest earned for the given months.
        print("\nCD Account Results:")
        print(f"Interest earned on CD account: ${cd_interest_earned}")
        print(f"Updated CD account balance: ${updated_cd_balance}")
    else:
        print("Error in processing CD account.")

# #Call the main function. Line 46 code provided 
if __name__ == "__main__":
   
    main()
