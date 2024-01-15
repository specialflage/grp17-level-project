print('-----------Example library-----------')
book_dict = {"pages": "277", "name": "Gone Girl", "year": 2007}
print(book_dict)
print('-----------Adding Elements To a Dictionary-----------')
# "Author": "Well Max"
book_dict["Author"] = "Well Max"
print(book_dict)
print('-----------Accessing Elements inside a Dictionary-----------')
# Gone Girl
book_name = book_dict["name"]
print(book_name)
print('-----------Changing Elements inside a Dictionary -----------')
# 2007 to 2010
book_dict['year'] = 2010
print(book_dict)
print('-----------Using loop to print keys and values----?????????-------')
for key, value in book_dict.items():
    print(key, value)
'''print("------different for loop-----")
for items in book_dict:
    print(items, book_dict[items])'''
print('-----------Removing item from a Dictionary-----------')
# Exclude name : gone girl
book_dict.pop("name")
print(book_dict)