import sys, os, re


def Authenticate(user, password):
	#Open file
	with open("./files/Users.txt", "r") as f:
		for line in f:
			(u, p) = filter(None, re.split("[\W]", line))
			if user == u and password == p:
				print("Success")
				return
			elif user == u and not password == p:
				print("Failure: bad password")
				return
		#Reached end of file
		print("Failure: no such user")
		

if __name__ == "__main__":
	try:
		Authenticate(sys.argv[1], sys.argv[2])
	except IndexError:
		print("Invalid Arguments")
