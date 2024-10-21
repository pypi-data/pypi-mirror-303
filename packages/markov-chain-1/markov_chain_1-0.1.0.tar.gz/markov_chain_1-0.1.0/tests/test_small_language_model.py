import pytest

from markov_chain.small_language_model import SmallLanguageModel


def test_small_language_model_initialization() -> None:
    """
    Test that SmallLanguageModel initializes with an empty Markov chain dictionary
    and an empty list of start characters.
    """
    # Arrange
    model = SmallLanguageModel()

    # Assert
    assert isinstance(model.markov_chain, dict), "markov_chain should be a dictionary"
    assert (
        len(model.markov_chain) == 0
    ), "markov_chain should be empty upon initialization"

    assert isinstance(model.start_characters, list), "start_characters should be a list"
    assert (
        len(model.start_characters) == 0
    ), "start_characters should be empty upon initialization"


# To run this test, you would typically use the pytest command in your terminal:
# pytest test_small_language_model.py

# import pytest

# from small_language_model import SmallLanguageModel

# def test_initialization():

# model = SmallLanguageModel()

# assert model.char_map == {}, "Character map should be initialized as empty."


def test_train_method_character_mapping() -> None:
    """
    Test that the train method correctly maps characters to the characters that follow them.
    Use the simple input text "hello" to verify character mappings.
    """
    # Arrange
    model = SmallLanguageModel()
    test_text = "hello"

    # Act
    model.train(test_text)

    # Assert
    expected_mappings = {
        "h": {"e": 1.0},
        "e": {"l": 1.0},
        "l": {"l": 0.5, "o": 0.5},
        # "o": {},  # 'o' is the last character, so it doesn't map to any following character
    }

    print(model.markov_chain)

    for char, expected_followers in expected_mappings.items():
        assert (
            char in model.markov_chain
        ), f"Character '{char}' should be in the Markov chain"

        for follower, expected_prob in expected_followers.items():
            assert (
                follower in model.markov_chain[char]
            ), f"'{follower}' should follow '{char}'"
            assert (
                pytest.approx(model.markov_chain[char][follower]) == expected_prob
            ), f"Probability of '{follower}' following '{char}' should be {expected_prob}"

    # assert model.start_characters == ["h"], "Start character should be 'h'"

    # # Check that the Markov chain doesn't contain any unexpected characters
    # assert set(model.markov_chain.keys()) == set(
    #     expected_mappings.keys()
    # ), "Markov chain should only contain expected characters"


# To run this test, use the command:
# pytest test_small_language_model.py


def test_predict_method() -> None:
    model = SmallLanguageModel()

    # Train the model with a simple text
    input_text = "hello"
    model.train(input_text)

    # Create a mapping for predictable character outputs
    predict_results = {
        "h": ["e"],
        "e": ["l"],
        "l": ["l", "o"],  # 'l' can predict 'l' or 'o'
        # "o": [],  # 'o' cannot predict any further character
    }

    for current_char in predict_results:
        if predict_results[
            current_char
        ]:  # Only test characters that have valid predictions
            output = model.predict_next_character(current_char)
            assert (
                output in predict_results[current_char]
            ), f"Expected one of {predict_results[current_char]} but got {output} for input '{current_char}'"
        else:
            assert (
                model.predict_next_character(current_char) is None
            ), f"Expected None for input '{current_char}'"

    # # Additionally test a character with no mapping
    # assert (
    #     model.predict_next_character("z") is None
    # ), "Expected None for untrained character 'z'"


@pytest.mark.parametrize(
    "training_text, test_cases",
    [
        (
            "hello world",
            [
                ("h", ["e"]),
                ("e", ["l"]),
                ("l", ["l", "o", "d"]),
                ("o", [" ", "r"]),
                ("w", ["o"]),
                # (
                #     "d",
                #     [],
                # ),  # 'd' is the last character, so it might return a start character
            ],
        ),
        (
            "the quick brown fox",
            [
                ("t", ["h"]),
                ("q", ["u"]),
                ("i", ["c"]),
                ("c", ["k"]),
                ("o", ["w", "x"]),
                # (
                #     "x",
                #     [],
                # ),  # 'x' is the last character, so it might return a start character
            ],
        ),
        (
            "aaa bbb ccc",
            [
                ("a", ["a", " "]),
                ("b", ["b", " "]),
                ("c", ["c"]),
                (" ", ["b", "c"]),
            ],
        ),
    ],
)
def test_predict_next_character_parametrized(
    training_text: str, test_cases: dict[str, list[str]]
) -> None:
    """
    Test that the predict_next_character method returns valid next characters
    based on various training data.
    """
    model = SmallLanguageModel()
    model.train(training_text)

    if isinstance(test_cases, list):
        for input_char, expected_outcomes in test_cases:
            predicted_char = model.predict_next_character(input_char)
            assert predicted_char in expected_outcomes, (
                f"For input '{input_char}' in text '{training_text}', "
                f"predicted '{predicted_char}' but expected one of {expected_outcomes}"
            )


@pytest.fixture
def trained_model() -> SmallLanguageModel:
    """
    Fixture to create and train a SmallLanguageModel instance with default text.
    """
    model = SmallLanguageModel()
    model.train("the quick brown fox jumps over the lazy dog")
    return model


def test_model_initialization(trained_model: SmallLanguageModel) -> None:
    """Test that the model is initialized and trained correctly."""
    assert isinstance(
        trained_model.markov_chain, dict
    ), "markov_chain should be a dictionary"
    assert (
        len(trained_model.markov_chain) > 0
    ), "markov_chain should not be empty after training"
    assert isinstance(
        trained_model.start_characters, list
    ), "start_characters should be a list"
    assert "t" in trained_model.start_characters, "start_characters should contain 't'"


@pytest.mark.parametrize(
    "input_char, expected_outcomes",
    [
        ("t", ["h"]),
        ("h", ["e"]),
        ("e", [" ", "r"]),
        ("q", ["u"]),
        ("x", [" "]),
        # ("g", []),  # 'g' is the last character, so it might return a start character
    ],
)
def test_predict_next_character(
    trained_model: SmallLanguageModel, input_char: str, expected_outcomes: list[str]
) -> None:
    """Test that predict_next_character returns valid next characters."""
    predicted_char = trained_model.predict_next_character(input_char)
    assert (
        predicted_char in expected_outcomes
    ), f"For input '{input_char}', predicted '{predicted_char}' but expected one of {expected_outcomes}"
