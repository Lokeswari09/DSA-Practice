nums = list(map(int, input().split()))
freq = {}
for i in nums:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
result = []
for key, value in freq.items():
    result.append([key, value])
print(result)