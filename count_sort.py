def count_sort(A):
    max_num = max(A)
    min_num = min(A)
    range_num = max_num - min_num + 1

    count = [0] * range_num

   
    for num in A:
        count[num - min_num] += 1
    sorted_array = []
    for i in range(range_num):
        while count[i] > 0:
            sorted_array.append(i + min_num)
            count[i] -= 1

    return sorted_array
A = list(map(int, input().split()))
print(count_sort(A))
