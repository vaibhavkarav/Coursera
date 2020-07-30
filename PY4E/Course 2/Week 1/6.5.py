text = "X-DSPAM-Confidence:    0.8475";
num = text.find('0')
num1 = text[num:]
print(float(num1))