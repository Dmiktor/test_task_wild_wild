
def spec_remove_elem_by_value(param):
    mas_res = [1, 2, 555, 'None', {"key": "None"}, 555, "None", ["ooo", 12], "None", 555, 'None', 555, None, 1234,
               {"key": "None"}]
    
    length = len(mas_res)
    offset = 0
    c = 0

    for i in range(length):
        if param == mas_res[i-offset] or param in str(mas_res[i-offset]):
            c += 1
            if c == 2:
                continue
            mas_res.pop(i-offset)
            offset += 1
        
    print(mas_res)

if __name__ == "__main__":
    spec_remove_elem_by_value('555')