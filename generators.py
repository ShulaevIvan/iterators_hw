nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

def flat_generator(array):
    count = 0
    for num in array:
        count += 1

    for i in range(count):
        for j in array[i]:
            yield j
            

#Базовый генератор

# def flat_generator(array):
#     for arr in array:
#         for i in arr:
#             yield i



if __name__ == '__main__':
    
    for item in  flat_generator(nested_list):
        print(item)