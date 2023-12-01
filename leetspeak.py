leet_speak_alphabet={
    "a": "4",
    "b": "I3",
    "c": "[",
    "d": ")",
    "e": "3",
    "f": "|=",
    "g": "&",
    "h": "#",
    "i": "1",
    "j": ",_|",
    "k": ">|",
    "l": "1",
    "m": "/\/\.",
    "n": "^/",
    "o": "0",
    "p": "|*",
    "q": "(_,)",
    "r": "I2",
    "s": "5",
    "t": "7",
    "u": "(_)",
    "v": "\/",
    "w": "\/\/",
    "x": "><",
    "y": "j",
    "z": "2",
    "1": "L",
    "2": "R",
    "3": "E",
    "4": "A",
    "5": "S",
    "6": "b",
    "7": "T",
    "8": "B",
    "9": "g",
    "0": "o",
}

def code_to_leet():
    while True:
        string_to_code=input('submit your string to leetcode: ')
        if len(string_to_code)==0:
            print('please dont let the string void ')
        else:
            result=''
            for char in string_to_code:
                if char.lower() in leet_speak_alphabet:
                    result+=leet_speak_alphabet[char.lower()]
                else:
                    result+=char
            print(f'"{string_to_code}" in leet alphabet is:\n "{result}"')
            you_want_continue=input('do you want to start again? [yes or no] ')
            if you_want_continue.lower()!='yes':
                break
code_to_leet()