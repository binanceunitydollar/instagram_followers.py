import instaloader

# Create an instance of Instaloader
loader = instaloader.Instaloader()

# Login to your Instagram account (optional)
loader.login('your_username', 'your_password')

# Retrieve the profile of the target account
target_username = 'dpz_king'
profile = instaloader.Profile.from_username(loader.context, target_username)

# Get the followers of the target account
followers = profile.get_followers()

# Iterate over the followers and perform actions (e.g., follow them)
for follower in followers:
    # Perform action on each follower (e.g., follow)
    # Your custom code here

# Print a success message
print("Followers retrieved and action performed successfully.")




