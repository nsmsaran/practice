import sys
import random

def greet_user():
    print("Hello! I am a Simple Python Chat Bot.")
    print("I can help you with the following tasks:")
    print("1. Palindrome checker")
    print("2. Basic mathematical calculator")
    print("3. Password generator")
    print("4. Password strength checker")
    print("5. Odd or even number checker")
    print("6. Leap year checker")
    print("7. Exit")

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

def basic_calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        op = input("Enter the operator (+, -, *, /): ")

        if op == '+':
            print(f"Result: {num1 + num2}")
        elif op == '-':
            print(f"Result: {num1 - num2}")
        elif op == '*':
            print(f"Result: {num1 * num2}")
        elif op == '/':
            if num2 == 0:
                print("Error: Division by zero!")
            else:
                print(f"Result: {num1 / num2}")
        else:
            print("Invalid operator.")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")

def generate_password():
    length = int(input("Enter the length of the password: "))
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;:,.<>/?"
    password = "".join(random.sample(chars, length))
    print(f"Generated password: {password}")

def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    elif any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
        return "Strong"
    else:
        return "Moderate"

def odd_or_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    greet_user()
    
    while True:
        choice = input("What would you like to do? Enter the number (1-7): ")
        
        if choice == '1':
            word = input("Enter a word or phrase to check if it's a palindrome: ")
            if is_palindrome(word):
                print(f"'{word}' is a palindrome.")
            else:
                print(f"'{word}' is not a palindrome.")
        
        elif choice == '2':
            basic_calculator()
        
        elif choice == '3':
            generate_password()
        
        elif choice == '4':
            password = input("Enter a password to check its strength: ")
            strength = check_password_strength(password)
            print(f"The password '{password}' is {strength}.")
        
        elif choice == '5':
            number = int(input("Enter a number to check if it's odd or even: "))
            result = odd_or_even(number)
            print(f"The number {number} is {result}.")
        
        elif choice == '6':
            year = int(input("Enter a year to check if it's a leap year: "))
            if is_leap_year(year):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
        
        elif choice == '7' or choice.lower() in ['exit', 'goodbye', 'bye']:
            print("Goodbye! Have a great day!")
            break
        
        else:
            print("Invalid choice! Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
