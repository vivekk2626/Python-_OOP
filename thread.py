import threading;

def fun(no,lock):
	lock.acquire();

	print("\n Inside Fun ");
	for i in range(no):
		print(i);

	lock.release();	
		

def gun(no,lock):
	lock.acquire();

	print("\nInside Gun");
	for i in range(no):
		print(i);
		
	lock.release();	



if __name__ == '__main__':

	lock=threading.Lock();

	print("\n*********** Application For Multi-Threading...**************");

	no=int(input("\n Enter the number :"));

	thread1=threading.Thread(target=fun,args=(no,lock));
	thread2=threading.Thread(target=gun,args=(no,lock));

	thread1.start();
	thread2.start();

	thread1.join();
	thread2.join();
