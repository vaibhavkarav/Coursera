score = input("Enter Score: ")
sc = float(score)
try:
	if sc<1.0:
		sc = float(score)
except:
	print("Enter a valid score")
if sc >= 0.9:
	print('A')
elif sc >= 0.8:
	print('B')
elif sc >= 0.7:
	print('C')
elif sc >= 0.6:
	print('D')
else:
	print('F')