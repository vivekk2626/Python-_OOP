from multiprocessing import Pool;

if __name__ == '__main__':
	
	list=[1,2,3,4,5,6,7,8,9];

	def square(no):
		return (no*no);	

	p=multiprocessing.Pool();

	result=p.map(square,list);

	print(result);		