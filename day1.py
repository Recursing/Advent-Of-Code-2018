from itertools import accumulate, chain
nums = list(map(int,open('data.txt','r').readlines()))
print(sum(nums))
s = set()
for t in accumulate(nums * 1000):
    if t in s:
            print(t)
            break
    s.add(t)
