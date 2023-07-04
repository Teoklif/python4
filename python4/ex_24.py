N = int(input())
a = int(input())
array  = []
for i in range(N):
    number = i + 1
    array.append(number)

bush_number = int(input())
if bush_number > N or bush_number < 1:
    print(f'нет такого кол-ва кустов')
else: 
    if bush_number-1 < 0:
        j = N
    else:
        j = bush_number-1
        
        if bush_number+1 > N:
            j2 = 1
        else:
            j2 = bush_number+1


        max_berries = a*bush_number + a*j + a*j2



print(f'{array}')
print(f'{max_berries}')

 

