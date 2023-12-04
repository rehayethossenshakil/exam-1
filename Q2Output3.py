y = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
x = []
q = []
p = []
r = []
for i in y:
    for j in i:
        if(1<=j and j<=4):
         z = j
         x.append(z)
        else:
          if(4<j and j<=8):
           w = j
           q.append(w)
          elif(j==9):
             b = j
             p.append(b)
          elif(10<=j and j<=12):
             c = j - 10
             p.append(c)
          elif(13<=j and j<=16):
             d = j - 10
             r.append(d)
          else:
              print("The input", j , "is not the given list")
rr = [x , q, p, r]
em = []
for k in rr:
   sum = 0
   for m in k:
      sum = sum + m
   em.append(sum)
print(em)