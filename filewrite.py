

if __name__ == '__main__':

	print("\nApplication For File Writting Purpose :");

	fd=open('file1.txt','a+');

	fd.write("\nAaai");

	fd.seek(0);

	print(fd.read());




	

	fd.close();