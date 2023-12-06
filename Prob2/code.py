# Create some kind of dp which return minimu cost. It must take the list and some kind of index to work
import sys 
sys.setrecursionlimit(99999999)

memo = dict()

def f(i):
  if i >= n - 3:
    return list_n[i]
  else:
    if memo.get(i, -1) != -1:
      return memo[i]
    else:
      val = list_n[i] + min(f(i + 1), f(i + 2), f(i + 3))
      memo[i] = val
      return val

n = int(input())
list_n = list(map(int, input().split()))

if n >= 4:
  print(min(f(0), f(1), f(2)))
else:
  print(min(list_n))
