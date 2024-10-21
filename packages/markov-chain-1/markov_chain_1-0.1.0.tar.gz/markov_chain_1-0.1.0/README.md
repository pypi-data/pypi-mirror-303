# Small Language Model

A simple implementation of a character-based small language model using a Markov chain. This model can be trained on input text to generate new text and predict the next character based on the current character.

## Table of Contents

- [Small Language Model](#small-language-model)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Example](#example)
  - [License](#license)

## Features

- Trains a Markov chain model based on character transitions in the provided text.
- Generates text of a specified length using learned character probabilities.
- Predicts the next character based on the current character using weighted probabilities.
- Handles training data and character transitions efficiently.

## Installation

To use the Small Language Model, you need Python installed on your machine. There are no additional dependencies, as it relies on Python's standard library.

## Usage

1. **Import the Class**: First, import the `SmallLanguageModel` from your module.
2. **Train the Model**: Use the `train` method with the text data you want the model to learn from.
3. **Generate Text**: Utilize the `generate_text` method to produce text of a desired length.
4. **Predict Characters**: Call `predict_next_character` with the current character to get the next predicted character.

## Example

Here’s a comprehensive example illustrating how to use `SmallLanguageModel`:

```python
from your_module import SmallLanguageModel

# Sample text for training
sample_text = """
The quick brown fox jumps over the lazy dog.
Sphinx of black quartz, judge my vow.
Pack my box with five dozen liquor jugs.
How vexingly quick daft zebras jump!
The five boxing wizards jump quickly.
"""

# Create and train the model
model = SmallLanguageModel()
model.train(sample_text)

# Generate and print some text
generated_text = model.generate_text(length=200)
print("Generated text:")
print(generated_text)

# Print some statistics about the Markov chain
print("\nMarkov Chain Statistics:")
print(f"Number of unique characters: {len(model.markov_chain)}")
print("Transition probabilities for 'e':")
if "e" in model.markov_chain:
    for next_char, prob in model.markov_chain["e"].items():
        print(f"  e -> {next_char}: {prob:.2f}")

# Test prediction
print("\nNext character predictions:")
for char in "thequickbrownfox":
    next_char = model.predict_next_character(char)
    print(f"  After '{char}': '{next_char}'")
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This simple model is inspired by the concepts of Markov chains and character-based language modeling.
Special thanks to the contributors of the Python programming language for their ongoing support and development.
text
