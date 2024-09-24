#SET

original_numbers = {1,2,3,4,5}
new_numbers = {4,5,6,7}
print(id(original_numbers))
original_numbers.update(new_numbers)
print(original_numbers)
print(id(original_numbers))

#original_numbers[0] = 7

numbers_list = [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3]
numbers_list =list(set(numbers_list))
print(numbers_list)


#items assignment

original_numbers.add(78)
print(original_numbers)
#item removal
original_numbers.remove(78)
#original_numbers.clear()
original_numbers = {1,2,3,4,5}
new_numbers = {4,5,6,7}
intersection = original_numbers.intersection(new_numbers)
print(intersection)


#FROZENSET
my_dict = {}
my_set = frozenset([1, 2, 3])
print(my_set)

#immutability-re van szükség, de mégis kell hogy set legyen, például ne lehessen benne tárolni duplikátumokat
#példa, blog post tag-ek. miután létrejött egy blog post és hozzá lettek adva a tag-ek, nem akarjuk véletlen sem megváltoztatni, és tutira is akarunk menni hogy 2 tag nem szerepel többször.
