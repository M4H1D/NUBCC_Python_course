while True:
	age=int(input("Enter your age(0-68): "))
	if 0<=age<13:
		if age%2==0:
			print("you are child and your age is Even.")
			x=input("'continue' or 'exit': ")
			if x=="exit":
				break
			else:
				continue 
		else:
			print("you are child and your age is Odd.")
			x=input("'continue' or 'exit': ")
			if x=="exit":
				break
			else:
				continue 
	elif 13<=age<20:
		if age%2==0:
			print("you are teenage and your age is Even.")
			x=input("'continue' or 'exit': ")
			if x=="exit":
				break
			else:
				continue 
		else:
			print("you are teenage and your age is Odd.")
			x=input("'continue' or 'exit': ")
			if x=="exit":
				break
			else:
				continue 
	elif 20<=age<35:
		if age%2==0:
			print("you are youth and your age is Even.")
			x=input("'continue' or 'exit': ")
			if x=="exit":
				break
			else:
				continue 
		else:
			print("you are youth and your age is Odd.")
			x=input("'continue' or 'exit': ")
			if x=="exit":
				break
			else:
				continue 
	elif 35<=age<51:
		if age%2==0:
			print("you are middle age and your age is Even.")
			x=input("'continue' or 'exit': ")
			if x=="exit":
				break
			else:
				continue 
		else:
			print("you are middle age and your age is Odd.")
			x=input("'continue' or 'exit': ")
			if x=="exit":
				break
			else:
				continue 
	elif 51<=age<69:
		if age%2==0:
			print("you are old and your age is Even.")
			x=input("'continue' or 'exit': ")
			if x=="exit":
				break
			else:
				continue 
		else:
			print("you are old and your age is Odd.")
			x=input("'continue' or 'exit': ")
			if x=="exit":
				break
			else:
				continue 
	
	else:
		print("please Enter correctly.")
		