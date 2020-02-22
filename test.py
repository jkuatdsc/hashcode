import re

def read_data():
    """
    Function to read data from a file line by line while removing the new lines.
    """
    data = []
    # Read file data
    with open("b_read_on.txt", "r+") as file:
        i = 0
        while True:
            file_data = file.readline()
            data.append(file_data.replace("\n", '')) #Remove newlines
            if file_data == '':
                break
        i += 1
    return data


def filter_data():
    """
    Remove the first two rows from the data
    """
    file_data = read_data()

    # Loop through the file data and append it to an array
    data = lambda x : [x for x in file_data]
    my_data = data(file_data)

    # Ignore the leading 2 lines of the data
    filtered_data = my_data[2:]
    return filtered_data



def check_highest_second_index(some_list):
    """
    A function to get the largest signup days by checking which is the largest value
    on index[1] of every array element
    """
    # Remove all spaces from the list elements
    list_with_no_spaces = [i.replace(' ', ',') for i in some_list]
    print(list_with_no_spaces)

    list_of_lists = []
    counter = 0
    for i in list_with_no_spaces:
        if int(i[2]) > counter:
            counter = int(i[2])
    return counter
        




def get_highest_signup_days():
    """
    Remove all spaces before, between and after values. 
    Filter out even indices and push their value to a new array (even indices represent the libraries).
    """

    # NB: This function also has some bugs, works partially
    new_data = []
    data = filter_data()
    unspaced_data = ([re.sub('\s+', ' ', i).strip() for i in data if i is not ''][:-1]) #Remove spaces
    int_data = [str(i) for i in unspaced_data] #Convert array values to integers
    even_indices = []
    for i in int_data:
        if int_data.index(i) % 2 == 0: #Get even indices
            even_indices.append(i)
    print(even_indices)
    highest_signup_days = check_highest_second_index(even_indices)
    
    print('\n')
    print(f'The number of libraries is : {len(even_indices)}')
    print(f'The highest signup days is : {highest_signup_days}')
 

# Run all the functions 
if __name__ == "__main__":
    data = filter_data()
    get_highest_signup_days()
