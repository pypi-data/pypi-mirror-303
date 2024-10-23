import re

def convert_num_th_to_global(number_th):
    thai_to_arabic = {'๐': '0', '๑': '1', '๒': '2', '๓': '3', '๔': '4', '๕': '5', '๖': '6', '๗': '7', '๘': '8', '๙': '9'}
    new_number = ''
    for number in number_th:
        if number in thai_to_arabic:
            new_number += thai_to_arabic[number]
        else:
            new_number += number
    return new_number



def verify_thai_number(input_string):
    thai_digit_pattern = r'^[\u0E50-\u0E59]+$'
    return bool(re.match(thai_digit_pattern, input_string))