import collections
import random


class SmallLanguageModel:
    def __init__(self):
        """
        Initialize the SmallLanguageModel.

        This method sets up the necessary variables for the language model.
        """
        self.markov_chain = {}
        self.start_characters = []

    def train(self, text):
        """
        Train the language model on the given text data.

        Args:
            text (str): The input text to train the model on.
        """
        # Store the start characters (first character of each sentence)
        self.start_characters = [sent[0] for sent in text.split(".") if sent]

        # Create a dictionary to store the Markov chain
        for i in range(len(text) - 1):
            current_char = text[i]
            next_char = text[i + 1]

            # If the current character is not in the Markov chain yet, add it
            if current_char not in self.markov_chain:
                self.markov_chain[current_char] = collections.defaultdict(int)

            # Increment the count for the next character
            self.markov_chain[current_char][next_char] += 1

        # Normalize the probabilities for each character
        for char, next_chars in self.markov_chain.items():
            total_count = sum(next_chars.values())
            for next_char, count in next_chars.items():
                next_chars[next_char] = count / total_count

    def generate_text(self, length=100):
        """
        Generate text based on the trained Markov chain.

        Args:
            length (int): The desired length of the generated text.

        Returns:
            str: The generated text.
        """
        if not self.markov_chain:
            return "Error: Model not trained yet."

        current_char = random.choice(self.start_characters)
        generated_text = current_char

        for _ in range(length - 1):
            if current_char not in self.markov_chain:
                # If we reach a character with no followers, start a new sentence
                current_char = random.choice(self.start_characters)
                generated_text += ". " + current_char
            else:
                next_char = random.choices(
                    list(self.markov_chain[current_char].keys()),
                    weights=list(self.markov_chain[current_char].values()),
                )[0]
                generated_text += next_char
                current_char = next_char

        return generated_text


model = SmallLanguageModel()
model.train("Your training text goes here.")
generated_text = model.generate_text(length=200)
print(generated_text)


# Youres terere.. Yoextres heraingourer t tes hes tr hexte.. Yoe.. Yoeraininining tes g t he..
# Youres goer trainingoe.. Your text goe.. Yourainining hext terainingoes hext t tr hext he.. Youre.. Yoes g text g t g trera
