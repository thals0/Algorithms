n, k = map(int, input().split())
count = 0

## 단순 방법 답안
while n != 1:
  if n%k == 0:
    n = n//k
    count += 1
  else:
    n = n-1
    count += 1

print(count)

## 시간복잡도를 생각한 답안
# while True:
#   # (N==K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
#   target = (n//k)*k
#   count += (n-target)
#   n = target

#   if n<k:
#     break
#   # K로 나누기
#   count += 1
#   n//=k
# # 마지막으로 남은 수에 대하여 1씩 빼기 
# count += (n-1)
# print(count)