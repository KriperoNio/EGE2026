pass # 1) x z w y
# for x in [0,1]:
#     for y in [0, 1]:
#         for z in [0, 1]:
#             for w in [0, 1]:
#                 if ((not(x <= z)) or (y == w) or y) == 0:
#                     print(x, y, z, w)
pass # 3) z x y w
# for x in [0,1]:
#     for y in [0, 1]:
#         for z in [0, 1]:
#             for w in [0, 1]:
#                 if (((x <= z) <= y) or (not w)) == 0:
#                     print(x, y, z, w)
#
pass # 4) z y w x
# for x in [0,1]:
#     for y in [0, 1]:
#         for z in [0, 1]:
#             for w in [0, 1]:
#                 if ((x and y) or (y == z) or w) == 0:
#                     print(x, y, z, w)
pass # 5) w y x z
# for x in [0,1]:
#     for y in [0, 1]:
#         for z in [0, 1]:
#             for w in [0, 1]:
#                 if (x or (not y)) and (not(x == z)) and (not w):
#                     print(x, y, z, w)
pass # 6) z y w x
# from itertools import product, permutations
#
# def f(x,y,z,w):
#     return (x and (not y)) or (x == z) or w
#
# for a1,a2,a3,a4,a5,a6,a7 in product([0,1],repeat=7):
#     t=[(1,a1,a2,a3),(1,1,a4,a5),(a6,1,a7,1)]
#     if len(t)==len(set(t)):
#         for p in permutations('xyzw'):
#             if [f(**dict(zip(p,r))) for r in t]==[0,0,0]:
#                 print(p)
pass # 25) z y x w
# from itertools import product, permutations
#
# def f (x, y, z, w):
#     return (x or y) and (not(y == z)) and (not w)
#
# for a1, a2, a3, a4 in product([0,1], repeat=4):
#     t = [(1, a1, 1, a2), (0, 1, a3, 0), (a4, 1, 1, 0)]
#     if(len(t)) == len(set(t)):
#         for p in permutations('xyzw'):
#             if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
#                 print(''.join(p))