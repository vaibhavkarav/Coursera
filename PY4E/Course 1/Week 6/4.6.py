def computepay(h,r):
    if h>40:
    	hr = h-40
    	rt = r*1.5
    	pay = hr*rt
    	return (40*r)+pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
p = computepay(h,r)

print("Pay",p)