temp = ''
array_ = []
for i in range(0, len(s)-1):
    if s[i] <= s[i+1]:
        if len(temp) == 0:
            temp += s[i]
        temp += s[i+1]
        array_.append(temp)
    else:
        temp = ''
if len(array_) == 0:
    print('Longest substring in alphabetical order is: {}'.format(s[0]))
else:
    answer = [x for x in array_ if len(x) == len(max(array_, key=len))]
    print('Longest substring in alphabetical order is: {}'.format(answer[0]))