import instaloader

# Create an instance of Instaloader
loader = instaloader.Instaloader()

# Login to your Instagram account
username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")
loader.login(username, password)

# Set the target account username
target_username = 'dpz_king'

try:
    # Retrieve the profile of the target account
    profile = instaloader.Profile.from_username(loader.context, target_username)

    # Get the followers of the target account
    followers = profile.get_followers()

    # Open the 'followers.txt' file in write mode
    with open("followers.txt", "w") as file:
        # Iterate over the followers and write their usernames to the file
        for follower in followers:
            file.write(follower.username + "\n")

    print("Followers saved to 'followers.txt' file.")

except instaloader.exceptions.ProfileNotExistsException:
    print("Invalid target account username. Please try again.")





