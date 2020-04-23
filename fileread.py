if __name__ == '__main__':
	
	print("\n******Application For File Reading ************");

	print("\n*********** File open ******************8****")
	fd=open("file.txt",mode='r',encoding='utf-8');  #means if file exists open file with append mode in read otherwise open in read mode


	print("\n***********Information About File :***********");
	print("\n",fd)
	

	print("\n***********Reading File Data Multiple Ways************************")

	print("\nReading 1st Line of File :")
	print(fd.readline());
	fd.seek(0);            # read karat karat yacha cursor line cha end la jato tyala parat initial la set karane.

	print("\nReading whole File :")
	print(fd.read());
	fd.seek(0);

	print("\nReading Specific byte of Data :")
	print(fd.read(5))
	

	print("\n Get the File Change Current Position :",fd.seek(2))
	
	print("\n Get the File Current Position :",fd.tell())
	

	print("\n*********** File Close ******************8****")
	fd.close();

	print("\n*********** File Open ******************8****")
	fd=open("file.txt",'a+');

	print("\nWrite the File :")
	fd.write("\nAAi:ssss");
	fd.seek(0);

	print("\nReading whole File :")
	print(fd.read());


	fd.close();
	print("\n*********** File Close ***********************")