from DataStructures.List.list_node import new_single_node


def new_list():
    new_list ={
    "first": None,
    "last": None,
    "size": 0,
    }
    return new_list  

def add_first(my_list, element):
    node = new_single_node(element)
    if my_list["first"] is None:
        my_list["first"] = node
        my_list["last"] = node
    else:
        node["next"] = my_list["first"]
        my_list["first"] = node
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    node = new_single_node(element)
    if my_list["first"] is None:
        my_list["first"] = node
        my_list["last"] = node
    else:
        my_list["last"]["next"] = node
        my_list["last"] = node
    my_list["size"] += 1
    return my_list
def size(my_list):

    return my_list["size"]

def first_element(my_list):
    return my_list["first"]["info"]

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]
def is_present(my_list,element,cmp_funcion):
    is_in_array = False
    temp=my_list["first"]
    count=0
    while temp is not None and not is_in_array:
        if cmp_funcion(temp["info"],element)==0:
            is_in_array=True
        else:
            temp=temp["next"]
            count+=1
    if not is_in_array:
        count=-1
    return count
