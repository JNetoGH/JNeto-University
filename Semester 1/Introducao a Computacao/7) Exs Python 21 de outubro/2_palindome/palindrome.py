while True:
    word = input("insert a word to check if it's a palindrome (or type quit to exit): ")
    if word.upper() == "QUIT":
        break
    pos_conter: int = 0
    neg_conter: int = len(word) - 1

    has_been_equals_so_far: bool = True
    while pos_conter < len(word)/2:
        if word[pos_conter] != word[neg_conter]:
            has_been_equals_so_far = False
            print(f"diff found at word[{pos_conter}]:{word[pos_conter]} != word[{neg_conter}]:{word[neg_conter]}")
        else:
            print(f"word[{pos_conter}]:{word[pos_conter]} == word[{neg_conter}]:{word[neg_conter]}")
        pos_conter += 1
        neg_conter -= 1

    if has_been_equals_so_far:
        print(f"\33[92m{word} is a palindrome\033[0m")
    else:
        print(f"\33[91m{word} is NOT a palindrome\033[0m")
    print()
