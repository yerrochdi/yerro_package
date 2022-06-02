def extract_upper(phrase):
    return list(filter(lambda letter: letter.isupper(), phrase))


def extract_lower(phrase):
    return list(filter(lambda letter: letter.islower(), phrase))