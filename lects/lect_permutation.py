from itertools import permutations
perm_str = input().split()
pem = input().split()

abc = list(permutations(perm_str[0], 2))
abc1 = [''.join(w) for w in abc]
for i in sorted(abc1):
    print(i, end="\n")
