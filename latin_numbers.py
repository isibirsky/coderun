""" You are given a number written in Roman numerals. Get the same number in regular notation (in Arabic numerals).
The Roman notation of numbers may include the following characters:

’I’ — 1
’V’ — 5
’X’ — 10
’L’ — 50
’C’ — 100
’D’ — 500
’M’ — 1000
The numbers ’I’, ’X’, ’C’ and ’M’ cannot be used more than three times in a row. The digits ’V’, ’L’, and ’D’ cannot be used more than once in the entire number record.

The numbers are usually written in descending order from left to right. For example, the number 350 will be written as 'CCCL'.

However, there are exceptions:

To get a ’4’ or a ’9’, put an ’I’ in front of a ’V’ or an ’X’, respectively.
To get a ’40’ or ’90’, put an 'X’ in front of an ’L’ or ’C'.
To get ’400’ or ’900’, put ’C’ before ’D’ or ’M'. """

def to_arab_number(latin_number):
    latin_numbers = {   'I': 1, 
                        'V': 5, 
                        'X': 10, 
                        'L': 50, 
                        'C': 100, 
                        'D': 500, 
                        'M': 1000 }
    
    
    arab_number = []
    prev_latin_numeral = '' #previous Latin numeral in the record latin_number

    # The numbers ’I’, ’X’, ’C’ and ’M’ cannot be used more than three times in a row.
    if  latin_number.count("IIII")\
        or latin_number.count("XXXX")\
        or latin_number.count("CCCC")\
        or latin_number.count("MMMM"):
            return -1
    # The digits ’V’, ’L’, and ’D’ cannot be used more than once in the entire number record.
    if  latin_number.count("V") > 1\
        or latin_number.count("L") > 1\
        or latin_number.count("D") > 1:
            return -1

    for latin_numeral in latin_number:
        # The numerals are written in descending order from left to right
        if  not prev_latin_numeral\
            or latin_numbers[prev_latin_numeral] >= latin_numbers[latin_numeral]:
                arab_number.append(latin_numbers[latin_numeral])
        # otherwise let's check for the exceptional cases.
        elif  prev_latin_numeral in {'I', 'X', 'C'}\
            and latin_numbers[latin_numeral] // arab_number.pop() in {5, 10}:
                if arab_number and arab_number[-1] < latin_numbers[latin_numeral]:
                    return -1
                arab_number.append(latin_numbers[latin_numeral] - latin_numbers[prev_latin_numeral])
        else:
            return -1
        prev_latin_numeral = latin_numeral
    return sum(arab_number)

latin_number = input()
print(to_arab_number(latin_number))