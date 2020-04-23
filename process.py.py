from multiprocessing import Process;
import os;

print("\n*********** Application For Multiprocessing ****************");

def fun(number):

	print("\nParent Process Of Fun :",os.getppid());
	print("\nChild Process Of Fun :",os.getpid());

	for i in range(number):
		print(i);



def gun(number):

	print("\nParent Process Of Gun  :",os.getppid());
	print("\nChild Process Of Gun :",os.getpid());
	
	for i in range(number):
		print(i);		


if __name__ == '__main__':

	print("\nTotal core in CPU :",os.cpu_count())
	
	print("\nParent Process Of Main  :",os.getppid());
	print("\nChild Process Of Main :",os.getpid());

	number=100;

	p1=multiprocessing.Process(target=fun,args=(number,));
	p2=multiprocessing.Process(target=gun,args=(number,));

	p1.start();
	p2.start();

	p1.join();
	p2.join();



		
