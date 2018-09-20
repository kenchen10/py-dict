def remove_first(word):
    #Removes the first letter of a word
    return word[1:]

def is_word(word, dictionary):
    #Finds out if word is in the dictionary
    if word in dictionary:
        return True
    return False

def same_first(w1, w2):
    #Checks if 2 words have the same first letter
    if starts_with(w1) == starts_with(w2):
        return True
    return False

def starts_with(word):
    #Returns first letter of a word
    return word[0]

def remove_first_list(dictionary):
    #Removes the first letter of every word in the dictionary
    return [remove_first(w) for w in dictionary]

def find_index(word, dictionary):
    #Finds the index of a word
    if is_word(word, dictionary):
        return dictionary.index(word)
    else:
        print(word + " is not in the dictionary")

def binarySearch(word, dictionary):
    first = 0
    last = len(dictionary) - 1

    while first <= last:
        mid = int((first + last) / 2)
        midpt = dictionary[mid]
        if midpt > word:
            last = mid - 1
        elif midpt < word:
            first = mid + 1
        else:
            return mid,True
    return first, False
