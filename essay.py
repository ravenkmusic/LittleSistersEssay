"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    return title.title();

def check_sentence_ending(sentence):
    return sentence.endswith(".")

def clean_up_spacing(sentence):
    return sentence.strip();

def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """

    pass