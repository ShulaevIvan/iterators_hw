nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None, [1, 2, None,[1, 2, None, ] ]],

]

# # #Базовый генератор

# def flat_generator(array):
#     for arr in array:
#         for i in arr:
#             yield i


def flat_generator(array):

    test_list = True
    while test_list:
        tmp_arr = []
        test_list = False
        for i in array:
            if isinstance(i, list):
                tmp_arr.extend(i)
                test_list = True
            else:
                tmp_arr.append(i)
        array = tmp_arr
    for i in array:
        yield i
    

if __name__ == '__main__':
    
    for item in  flat_generator(nested_list):
        print(item)