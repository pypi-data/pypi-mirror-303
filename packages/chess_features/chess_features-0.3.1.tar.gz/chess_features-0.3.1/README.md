# Chess Features

This Python package provides a convenient way to convert chess board representations from the Python Chess library into formats suitable for machine learning algorithms. It offers various representations that can be directly utilized as input for machine learning tasks.

## Features

- Convert Python Chess board representations into machine learning-friendly formats.
- Supports several common representations used in machine learning tasks.
- Easy-to-use interface for seamless integration into your projects.

## Installation

You can install the package using pip:

```bash
pip install chess_features
```

## Usage

Here's a basic example demonstrating how to use the package:

```python
from chess import Board
from chess_features import ChessFeatures

# Create a Chess board using the Python Chess library
board = Board()

# Initialize the ChessFeatures
converter = ChessFeatures()

# Convert the board representation into a machine learning-friendly format
# Example: Convert to a feature vector
feature_vector = converter.to_stockfish_feature_vector(board)

# Example: Convert to a bitmap
bitmap = converter.to_bitmap(board)

```

## Available Representations

- Feature Vector: A flattened vector representation of the board.
- Bitmap: A bitmap representation of the board.

## Acknowledgements

- This package utilizes the [Python Chess library](https://python-chess.readthedocs.io/en/latest/).
- The information for Stockfish features are taken from [Stockfish Evaluation Guide](https://hxim.github.io/Stockfish-Evaluation-Guide/).

## ChatGPT

Apart from this readme no ChatGPT was used.
