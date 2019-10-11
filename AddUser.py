import sys, os, re

def AddUser(user, password):
	#Open file and read	
	with open("./files/Users.txt", "a+") as f:
		#Compare to each user
		for line in f:
			(u, p) = filter(None, re.split("[\W]", line))
			if user == u:
				print("User {} already exists.").format(user)
				return
		#User not found, create
		newEntry = "\"{}\":{}\n".format(user, password)
		f.write(newEntry)
		print("User {} successfully created").format(user)
if __name__ == "__main__":
	try:
		AddUser(sys.argv[1], sys.argv[2])
	except IndexError:
		print("Invalid arguments")
