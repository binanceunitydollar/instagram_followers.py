import instaloader

# Create an instance of Instaloader
loader = instaloader.Instaloader()

# Login to your Instagram account
username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")
loader.login(username, password)

# Retrieve the profile of the target account
target_username = input("Enter the target account username: ")
profile = instaloader.Profile.from_username(loader.context, target_username)

# Get the followers of the target account
followers = profile.get_followers()

# Rest of the code...



