__Author_ = 'Ryan Cabrera'


def main():
    word_to_validate = "madamimadam"
    index = len(word_to_validate) - 1

    for character in word_to_validate:
        if character != word_to_validate[index]:
            print(word_to_validate, " is not a palindrome")
            exit(1)
        index -= 1

    print(word_to_validate, " is a palindrome")


if __Author_:
    main()
