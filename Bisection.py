def bisection(sorted_list, target):
    first_index = 0
    last_index = len(sorted_list) - 1
    while first_index != last_index:
        middle_index = int((first_index + last_index) / 2)
        if target == sorted_list[middle_index]:
            print 'This is immediate find'
            break
        elif target < sorted_list[middle_index]:
            last_index = middle_index
            print 'last index = %s' % last_index
        elif target > sorted_list[middle_index]:
            first_index = middle_index
            print 'first index = %s' % first_index
        else:
            middle_index = None
            break
    # if sorted_list[middle_index] == target:
    #     index = middle_index
    # else:
    #     index = None

    return middle_index

d = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
# for i in range(20):
#     d.append('%s') % i
print(d)
result = bisection(d, '16')
print(result)
