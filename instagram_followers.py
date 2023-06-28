import instaloader
# Create an instance of Instaloader
loader = instaloader.Instaloader()

# Login to an Instagram account (optional)
loader.login('herrlybag', 'saadsaad')

# Retrieve the profile of the target account
profile = instaloader.Profile.from_username(loader.context, 'girls_anime_dpz')

# Get the followers of the target account
followers = profile.get_followers()

# Iterate over the followers and print their usernames
for follower in followers:
    print(follower.username)


