def count_ants(input_string):
    count = 0
    for i in range(len(input_string) - 2):  
        if input_string[i].lower() == 'a' and input_string[i + 2].lower() == 't':
            count += 1            
    return count

input_string = 'Antandart'
print(f"String= '{input_string}', Count= {count_ants(input_string)}")
