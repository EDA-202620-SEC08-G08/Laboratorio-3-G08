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
def is_empty(my_list):
    return my_list["size"] == 0
def last_element(my_list):
    return my_list["last"]["info"]
def delete_element(my_list, pos):
    if pos == 0:
        my_list["first"] = my_list["first"]["next"]
    else:
        searchpos = 0
        node = my_list["first"]
        while searchpos < pos - 1:
            node = node["next"]
            searchpos += 1
        node["next"] = node["next"]["next"]
    my_list["size"] -= 1
    return my_list
def remove_first(my_list):
    if my_list["first"] is not None:
        my_list["first"] = my_list["first"]["next"]
    if my_list["first"] is None:
        my_list["last"] = None
        my_list["size"] -= 1
    return my_list["size"]
def remove_last(my_list):
    if my_list["first"] is not None:
        if my_list["first"] == my_list["last"]:
            my_list["first"] = None
            my_list["last"] = None
        else:
            node = my_list["first"]
            while node["next"] != my_list["last"]:
                node = node["next"]
            node["next"] = None
            my_list["last"] = node
        my_list["size"] -= 1
    return my_list["size"]
def insert_element(my_list, pos, element):
    node = new_single_node(element)
    if pos <= 0 or my_list["first"] is None:
        node["next"] = my_list["first"]
        my_list["first"] = node
    if my_list["last"] is None:
        my_list["last"] = node
    elif pos >= my_list["size"]:
        my_list["last"]["next"] = node
        my_list["last"] = node
    else:
        searchpos = 0
        current_node = my_list["first"]
        while searchpos < pos - 1:
            current_node = current_node["next"]
            searchpos += 1
        node["next"] = current_node["next"]
        current_node["next"] = node
    my_list["size"] += 1
    return my_list
def change_info(my_list, pos, new_element):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    node["info"] = new_element
    return my_list
def exchange(my_list, pos1, pos2):
    if pos1 == pos2:
        return my_list
    searchpos1 = 0
    searchpos2 = 0
    node1 = my_list["first"]
    node2 = my_list["first"]
    while searchpos1 < pos1:
        node1 = node1["next"]
        searchpos1 += 1
    while searchpos2 < pos2:
        node2 = node2["next"]
        searchpos2 += 1
    temp_info = node1["info"]
    node1["info"] = node2["info"]
    node2["info"] = temp_info
    return my_list
def sub_list(my_list, pos1, pos2):
    sub_list = new_list()
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos1:
        node = node["next"]
        searchpos += 1
    while searchpos <= pos2:
        add_last(sub_list, node["info"])
        node = node["next"]
        searchpos += 1
    return sub_list
