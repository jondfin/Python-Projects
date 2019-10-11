By Jon Cobi Delfin NetID jjd279
Assignment 3

Setup:
	The set of programs requires a subdirectory called 'files' containing:
		Users.txt
		UserGroups.txt
		ObjectGroups.txt
		AccessPermissions.txt
	These should already be included in the submission but in case they get deleted
	In current directory do:
		mkdir files
		cd files/
		touch Users.txt
		touch UserGroups.txt
		touch ObjectGroups.txt
		touch AccessPermissions.txt
Programs:
	AddUser.py
	-Adds a user given a username and password
	How to run:
	python AddUser.py <username> <password>
	
	ex: Create 'user123' with password 'abcdefg'
		python AddUser.py user123 abcdefg
		User user123 successfully created
	ex: User has already been created
		python AddUser.py user123 abcdefg
		User user123 already exists

	Authenticate.py
	-Authenticates a user given username with matching password
	How to run:
	python Authenticate.py <username> <password>

	ex: Authenticate 'user123' with password 'abcdefg'
		python Authenticate.py user123 abcdefg
		Success
	ex: Authenticate 'user123' with bad password
		python Authenticate.py user123 oiasjd
		Failure: bad password
	ex: Authenticate non-existent user
		python Authenticate.py asdf qwer
		Failure: no such user

	AddUserToGroup.py
	-Adds a user to a user group given username and user group
	How to run:
	python AddUserToGroup.py <username> <groupname>
	
	ex. Add user 'user123' to group 'g1'
		python AddUserToGroup.py user123 g1
		Success: g1 = ['user123']
	    if other users were already in the group then it would be appended
		Success: g1 = ['abc1', 'abc2'. 'user123']
	ex. Add user already in the group
		python AddUserToGroup.py user123 g1
		User user123 is already in the group g1
	ex. Add non-existent user
		python AddUserToGroup.py asdf g1
		User user123 does not exist

	AddObjectToGroup.py
	-Adds an object to an object group given object name and object group
	How to run:
	python AddObjectToGroup.py <objectname> <groupname>

	ex. Add object 'obj123' to group 'g1'
		python AddObjectToGroup.py obj123 g1
		Success: g1 = ['obj123']
	    if other objects were already in the group then it would be appended
		Success: g1 = ['abc1', 'abc2'. 'obj123']
	ex. Add object already in the group
		python AddObjectToGroup.py obj123 g1
		Object obj123 is already in the group g1

	AddAccess.py
	-Gives access to a user group on an object group
	-If an object group is not provided a usergroup will still be given access
	How to run:
	python AddAccess.py <operation> <usergroupname> <objectgroupname>

	ex. Give user group 'users' operation 'view' on object group 'g1'
		python AddAccess.py view users g1
		Success: view = [('users, 'g1')]
	    if other user groups were given this operation then it would be appended
		Success: view = [('abc', '123'), ('efg', '456'), ('users', 'g1')]
	ex. User group already has access permission
		python AddAccess.py view users g1
		User group users already has permission <view> for object group g1
	ex. User group does not exist
		python AddAccess.py view zxcv g1
		User group zxcv does not exist
	ex. Object group does not exist
		python AddAcess.py view users zxcv
		Object group zxcv does not exist

	CanAccess.py
	-Reports whether or not a user can perform an operation on an object
	How to run:
	python CanAccess.py <operation> <username> <objectname>

	ex. Report if 'user' can 'view' 'obj123'
		python CanAccess.py view user obj123
		User user has permission <view> on obj123
	ex. Report if 'tom' can 'view' 'obj123' (tom is not part of usergroup user)
		python CanAccess.py view tom obj123
		User tom does not have permission <view> on obj123
	ex. Operation does not exist
		python CanAccess.py write user obj123
		Operation write does not exist
	ex. User does not exist
		python CanAccess.py view user1 obj123
		User user1 does not exist
	ex. User not in any user group
		python CanAccess.py view joe obj123
		User joe is not part of any user group
	ex. Object not in any object group
		python CanAccess.py view user obj456
		Object obj456 is not part of any object group

	*If any of the programs are provided with an invalid argument it will report "Invalid arguments"
