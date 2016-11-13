def data_type(grey):
    if type(grey) == bool:
        return grey
    elif type(grey) == int:
        if grey <100:
            return "less than 100"
        elif grey>100:
            return "more than 100"
        elif grey==100:
            return 'equal to 100'
    elif type(grey) == list:
        if len(grey) >= 3:
            return grey[2]
        else:
            return None
    if type(grey) == str:
        return len(grey)
    else:
        return "no value"