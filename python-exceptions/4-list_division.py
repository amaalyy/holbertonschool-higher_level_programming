#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):

        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise (IndexError)

            elif (type(my_list_1[i]) not in (int, float) or
                  type(my_list_2[i]) not in (int, float)):
                raise (TypeError)

            elif my_list_2[i] == 0:
                raise (ZeroDivisionError)

            result_list.append(my_list_1[i] / my_list_2[i])

        except IndexError:
            print("out of range")
            result_list.append(0)
        except TypeError:
            print("wrong type")
            result_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result_list.append(0)

        finally:
            pass

    return (result_list)
