n = int(input("N: "))

num_points_circle = 0
num_points_total = 0

x = [x/n for x in range(n + 1)]
y = [y/n for y in range(n + 1)]
#print(x)
#print(y)
for i in range(n+1):
    for j in range(n+1):
        distance = x[i]**2 + y[j]**2
        if(distance <= 1):
            num_points_circle += 1
        num_points_total += 1
    
pi_estimation = 4* num_points_circle/num_points_total
print(pi_estimation)
print(num_points_circle)
print(num_points_total)