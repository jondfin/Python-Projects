import sys, os, re

def AddUserToGroup(user, userGroup):
	#Check is user exists
	with open("./files/Users.txt", "r") as f:
		exist = False
		for line in f:
			(u, p) = filter(None, re.split("[\W]", line))
			if u == user:
				exist = True
				break
	if exist == False:
		print("User {} does not exist").format(user)
		return
	
	data = [] #store file lines
	index = 0 #tracks which line to overwrite
	groupExists = False

	#Check if user is already in group, also search for user group
	with open("./files/UserGroups.txt", "r") as f:
		data = f.readlines()
		for line in data:
			(group, users) = filter(None, line.split("="))
			if group.strip() == userGroup:
				groupExists = True
				break
			index += 1

	#if group didnt exist then create it and append to end of file
	if groupExists == False:
		with open("./files/UserGroups.txt", "a") as f:
			newline = "{} = ['{}']\n".format(userGroup, user)
			print("Success: {} = ['{}']").format(userGroup, user)
			f.write(newline)
			return

	#add user to group	
	with open("./files/UserGroups.txt", "r+") as f:
		(group, users) = filter(None, data[index].split("=")) #separate into user group and users
		userList = filter(None, re.split("[\W]+", users)) #turn users into list
		if user in userList:
			print("User {} is already in the group {}").format(user, userGroup)
			return
		userList.append(user)
		newline = "{} = {}\n".format(userGroup, userList)
		print("Success: {} = {}").format(userGroup, userList)
		data[index] = newline
		f.writelines(data)
	
	return				

if __name__ == "__main__":
	try:
		AddUserToGroup(sys.argv[1], sys.argv[2])
	except IndexError:
		print("Invalid arguments")

