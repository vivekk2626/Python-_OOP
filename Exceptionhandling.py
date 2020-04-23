print('********* Application For Exception handling ************');

no1=int(input("\nEnter the 1st number :"));
no2=int(input("\nEnter the 2nd number :"));

try:
	iret=no1/no2;
except ZeroDivisionError:
	print("\n*****Unable to divide by Zero ****** :")	
finally:
	print("\nRelease All Resources :")


