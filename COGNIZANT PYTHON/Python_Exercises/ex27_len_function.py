# Exercise 27 - Len Function

def string_length(text):

    if text.strip() == "":
        print("Empty String")
        return

    print("Length:", len(text))


string_length("Python")