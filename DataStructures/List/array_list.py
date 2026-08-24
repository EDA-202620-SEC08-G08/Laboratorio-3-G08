def new_list(size):
    new_list ={
    "elements": [],
    "size":0,
    }
    
    return new_list

def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

def size(my_list):

    return my_list["size"]

def first_element(my_list):
    return my_list["elements"][0]
    