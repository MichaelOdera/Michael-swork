def data_type(grey):
    if type(grey) == bool: 
    # This checks if the element entered is boolean 
        return grey
    elif type(grey) == int:
    # This checks if "grey" is an integer
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
        # This returns no vslue reply if the result is not a string
        return "no value"