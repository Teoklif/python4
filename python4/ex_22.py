N = int(input())
array_N  = list(map(int, input().split()))
M = int(input())
array_M  = list(map(int, input().split()))
final_array = list(set(sorted(list(array_N + array_M))))

print (f'{final_array}')
        