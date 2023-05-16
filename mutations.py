def mutate_string(string, position, character):
    stringg=list(string)
    stringg[position]=character
    newstring="".join(stringg)
    return newstring

if __name__ == '__main__':
