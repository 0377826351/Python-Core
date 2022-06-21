from collections import deque,defaultdict,Counter

# #stack right
# stack = deque([])
# #append right
# stack.append(3)
# stack.append(2)
# stack.append(1)
# print(stack)

# #pop right
# res = stack.pop()
# print(stack)
# print(res)

#Stack left
# stack = deque([])
# stack.appendleft(1)
# stack.appendleft(2)
# stack.appendleft(3)
# print(stack)

# res = stack.popleft()
# print(stack)
# print(res)

# #Queue (append-popleft,appendleft - pop)
# que = deque([]) 
# que.append(3)
# que.append(2)
# que.append(1)
# print(que)

# res = que.popleft()
# print(que)
# print(res)


# # Defaultdict
# st = defaultdict(lambda :'Không xác định')
# st['Code'] = 'PY0001'
# st['FullName'] = 'Cumingg'

# print(st['FullName'])
# print(st['Code'])
# print([st['Sex']])

#counter
#thủ công
# list1 = ['x','y','z','x','x','y']
# dict = {}
# for i in list1:
#     if i not in dict:
#         dict[i] = 1
#     else:
#         dict[i] += 1

# #counter
# dict2 = Counter(list1)
# print(dict2)
