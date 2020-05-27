from math import ceil

# #бинарный поиск
# a = [1,4,6,9,11,12,13,15,21,23,45,67]
# b=int(input())
# z=ceil(len(a)/2)
# q=0
# while q!=1:
#
#     if a[z]==b:
#         print(a[z])
#         q=q+1
#     else:
#         if b>=a[z]:
#             a=a[z:]
#             z = ceil(len(a)/2)
#         else:
#             a=a[:z]
#             z = ceil(len(a)/2)-1

# #сортировка выбором
#
# #наибольший элемент
# z = [2,1,3,9,3,1,6,7,4]
#
#
# def findmax(z):
#     highest = z[0]
#     for i in range(0, len(z)):
#         if z[i] > highest:
#             highest = z[i]
#
#     return z.index(highest)
#
# def sortchoice(z):
#     z1 = []
#     for i in range(0, len(z)):
#         z1.append(z[findmax(z)])
#         z.pop(findmax(z))
#     return z1
#
# print(sortchoice(z))