'''
Week I Exercise I - a
'''

num_v = 0
for i in range(len(s)):
    if (s[i] == 'a') | (s[i] == 'e') | (s[i] == 'i') | (s[i] == 'o') | (s[i] == 'u'):
        num_v += 1
print(num_v)