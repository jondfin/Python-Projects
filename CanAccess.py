import sys, os, re

def getUserGroups(user):
	#returns list of groups that a user is part of
	groups = []
	data = []
	with open("./files/UserGroups.txt", "r") as f:
		data = f.readlines()
		for line in data:
			(group, users) = filter(None, line.split("="))
			userList = filter(None, re.split("[\W+]", users))
			for u in userList:
				if u == user:
					groups.append(group.strip())
					break
	return groups

def getObjGroups(obj):
	#returns a list of groups that an object is a part of
	groups = []
	data = []
	with open("./files/ObjectGroups.txt", "r") as f:
		data = f.readlines()
		for line in data:
			(group, objs) = filter(None, line.split("="))
			objList = filter(None, re.split("[\W+]", objs))
			for o in objList:
				if o == obj:
					groups.append(group.strip())
					break
	return groups

def CanAccess(operation, user, obj):
	data = []
	opExists = False

	#Check is user exists
	with open("./files/Users.txt", "r") as f:
		userExists = False
		for line in f:
			(u, p) = filter(None, re.split("[\W]", line))
			if u == user:
				userExists = True
				break
	if userExists == False:
		print("User {} does not exist").format(user)
		return

	userGroups = getUserGroups(user) #get a list of groups a user is a part of
	if not userGroups: #check if userGroups is empty
		print("Failure: User {} is not part of any user group").format(user)
		return
	if obj != "null":
		objGroups = getObjGroups(obj) #get a list of groups an object is a part of
	if not objGroups: #check if objGroups is empty
		print("Failure: Object {} is not part of any object group").format(obj)
		return

	#Read permissions
	with open("./files/AccessPermissions.txt", "r") as f:
		data = f.readlines()
		for line in data:
			(op, groups) = line.split("=")
			if op.strip() == operation:
				opExists = True
				groups = groups.strip()
				pairs = re.findall("\(\s?\'(.*?)\'\s?,\s?\'(.*?)\'\s?\)", groups)
				for pair in pairs:
					#check groups for access
					#e.g for pair (x, y)
					#if x is in userGroups and y is in objGroups
					userAccess = False 
					objAccess = False
					(ug, og) = pair
					#search userGroups
					for u in userGroups:
						if u == ug:
							userAccess = True
							break
					#search objGroups
					for o in objGroups:
						if o == og:
							objAccess = True
							break
					if userAccess and objAccess:
						if obj == "null":
							print("User {} has permission <{}>").format(user, operation)
							return
						print("User {} has permission <{}> on {}").format(user, operation, obj)
						return
	if opExists == False:
		print("Operation {} does not exist").format(operation)
		return
	if obj == "null":
		print("User {} does not have permission <{}>").format(user, operation)
		return
	print("User {} does not have permission <{}> on {}").format(user, operation, obj)

if __name__ == "__main__":
	try:
		if len(sys.argv) == 4:
			CanAccess(sys.argv[1], sys.argv[2], sys.argv[3])
		elif len(sys.argv) == 3:
			CanAccess(sys.argv[1], sys.argv[2], "null")
	except IndexError:
		print("Invalid arguments")
