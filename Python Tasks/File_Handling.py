def printtable(n):
   table = ""
   for i in range(1,11) :
    table += (f"{n} X {i} = {n*i}\n")
   
   f = open(f"Tables/table_{n}","w")
   f.write(table)
    
for i in range(2,21):
    printtable(i)