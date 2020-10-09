import os
import re


def count_occurrences_of_string(search_string, input_file_path):
    _in_str = search_string
    _in_str_pat = re.compile(_in_str)
    _in_str_len = len(_in_str)
    result = 0
    line_nbr = 0
    with open(input_file_path, 'r') as input_file_ob:
        for line in input_file_ob.readlines():
            line_nbr += 1
            match_list = re.findall(_in_str_pat, line)
            if len(match_list) > 0:
                result = result + len(match_list)
                print("Current line_number= {} and count = {}".format(line_nbr, result))
    return result


def count_occurrence_in_dir(search_string, input_dir_path):
    total_count = 0
    for cur_dir, dirs, files in os.walk(input_dir_path):
        for input_file in files:
            print("Reading file = {}".format(input_file))
            input_file_path = os.path.join(cur_dir, input_file)
            count_in_file = count_occurrences_of_string(search_string, input_file_path)
            if count_in_file > 0:
                total_count = total_count + count_in_file
            else:
                print("\t No match for {} found in this file".format(search_string))
    else:
        return total_count


if __name__ == "__main__":
    # input_directory = r"D:\D_drive_BACKUP\MENTOR\Utility\Search_a_string\840426_OUT"
    # input_file = r"D:\D_drive_BACKUP\MENTOR\Utility\Search_a_string\840426_OUT\EmilGeoDump_200914T120001_200914T121459_840426.bin.gz_decoded_0.txt"
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Please provide the Search-String and then search_directory_path")
    parser.add_argument("search_string", help="Please provide string you are searching for")
    parser.add_argument("input_dir", help="Please provide search_directory")
    arguments = parser.parse_args()
    search_string = arguments.search_string
    input_directory = arguments.input_dir
    print("Searching for " + search_string)
    string_count = count_occurrence_in_dir(search_string, input_directory)
    print("Total count = {}".format(string_count))
