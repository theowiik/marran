from enum import Enum

from faker import Faker


class Language(Enum):
    SWEDISH = "en_US"
    ENGLISH = "en_US"


def get_sentence(words: int, language: Language) -> str:
    """Returns a random sentence based on the number of words and language.

    Args:
        words (int): Number of words in the sentence.
        language (Language): Language of the sentence.

    Returns:
        str: Random sentence.
    """
    fake = Faker(language.value)
    sentence = fake.sentence(nb_words=words)
    return sentence


# fake = Faker(Language.SWEDISH.value)
# sentence = fake.sentence(nb_words=7)

# print(sentence)
