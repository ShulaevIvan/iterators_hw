from pprint import pprint

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

class FlatIterator:
    
    def __init__(self, arr):
        self.arr = arr
        self.start = -1
        self.end = 0
        for mass in arr:
            count = len(mass)
            self.end += count
        self.inner_counter = -1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.start += 1
        g = self.result()
        if self.start == self.end:
            raise StopIteration
        
        for arr in g:
            for i in arr:
                self.inner_counter += 1
                return arr[self.inner_counter]
                
    def result(self):
       g = [j for i in self.arr for j in i]
       yield g

    
def flat_generator(arr):
    return [i for inner_arr in arr for i in inner_arr] 
    
            
 


flat_list = [item for item in FlatIterator(nested_list)]
pprint(flat_list)

print('<---------------------->')   
for item in FlatIterator(nested_list):
	print(item) # 
 
print('<---------------------->')    
for item in flat_generator(nested_list):
    print(item)
    
print('<---------------------->')   
      
