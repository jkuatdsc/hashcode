import re

def read_data():
    """
    Function to read data from a file line by line while removing the new lines.
    """
    data = []
    with open("b_read_on.txt", "r+") as file:
        i = 0
        while True:
            file_data = file.readline()
            data.append(file_data.replace("\n", ''))
            if file_data == '':
                break
        i += 1
    return data


def filter_data():
    """
    Remove the first two rows from the data
    """
    file_data = read_data()
    data = lambda x : [x for x in file_data]
    my_data = data(file_data)
    filtered_data = my_data[2:]
    return filtered_data


def get_highest_signup(even_indice_list, n):
    """
    Split an array into multiple arrays and get the largest value of the arrays[1] value (signup time)
    """
    # NB: This function does NOT function as expected, help fix it :)
    max = even_indice_list[0]
    for i in range(1, n):
        if even_indice_list[i] > max:
            max = even_indice_list[i]
    return max  



def get_highest_signup_days():
    """
    Remove all spaces before, between and after values. Only filter out even indices and push their value 
    to a new array (even indices represent the libraries).
    get the highest library signup time and return it's value
    """
    # NB: This function also has some bugs, works partially
    new_data = []
    data = filter_data()
    unspaced_data = ([re.sub('\s+', ' ', i).strip() for i in data if i is not ''][:-1])
    # print(unspaced_data)
    int_data = [str(i) for i in unspaced_data]
    even_indices = []
    for i in int_data:
        if int_data.index(i) % 2 == 0:
            even_indices.append(i)
    print(f'The number of libraries is {len(even_indices)}')
    highest_signup_days = get_highest_signup(even_indices, len(even_indices))
    highest_signup_days = list(str(highest_signup_days))
    hsd = ''.join([re.sub( '\s+','', i) for i in highest_signup_days])
    print(str(hsd)[1])

    return str(hsd)[1]


# Run all the functions
if __name__ == "__main__":
    data = filter_data()
    filter_data()
    get_highest_signup_days()
