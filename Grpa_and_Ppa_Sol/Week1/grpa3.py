def odd_one(L):
    int_counter = 0
    float_counter = 0
    str_counter = 0
    bool_counter = 0
    for i in L:
        if type(i) == int:
            int_counter += 1
        elif type(i) == float:
            float_counter += 1
        elif type(i) == str:
            str_counter += 1
        elif type(i) == bool:
            bool_counter += 1
    if int_counter==1:
        return "int"
    if float_counter==1:
        return "float"
    if str_counter==1:
        return "str"
    if bool_counter==1:
        return "bool"

if __name__ == '__main__':
    print(odd_one(eval(input().strip())))