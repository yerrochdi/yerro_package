def extract_upper(phrase):
    """_summary_
    extract upper test
    Args:
        phrase (str): _description_

    Returns:
        list: Only upper case character from the string
    >>> extract_upper("Hello Yassine")
    ['H', 'Y']
    """
    return list(filter(lambda letter: letter.isupper(), phrase))


def extract_lower(phrase):
    """_summary_
    extract lower test
    Args:
        phrase (str): _description_

    Returns:
        list: Only lower case character from the string
    >>> extract_lower("Hello Yassine")
    ['e', 'l', 'l', 'o', 'a', 's', 's', 'i', 'n', 'e']
    """
    return list(filter(lambda letter: letter.islower(), phrase))