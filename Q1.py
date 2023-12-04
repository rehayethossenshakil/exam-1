a = [2, 4, 4, 4, 5, 5, 7, 9]
def custom_len(z):
    count = 0
    for i in z:
        count = count + 1
    return(count)
n = custom_len(a)
sum = 0
for x in a:
    sum = sum + x
x̄ = sum/n
sum2 = 0
for xi in a:
    y = (xi - x̄)**2
    sum2 = sum2 + y
sd = (sum2/(n - 1))**0.5
print(sd)

