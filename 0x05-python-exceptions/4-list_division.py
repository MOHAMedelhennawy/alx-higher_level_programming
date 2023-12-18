#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    div = 0
    i = 0
    for i in range(0, list_length):
        try:
            div = (my_list_1[i] / my_list_2[i])
        except(ZeroDivisionError):
            div = 0
            print("division by 0")
        except(TypeError):
            div = 0
            print("wrong type")
        except(IndexError):
            div = 0
            print("out of range")
        finally:
            new_list.append(div)
    return(new_list)
