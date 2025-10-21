# Get user email address
email = input("What is your email address?: ").strip()

# slice out user name
user = email[:email.index("@")]

# slice domain name
domain = email[email.index("@") +1 :]

# format meassage
result = (f"Hey your username is {user} and your domain is {domain}")

# display output message
print(result)

# we use strip() to avoid spaces