import csv

def search_dictionary(dictionary, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
                    
    if key_column_index in dictionary:                
        searched_value = dictionary[key_column_index]
        
    return searched_value

  
def read_dictionary(filename):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    file_dict = {}
    KEY_INDEX = 0

    with open(filename, 'rt') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        # Iterates through each line that has been seperated into a list
        for row_list in reader:
            if row_list != 0:
                item_list = []
                # Finds and makes the key
                key = row_list[KEY_INDEX]
                # Adds info cooraleted to the key
                for item in row_list:
                    if item != key:
                        item_list.append(item)
                        file_dict[key] = item_list
    return file_dict

  
def main():
                                                        
    students_dict = read_dictionary('students.csv')
    i_number = str(input("Please input I Number: "))
    stalker = search_dictionary(students_dict, i_number)
    print(stalker[0])
    
if __name__ == '__main__':
  main()


