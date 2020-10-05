try:
	try:
		import pytube
	except:
		print("\nNeed To Download Some Files")
		inp=input("\nShould I Download (y/n): ")
		inp=inp.lower()
		if inp=='y':
			try:
				import os
				os.system("pip install pytube")
				os.system("pip install pytube3")
				exit()
			except:
				print("Please Check Your Internet Connection!")
				exit()
		else:
			exit()
	link = input('\nEnter the link: ')
	print("\nPlease Wait....")
	yt = pytube.YouTube(link)
	stream = yt.streams.first()
	print("\nDownloading Started!")
	stream.download()
	print('\nDownload Completed!')
except:
	print("\nSomething Went Wrong!")
	exit()
