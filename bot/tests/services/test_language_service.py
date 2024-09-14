import pytest

from src.services.language_service import Language, get_sentence

NUM_TEST_RUNS: int = 10


@pytest.mark.parametrize(
    "language, min_word_count",
    [
        (Language.SWEDISH, 5),
        (Language.ENGLISH, 5),
    ],
)
def test_get_sentence_language(language: Language, min_word_count: int) -> None:
    """Test if the function returns a sentence in the specified language."""
    # TODO: Actually test the language of the sentence

    for _ in range(NUM_TEST_RUNS):
        sentence: str = get_sentence(min_word_count, language)
        assert isinstance(sentence, str)
        assert len(sentence.split()) >= min_word_count


@pytest.mark.parametrize(
    "language, min_word_count",
    [
        (Language.ENGLISH, 5),
        (Language.SWEDISH, 5),
    ],
)
def test_get_sentence_min_word_count(language: Language, min_word_count: int) -> None:
    """Test if the function respects the minimum word count parameter."""
    for _ in range(NUM_TEST_RUNS):
        sentence: str = get_sentence(min_word_count, language)
        assert len(sentence.replace(",", "").split()) >= min_word_count


@pytest.mark.parametrize(
    "language, word_count",
    [
        (Language.ENGLISH, 10),
        (Language.SWEDISH, 10),
    ],
)
def test_get_sentence_specific_word_count(language: Language, word_count: int) -> None:
    """Test if the function respects the exact word count parameter."""
    for _ in range(NUM_TEST_RUNS):
        sentence: str = get_sentence(word_count, language)
        assert len(sentence.replace(",", "").split()) == word_count


@pytest.mark.parametrize("language", [Language.ENGLISH, Language.SWEDISH])
def test_get_sentence_variability(language: Language) -> None:
    """Test if the function returns different sentences over multiple runs."""
    sentences: list[str] = [get_sentence(5, language) for _ in range(NUM_TEST_RUNS)]
    unique_sentences: set[str] = set(sentences)
    assert len(unique_sentences) == len(
        sentences
    ), f"The function returned duplicate sentences for language {language}"
