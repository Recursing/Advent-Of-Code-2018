from collections import Counter
lines = open('data.txt','r').readlines()

print(sum(3 in set(Counter(l).values()) for l in lines) *
      sum(2 in set(Counter(l).values()) for l in lines))

removed = [[l[:i]+l[i+1:] for l in lines] for i in range(26)]
counts = (Counter(r).most_common(1)[0] for r in removed)
print(next(line for line,count in counts if count == 2))

#oneliner for fun
print(next(line for line,count in (Counter([l[:i]+l[i+1:] for l in lines]).most_common(1)[0] for i in range(26)) if count == 2))
