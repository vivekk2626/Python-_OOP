def smartsub(a,b):
	print(a-b);

def smartsub(fptr):

	def inner(a,b):
		if(a<b):
			a,b=b,a;
		return fptr(a,b); # yane value return hote swap houn ani sub la jate 

	return inner;		




sub=smartsub(sub);	

sub(6,8);
	