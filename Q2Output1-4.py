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
              print("The input", j , "is not in the given list")
rr = [x , q, p, r]
print()
print("Output-1:" , rr)
aa =[]
bb =[]
cc=[]
dd=[]
for lm in y:
   for ip in lm:
      if(ip%2!=0 and 1<=ip and ip<=4):
         aa1 = "Odd"
         aa.append(aa1)
      else:
         if(ip%2==0 and 1<=ip and ip<=4):
            aa2 = "Even"
            aa.append(aa2)
         elif(ip%2!=0 and 5<=ip and ip<=8):
            bb1 = "Odd"
            bb.append(bb1)
         elif(ip%2==0 and 5<=ip and ip<=8):
            bb2 = "Even"
            bb.append(bb2)
         elif(ip%2!=0 and 9<=ip and ip<=12):
            cc1 = "Odd"
            cc.append(cc1)
         elif(ip%2==0 and 9<=ip and ip<=12):
            cc2 = "Even"
            cc.append(cc2)
         elif(ip%2!=0 and 13<=ip and ip<=16):
            dd1 = "Odd"
            dd.append(dd1)
         elif(ip%2==0 and 13<=ip and ip<=16):
            dd2 = "Even"
            dd.append(dd2)
         else:
            print("The input", ip, "is not in the given list")
print()
print("Output-2:" ,aa, bb, cc, dd)

em = []
for k in rr:
   sum = 0
   for m in k:
      sum = sum + m
   em.append(sum)
print()
print("Output-3:" , em)
print()
tt = []
for mk in em:
   if(mk%2==0):
      mk = "Even"
      tt.append(mk)
   else:
      mk = "Odd"
      tt.append(mk)
print( "Output-4:",tt)
print()