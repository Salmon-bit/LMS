dark_honey = 0
light_honey = 0

nums = list(map(int, input().split()))

for n in nums:
    if n % 2 == 0:
        light_honey += n
    else:
        dark_honey += n

print(f"Тёмного мёда: {dark_honey}.")
print(f"Светлого мёда: {light_honey}.")
