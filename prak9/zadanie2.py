def list_tuple_dict(name, age, city):
    data_list = [name, age, city]
    data_tuple = (name, age, city)
    data_dict = {'name': name, 'age': age, 'city': city}
    return data_list, data_tuple, data_dict
result_list, result_tuple, result_dict = list_tuple_dict("Alice", 25, "New York")
print(result_list)  
print(result_tuple)  
print(result_dict) 