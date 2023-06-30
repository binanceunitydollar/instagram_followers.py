import instaloader

# Create an instance of Instaloader
loader = instaloader.Instaloader()

# Login to your Instagram account
username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")
loader.login(username, password)

# Prompt user to enter the target account username
target_username = input("cartoon_dp3")

try:
    # Retrieve the profile of the target account
    profile = instaloader.Profile.from_username(loader.context, target_username)

    # Rest of the code...
    followers = profile.get_followers()
    for follower in followers:
        print(follower.username)

except instaloader.exceptions.ProfileNotExistsException:
    print("Invalid target account username. Please try again.")



