import re
import string

# Load breached passwords from file
def load_breached_passwords(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        print("Warning: Breached passwords file not found. Skipping this check.")
        return set()

# Commonly used weak passwords (you can expand this list)
COMMON_PASSWORDS = {"123456", "password", "12345678", "qwerty", "abc123", "password1"}
BREACHED_PASSWORDS = load_breached_passwords("PwnedPasswordsTop100k.txt")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Character variety check
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add at least one digit.")
    
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Mix uppercase and lowercase letters.")
    
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&* etc.).")
    
    # Check for common passwords
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("Your password is too common. Choose a more unique one.")
        return 1, feedback  # Automatically weak if it's common
    
    # Check if password is in breached list
    if password in BREACHED_PASSWORDS:
        feedback.append("This password was found in many data breaches and is at the top 100,000 leaked passwords from the website Have I Been Pwned (https://haveibeenpwned.com) data set.")
        return 1, feedback  # Automatically weak if breached
    
    # Check for repeated characters or sequences
    if re.search(r'(.)\1{2,}', password):
        feedback.append("Avoid repeated characters.")
    
    return score, feedback

# Function to get strength label
def get_strength_label(score):
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    else:
        return "Strong"

# Main function to test the password strength
def main():
    password = input("Enter a password to test: ")
    score, feedback = check_password_strength(password)
    strength_label = get_strength_label(score)
    
    print(f"\nPassword Strength: {strength_label} ({score}/5)")
    if feedback:
        print("Suggestions:")
        for tip in feedback:
            print(f" - {tip}")

if __name__ == "__main__":
    main()
