import string

# the list of all the letters
abc=list(string.ascii_lowercase)

def is_heterogram(word):
    '''find if the word does not has one or more letters that appers in it'''
    letters=[]
    for letter in word:
        if letter in letters:
            return False
        letters.append(letter)
    return True

def is_isogram(word):
    '''find if all the letters appers the same times in the word'''
    frcn={}
    for letter in word:
        letter.lower()
        if letter.isalpha():
            try:
                frcn[letter]+=1
            except:
                frcn[letter]=1
    return all(frc==list(frcn.values())[0] for frc in frcn.values())

def is_pangram(word):
    '''find if the word has all the letters of abc'''
    letters=[i.lower() for i in word]
    letters=sorted(letters,key=lambda lttres: 0 if any(lttre.isalpha() for lttre in lttres) else 1)
    return all(lt in letters for lt in abc)