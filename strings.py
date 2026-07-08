# String Manipulation



text = "cybersecurity"
first_char = text[0] # Get the first character of the above variable
print(first_char)


# Slicing

text1 = "Cyber-Security"
Slice = text1[-8:]
print(Slice)


# Example of practical use of slicing

filename= "cmdiop.exe"
if filename [-4] == ".exe" or filename[-4:] == ".EXE":
    print("This is an executable file")


# Split Function
# Breaks a string into a list of substrings based on a specified delimiter

text2 = "Cyber Security"
words = text2.split()
print(words)


# Common String Methods
text3 = "String Manipulation"
print(text3.upper()) # Converts the string to uppercase
print(text3.lower()) # Converts the string to lowercase

# Trimming whitespace from a string
text4 = "  String Manipulation  "
print(text4.strip()) # Removes leading and trailing whitespace

# Replace Characters in a String
text5 = "String Manipulation"
print(text5.replace("Manipulation", "Operations")) # Replaces "Manipulation" with


message = "User Password: password123"
secure_message = message.replace("password123", "[REDACTED]")   
print(secure_message)

# Finding Substrings

email = "pmedley@example.com"
print(email.find("@")) # Finds the index of the "@" character

print(email[7:])
domain = email.split("@")[1]
print(domain)


Username = email[:email.index("@")]
Domain = email[email.index("@") +1;]")]

print("Username:", Username)
print("Domain:", Domain)


