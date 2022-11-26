from functools import lru_cache

@lru_cache
def f(x):
  if x == 0:
    return 100
  elif x == 1:
    return 100
  elif x == 2:
    return 200
  return f(x-1)+f(x-2)+f(x-3)

print(f(19))