#while_loops_lists.py

# create a list of unverified users
unconfirmed_users = ['tony', 'frank','mary']

# en empty list with confirmed users
confirmed_users = []

while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)

#display all confirmed users
print("\nThe following uses have been confirmed")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())