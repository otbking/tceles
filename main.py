import math;

day = 0;
distance = 0;

#Convert astronomical unit to meters.
def aumeter(a):
	return 1.496E11*a;

#TODO
#Don't understand this yet, may not be implemented correctly.
#We can always get distance some other way, as long as we have something to work with for now.
#Returns earth's distance vector?
#What is D?
#Spencer JW (1971)
#variable d is the day of the year: January 1 = 0, December 31 = 364
#disregard leap years.

def spencer(d):
	D = 1; 
	T = 2 * math.pi * D * d / 365;
	f1 = 1.000110;
	f2 = 0.034221 * math.cos(T);
	f3 = 0.001280 * math.sin(T);
	f4 = 0.000719 * math.cos(2*T);
	f5 = 0.000077 * math.sin(2*T);
	return math.sqrt(1./(f1+f2+f3+f4+f5));

def main():
	a = spencer(0);		#January 1st
	b = spencer(78);	#March Equinox
	c = spencer(170);	#June Solstice
	d = spencer(264);	#September Equinox
	e = spencer(354);	#December Solstice
	f = spencer(365);	#December 31st
	foo = [a, b, c, d, e, f];
	goo = [];
	for i in foo:
		goo.append(aumeter(i));
	print(foo);
	print(goo);
	return 0;

main();
