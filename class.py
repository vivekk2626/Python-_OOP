print("\n ************Application for Python OOP Concepts :***************");

class demo:
	x=60;

	def __init__(self,ino1,ino2):
		print("\nInside Init Constructor :");
		self.ino=ino1;
		self.ino2=ino2;

	@classmethod	
	def Fun(cls):
		print("\nInside Fun Class Method :");	

	@staticmethod	
	def add(a,b):
		print("\nAddition is Static Method :",a+b);





obj1=demo(10,20);

print("\nClass Variable value is :",demo.x);
demo.Fun();
demo.add(1,2);