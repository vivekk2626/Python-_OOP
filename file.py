if __name__ == '__main__':
	
	print("\n******Application For File System ************");

	fd=open("file.txt",mode='r',encoding='utf-8');  #means if file exists open file with append mode in read otherwise open in read mode


	print("\n***********Information About File :***********");
	print("\n",fd)
	

	print("\n*********** File Data ************************")
	print(fd.readline());
	

	print("\n Get the File Change Current Position :",fd.seek(2))
	
	print("\n Get the File Current Position :",fd.tell())
	
	print("\n Get the File Change Current Position :",fd.seek(20));

	print("\n Get the File Current Position :",fd.tell())

	print("\n*********** File Close ******************8****")
	fd.close();

