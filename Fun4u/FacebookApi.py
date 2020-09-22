
from fbchat import Client 
from fbchat.models import Message

username = "Your username or email"
password = "*************"

# login to fb
client = Client(username,password)

# logout from fb
client.logout()

# send message to your friends
client.send( Message(text = "Message"),
			 thread_id = "friend_user_id",
			 thread_type = ThreadType.USER)

# send message to any group
client.send( Message(text = "Message"),
			 thread_id = "group_id",
			 thread_type = ThreadType.GROUP)

# serching user
users = client.searchForUsers("name of the user")
for user in users :
	print(user)

# Get user information 
users = client.searchForUsers("name of user")
user = users[0]
# ================= User info ===================
print(f"user id :  {user.uid}")
print(f"user name : {user.name}")
print(f"user profile pic : {user.photo}")
print(f"user url : {user.url}")