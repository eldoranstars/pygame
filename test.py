bicycles = [ 'trek', 'cannondale', 'redline', 'redline', 'cannondale', 'redline', 'specialized']

list_bicycles = []
for bicycle in bicycles:
    if bicycle not in list_bicycles:
        list_bicycles.append(bicycle)
        print(bicycle)



# length_bicycle = len(list_bicycles)

# for i in range(len(list_bicycles)):
#     count = 0
#     for bicycle in bicycles:
#         if bicycle == list_bicycles[i]:
#             count += 1
#     print(list_bicycles[i] + ':' + str(count))