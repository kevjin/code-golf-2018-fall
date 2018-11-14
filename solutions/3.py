t=input();a=[]
for i in range(t-1):
 l=raw_input();k=input();a.append(sorted(l.split())[k-1])
print("\n".join(a))