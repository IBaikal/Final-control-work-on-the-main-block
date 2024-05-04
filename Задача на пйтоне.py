def create_new_array(arr):
    new_arr = []
    for x in arr:
        if len(x) <= 3:
            new_arr.append(x)
    return new_arr

if __name__ == '__main__':
    arr = input("Введите строки через пробел: ").split()
    print(create_new_array(arr))