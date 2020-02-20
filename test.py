def get_data():
    with open("a_example.txt", "r+") as file:
        data_obj = {}
        lines = []
        data = []
        i = 0
        while True:
            d = {'line':'data'}
            name = "line_" + str(i)
            lines.append(name)
            file_data = file.readline()
            data.append(file_data.replace("\n", ''))
            
            if file_data == "":
                break
            i += 1
        data = dict(zip(lines, data))
    return data

def first_lib(data):
    name = ""
    key = 2
    value = 0
    data 
    for k, v in data.items():
        print(f'{k} : {v}')
        line = "line_" + str(key)
        if k == line:
            list_of_values = v.split(" ")
            # print(list_of_values[1])
            if int(value) < int(list_of_values[1]):
                name = k
    print(name)
        


# print(data)

# with open("a_out.txt" , "w+") as file:
#     file.write(data)
if __name__ == "__main__":
    data = get_data()
    first_lib(data)
