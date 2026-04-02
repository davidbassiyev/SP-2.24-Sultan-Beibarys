# a = input()
# a = a.split()
# a = list(a)
# b = []
# for i in a:
#     if int(i) % 2 == 0:
#         b.append(int(i) * 2)
# print(*b)


# a = input()
# b = a[0]
# c = a[0]
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         c += a[i]
#     else:
#         c = a[i]

#     if len(c) > len(b):
#         b = c
# print(b)

a = input().split()
c = []
for i in a:
    if i in c:
        continue
    b = a.count(i)
    print(i, "=", b)
    c.append(i)

# a = input().split()
# b = ""
# for i in a:
#     if len(i) > len(b):
#         b = i
# print(b)

# a = input()
# b = ""
# for i in range(len(a)):
#     if a[i] in "1234567890":
#         b += a[i]
# if b == "":
#     print(0)
# else:
#     print(b)
