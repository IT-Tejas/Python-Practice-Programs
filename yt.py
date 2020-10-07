print("""
************************************TECH_TEJAS******************************************
""")
try:
	try:
		from pytube import YouTube
	except:
		print("\nNeed To Download Some Files")
		inp=input("\nShould I Download (y/n): ")
		inp=inp.lower()
		if inp=='y':
			try:
				import pip
				pip.main(["install", "pytube"])
				pip.main(["install", "pytube3"])
				exit()
			except:
				print("Please Check Your Internet Connection!")
				exit()
		else:
			exit()
	link = input('\nEnter the link: ')
	print("\nPlease Wait....")
	yt = YouTube(link)
	print("\n***********************All Video Streams************************\n")
	stre = yt.streams.all()
	n=1
	for i in stre:
	    print(f"{n})    {i}")
	    n+=1
	qua=int(input("\nEnter Video Index Number: "))
	video=stre[qua-1]
	print(video)
	print("\nDownloading Started!")
	print("\n\n****************************Video Details*************************")
	print("\nTitle: "+yt.title)
	print("\nThumbnail: "+yt.thumbnail_url)
	video.download()
	print('\nDownload Completed!')
except Exception as e:
	print("\nSomething Went Wrong!")
#	print(e)
	exit()
