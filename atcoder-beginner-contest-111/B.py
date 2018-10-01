N = int(input())
if N % 111 == 0:
  print(N)
else:
  for i in range(N, 1000):
    if i % 111 == 0:
      print(i)
      break
