import sys, os, re

def AddObjectToGroup(objectname, groupname):
	data = []
	index = 0
	groupExists = False


	#Read file
	with open("./files/ObjectGroups.txt", "r") as f:
		data = f.readlines()
		for line in data:
			(group, obj) = filter(None, line.split("="))
			#Look for group
			if group.strip() == groupname:
				groupExists = True
				break
			index += 1
	#Create group and add object to it
	if groupExists == False:
		with open("./files/ObjectGroups.txt", "a") as f:
			newline = "{} = ['{}']".format(groupname, objectname)
			print("Success: {}").format(newline)
			f.write(newline)
			return
	#Add object to group
	with open("./files/ObjectGroups.txt", "r+") as f:
		(group, obj) = filter(None, data[index].split("="))
		objList = filter(None, re.split("[\W+]", obj))
		#Look for object in group
		if objectname in objList:
			print("Object {} is already in group {}").format(objectname, groupname)
			return
		objList.append(objectname)
		newline = "{} = {}\n".format(groupname, objList)
		data[index] = newline
		print("Success: {} = {}").format(groupname, objList)
		f.writelines(data)
		return	
		

if __name__ == "__main__":
	try:
		AddObjectToGroup(sys.argv[1], sys.argv[2])
	except IndexError:
		print("Invalid arguments")
