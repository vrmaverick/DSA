def recursive_reverse_string (str):
    if len(str) == 2:
        print(f"Base hit {str}")
        return str[-1]+str[0]
    
    return str[-1]+recursive_reverse_string(str[0:-1])


if __name__ == '__main__':
    st = recursive_reverse_string('Vedant')
    print(st)

# string = 'Vedant'

# print(string[-1]+string[0])