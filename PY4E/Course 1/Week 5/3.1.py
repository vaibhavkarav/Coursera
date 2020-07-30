hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

if h>40 :
	hr = h-40

rt = r*1.5
pay = hr*rt
gpay = 40*r+pay

print(gpay)