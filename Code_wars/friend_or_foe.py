# Make a program that filters a list of strings and returns a list with only your friends name in it.

# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

# i.e.

# friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
# Note: keep the original order of the names in the output.

# someones answer
# def friend(x):
#     return [f for f in x if len(f) == 4]


def friend(x):
    friends = []
    # foes= []
    for i in x:
        if len(i) == 4:
            friends.append(i)
        # else:
        #     foes.append(i)
    return friends


def run():
    x = input("Enter names, ill tell you if they are your frines (separate by spaces): ")
    li = list(x.split(" "))
    friends_list = friend(li)
    print("This are your real friends" + str(friends_list))


if __name__ == "__main__":
    run()