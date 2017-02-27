
n = int(raw_input().strip())
arr = [int(arr_temp) for arr_temp in raw_input().strip().split(' ')]
negatives = 0
positives = 0
zeroes = 0
for val in arr:
    if val==0:
        zeroes+=1
    elif val<1:
        negatives+=1
    elif val>0:
        positives+=1
print(float(positives/n))
print(float(negatives/n))
print(float(zeroes/n))