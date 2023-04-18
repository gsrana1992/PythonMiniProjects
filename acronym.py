def create_acronym(full_word: str) -> None:
    """
    Prints the acronym for any word passed as an argument

    :param: full_word, that needs to be converted to an acronym
    :return: None
    """
    acronym = ""
    for word in full_word.split():
        acronym += word[0]
    print(f'Acronym for "{full_word.title()}" would be, {acronym.upper()}')


if __name__ == '__main__':
    create_acronym('internet protocol')
