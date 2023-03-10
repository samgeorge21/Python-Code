def check_for_TODO(text):
    if type(text) is str:
        if "TODO" in text:
            return "The text includes TODO"
        else:
            return "The text does not include TODO"
    else:
        return "This function will only accept a string of text"