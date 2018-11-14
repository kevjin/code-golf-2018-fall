for i in range(1,999999):
 if (i%3==0 or i%5==0 or i%7==0) and str(i)[0]==str(i)[-1]:
  print(i)