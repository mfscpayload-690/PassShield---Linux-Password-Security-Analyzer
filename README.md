**PassShield - Linux Password Security Analyzer**

**Overview:**

_This Python script analyzes the strength of a given password based on various factors like length, character diversity, and common weaknesses. It provides feedback to help users create stronger passwords._

**Features:**

Evaluates password strength on a scale of Weak, Moderate, and Strong

**Checks for:**

_Length (minimum 8 characters recommended, 12+ is stronger)_

_Character diversity (uppercase, lowercase, numbers, special characters)_

_Commonly used weak passwords_

_Repetitive characters or sequences_

_Leaked passwords from data breaches using the PwnedPasswordsTop100k.txt dataset_

_Provides suggestions for improvement_

**Installation**

Ensure you have `python3` installed. Clone this repository and navigate to the project folder:

`$ git clone https://github.com/mfscpayload-690/PassShield.git`
`$ cd PassShield`

**Usage:**

Download the `PwnedPasswordsTop100k.txt` file from Have I Been Pwned (https://haveibeenpwned.com)

Place the file in the same directory as the script.

Run the script in a terminal:

`$ python password_strength_analyzer.py`

Enter a password when prompted, and the script will evaluate its strength and provide feedback.

**Example:**

> `Enter a password to test: password123`

> `Password Strength: Weak (1/5)`
>  `Suggestions:`
>   `- Your password is too common. Choose a more unique one.`
>   `- This password was found in many data breaches and is at the top 100,000 leaked passwords from the website Have I Been Pwned (https://haveibeenpwned.com) data set.`

**Contributing**

_Feel free to fork this repository and submit pull requests with improvements!_

**License:**

This project is licensed under the MIT License.

