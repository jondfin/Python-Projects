import sys, os, re

def userGroupExists(userGroupName):
	data = []
	with open("./files/UserGroups.txt", "r") as f:
		data = f.readlines()
		for line in data:
			(group, users) = filter(None, line.split("="))
			if group.strip() == userGroupName:
				return
	print("User group {} does not exist").format(userGroupName)
	sys.exit(0)

def objGroupExists(objectGroupName):
	data = []
	with open("./files/ObjectGroups.txt", "r") as f:
		data = f.readlines()
		for line in data:
			(group, objects) = filter(None, line.split("="))
			if group.strip() == objectGroupName:
				return
	print("Object group {} does not exist").format(objectGroupName)
	sys.exit(0)

def AddAccess(operation, userGroupName, objectGroupName):
	#Check if user group and object group exists
	userGroupExists(userGroupName)
	objGroupExists(objectGroupName)

	data = []
	index = 0
	opExists = False
	#search data
	with open("./files/AccessPermissions.txt", "r") as f:
		data = f.readlines()
		for line in data:
			(op, groups) = filter(None, line.split("="))
			if op.strip() == operation:
				opExists = True
				groups = groups.strip()
				pairs = re.findall("\(\s?\'(.*?)\'\s?,\s?\'(.*?)\'\s?\)", groups) #turn into tuple
				#search each tuple
				for pair in pairs:
					(u, o) = pair
					if u == userGroupName and o == objectGroupName:
						print("User group {} already has permission <{}> for object group: {}").format(userGroupName, operation, objectGroupName)
						return
				#access doesnt exist for usergroup
				break
			index += 1
	#add new operation if it doesnt exists
	if opExists == False:
		with open("./files/AccessPermissions.txt", "a") as f:
			t = (userGroupName, objectGroupName)
			newline = "{} = [{}]".format(operation, t)
			print("Success: {}").format(newline)
			f.write(newline)
			return

	#add new tuple to operation
	with open("./files/AccessPermissions.txt", "r+") as f:
		(op, groups) = filter(None, data[index].split("="))
		groups = groups.strip()
		pairs = re.findall("\(\s?\'(.*?)\'\s?,\s?\'(.*?)\'\s?\)", groups)
		t = (userGroupName, objectGroupName)
		pairs.append(t)
		newline = "{} = {}\n".format(operation, pairs)
		data[index] = newline
		print("Success: {} = {}").format(operation, pairs)
		f.writelines(data)
		return	

if __name__ == "__main__":
	#If object group is defined, need to add object instead of user?
	try:
		if len(sys.argv) == 4:
			AddAccess(sys.argv[1], sys.argv[2], sys.argv[3])
		elif len(sys.argv) == 3:
			AddAccess(sys.argv[1], sys.argv[2], "null")
	except IndexError:
		print("Invalid arguments")

