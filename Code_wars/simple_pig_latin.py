# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !
def pig_it(text):
    li = list(text.split(" "))
    latin = ""
    for i in li:
        if i.isalpha():
            aux = i[0]
            latin += i[1:] + aux + "ay" + " "
        else:
            latin += i
    if latin[-1:] == " ":
        latin = latin[:-1]
    return latin


def run():
    text = input("Write something, we'll turn it to simple pig latin: ")
    latin = pig_it(text)
    print(latin)


if __name__ == "__main__":
    run() 