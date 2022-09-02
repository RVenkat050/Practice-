# a = [['A','Laptop'],['A','Laptop'],['A','Mouse'],['B','Laptop'],['A','Headset'],['B','Headset']]
# count_A = 0
# count_B = 0
# temp = []
# for i in a:
#     if i[0] == 'A':
#         count_A += 1
#     if i[0] == 'B':
#         count_B += 1
# temp.append([['A',count_A],['B',count_B]])
# print(temp)
# print([['A', 'Laptop',a.count(['A','Laptop'])],['A','Mouse',a.count(['A','Mouse'])],
#       ['B','Laptop',a.count(['B','Laptop'])],['A','Headset',a.count(['A','Headset'])],
    #   ['B','Headset',a.count(['B','Headset'])]])

# mylist = [['A', 'Laptop','CPU'], ['A', 'Laptop','CPU'], ['A', 'Mouse','CPU'], ['B', 'Laptop','CPU'], ['A','Headset','CPU'],
# ['B','Headset','CPU']]
# count={}
# print("Initial Count", count)
# for i in mylist:
#     print("i iteration at 21", i)
#     for j in i[0:3]:
#         print("j iteration at 23", j)
#         if j in count:
#             print(" if Count at 25", j)
#             count[j]+=1
#         else:
#             count[j]=1
#             print("Else  Count at 29", j)
# l=list(count.items())
# print(l)
# inp = [['A', 'Laptop'], ['A', 'Laptop'], ['A', 'Mouse'], ['B', 'Laptop'], ['A', 'Headset'], ['B', 'Headset']]
# # print(inp)
# lst = []
# lst1=[]
# lst2 = []
# out1 = []
# out2 = []
# for i in inp:
#     if (i[0] not in lst):
#         lst.append(i[0])
#         out1.append([i[0], 1])
#     else:
#         ind = lst.index(i[0])
#         out1[ind][1] = out1[ind][1] + 1

#     if (i[1] not in lst2):
#         lst2.append(i[1])


#     if i not in lst1:
#         lst1.append(i)
#         out2.append([i[0],i[1], 1])
#     else:
#         ind = lst1.index(i)
#         out2[ind][2] = out2[ind][2] + 1
# print(out2)
# lst.append(lst2)

# print(out1)
# print(lst)  # out3




# A = [1, 2, 3, 'ae']
# B = [1, 1, 'b', 6]
# C=[]
# count=0
# for i in range (len(A)):
#     if A[i]=='ae':
#         A[i]=0
#     if B[i]=='b':
#         B[i]=0
#     x=A[i]+B[i]
#     if x%2!=0:
#         x=0
#     C.append(x)
# print(C)
# A = [1, 2, 3, 'ae']
# B = [1, 1, 'b', 6]
# p=A+B
# count=0
# num=0
# ele=0
# for i in range (len(p)):
#     num=p.count(p[i])
#     if (num>count):
#         count=num
#         ele=i
# print(p[ele])


# #3


# l = [-10, 2, 3, -2, 0, 5, -15]


# def calMaxSum(l):
#     currsum = 0
#     maxsum = 0
#     for i in l:
#         maxsum = maxsum + i
#         maxsum = max(maxsum, 0)
#         currsum = max(currsum, maxsum)

#     return currsum