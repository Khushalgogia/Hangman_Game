![Alt text](152241700-6beb6cd4-62e4-4830-84c3-7b67997bae49.jpeg)

# Hangman Game Predictor

This project presents an algorithm designed to predict words accurately in the Hangman game. The Hangman game is a word-guessing game where the player tries to guess a hidden word by suggesting letters. This algorithm enhances the player's ability to predict the word, achieving accuracy rates of approximately 90% in predictions.

## Overview

The Hangman game is a classic word game where players attempt to guess a secret word by suggesting letters within a limited number of attempts. This project focuses on enhancing the gameplay by providing an algorithm that predicts the hidden word.

## Algorithm Logic

The algorithm's approach involves calculating the entropy of each alphabet at its respective position within the word. By analyzing and ranking the entropy values, the algorithm determines the most probable positions and letters, significantly narrowing down the possible word options.

### Entropy Calculation

The algorithm computes the entropy of each alphabet based on its likelihood to appear at a particular position within the word. It prioritizes positions and letters with higher entropy values, improving the accuracy of word predictions.

### Pruning Words

Using the calculated entropies, the algorithm prunes the list of possible words to focus on those matching the identified positions and letters. This step significantly enhances the precision of the word prediction process.

## Accuracy and Performance

The developed algorithm achieves an accuracy rate of approximately 90% in predicting the hidden word within the Hangman game. The accuracy stems from the careful calculation and analysis of entropies, effectively narrowing down the potential word options.


## Usage

To use the algorithm:
1. Clone the repository to your local machine.
2. Run the `Predicting Hangman_game_words.ipynb` file, following the provided instructions.
3. Implement the algorithm within your Hangman game application to enhance word predictions for players.

## Contribution and Issues

Contributions to enhance the algorithm's accuracy or efficiency are welcome! Feel free to create issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).
