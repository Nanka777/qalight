# # lst = [1, 2, 3]
# # lst2 = lst.copy()
# #
# # print(lst)
# # print(lst2)
# #
# # lst3 = [[[1, 1], [2, 2]], [3, 4], [5, 6]]
# # lst4 = lst3.copy()
# # print(lst4)
#
# # SET
# # string = 'sdgasdgdag'
# # x = set(string)
# #
# # lst1 = [1, 2, 3, 4, 5]
# # lst2 = [5, 4, 5, 2, 1]
# #
# # print(set(lst1) == set(lst2))
# #
# # print(len(set(lst1)))
#
#
# # lst = [1, 2, 3, 4]
# # print(5 in lst)
#
# # s1 = {1, 2, 3, 4, 5}
# # s2 = {1, 2, 3, 4, 6}
# # print(s2.difference(s1))
# # s1.remove(5)
# # s1.discard(6)
# # s1.clear()
# # print(s1)
#
# # s2 = frozenset(s1)
# # print(s2)
#
# keys = ['one', 'two', 'three']
# values = [1, 2, 3]
#
# for obj in zip(keys, values):
#     print(obj)
# #
# # another_dict = {'four': 4, 'five': 5}
# # dictionary.update(another_dict)
# #
# # print(dictionary)
#
# # for i in range(10):
# #     print(i)
# #
# # words = ['one', 'two', 'three']
# # for x in words:
# #     print(x)
# #

lst = [25, 17, 32, 1]
mx = max(lst)
mn = min(lst)
mx_index = lst.index(mx)
mn_index = lst.index(mn)
lst[mx_index] = mn
lst[mn_index] = mx
print(lst)

tpl = ()

# tup = (1, 2, 3)
# tup2 = None
# print(type(tup2))
# try:
#     tup2 = tup
#     tup2[0] = 5
# except TypeError:
#     print('Все добре, помилка виникла')
# else:
#     print('Помилки не виникло, все погано')
# finally:
#     print('А я взагалі завжди виконуюсь')
#
# assert tup2 == tup