pass # 1) 1891
# n=4*625**1920+4*125**1930-4*25**1940-3*5**1950-1960
# count=0
# while n>0:
#     if n%5==0:
#         count+=1
#     n//=5
# print(count)
pass # 2) 796
# n = 13*625**1320 + 12*125**1230 - 14*25**1140 - 13*5**1050 - 2500
# c = 0
# while n > 0:
#     if n % 25 == 0:
#         c += 1
#     n //= 25
# print(c)
pass # 5) 8767
# for x in ([str(i) for i in range(10)] + [chr(65 + i) for i in range(5)]):
#     n = int(f'123{x}5', base=15) + int(f'1{x}233', base=15)
#     if n % 14 == 0:
#         print(n//14)
pass # 6) 470402599
# for x in ([i for i in range(10)] + [chr(65 + i) for i in range(9)])[::-1]:
#     n = int(f'98{x}79641', base=19) + int(f'36{x}14', base=19) + int(f'73{x}4', base=19)
#     if n % 18 == 0:
#         print(n // 18)
#         break
pass # 11) 2024
# for x in range(2030, 0, -1):
#     n = 3**100 - x
#     c = 0
#     while n > 0:
#         if n % 3 == 0:
#             c += 1
#         n//=3
#     if c == 5:
#         print(x)
#         break
pass # 23) 72450445
# for x in ([i for i in range(10)] + [chr(65+i) for i in range(11)]):
#     n = int(f'82934{x}2', base=21) + int(f'2924{x}{x}7', base=21) + int(f'67564{x}8', base=21)
#     if n%20 == 0:
#         print(n//20)
#         break
