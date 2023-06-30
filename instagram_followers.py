import instaloader

# Create an instance of Instaloader
loader = instaloader.Instaloader()

# Login to your Instagram account
username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")
loader.login(username, password)

# Retrieve the profile of the target account
target_username = "target_username"
profile = instaloader.Profile.from_username(loader.context, dpz_cartoon_)

# Rest of the code...


