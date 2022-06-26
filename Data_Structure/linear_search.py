def linear_search(lt, num):
    flag = False

    for index, element in enumerate(lt):
        if element == num:
            flag = True
            break
    
    if flag == True:
        print('Element Present At {}'.format(index))
    else:
        print('Element Not Found')

lt = [23, 45, 12, 4, 89, 64, 10, 4]
searched_element = 4
linear_search(lt, searched_element)