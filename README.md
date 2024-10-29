# Code Analysis and Projects

This repository contains various Python projects, including sorting algorithms, the Collatz conjecture implementation, and a Word Jumble game. Each section provides insights into the functionality and time complexity of the algorithms used.

## Projects Overview

### 1. Sorting Algorithms
The repository includes implementations of different sorting algorithms:

- **Bubble Sort**: A simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. 
  - **Time Complexity**: 
    - Worst-case: O(n²)
    - Best-case: O(n) (when the array is already sorted)
  
- **Quick Sort**: A more efficient sorting algorithm that uses a divide-and-conquer approach. It selects a 'pivot' element and partitions the other elements into those less than and greater than the pivot.
  - **Time Complexity**: 
    - Average-case: O(n log n)
    - Worst-case: O(n²) (when the smallest or largest element is always chosen as the pivot)

- **Merge Sort**: A stable, divide-and-conquer sorting algorithm that splits the array into halves, sorts them, and merges them back together.
  - **Time Complexity**: 
    - O(n log n) for all cases

### 2. Collatz Conjecture
The Collatz conjecture is a sequence defined as follows: 
- Start with any positive integer n.
- If n is even, divide it by 2.
- If n is odd, multiply it by 3 and add 1.
- Repeat the process indefinitely until n reaches 1.

The implementation tracks the number of steps taken to reach 1.
- **Time Complexity**: The conjecture does not have a proven time complexity, but empirical observations suggest it behaves logarithmically for most numbers.

### 3. Word Jumble Game
A two-player game where players guess jumbled words. The game selects a random word, jumbles it, and players take turns guessing the original word.

#### Features:
- Randomly selected words from a predefined list.
- Score tracking for each player.
- Player name customization.
- Game ends after a set number of rounds or can be modified for replay.

#### Example Functions:
- **choose()**: Randomly selects a word.
- **jumble(word)**: Jumbles the letters of the chosen word.
- **thank(p1n, p2n, p1, p2)**: Displays final scores.
- **play()**: Manages the game loop.

## How to Run the Projects
1. Clone or download the repository to your local machine.
2. Ensure you have Python installed.
3. For each project, run the relevant function in your Python environment (e.g., `play()` for the Word Jumble game).

## Contributions
Contributions are welcome! Feel free to fork the repository, make improvements, or report any issues.

## License
This project is licensed under the MIT License.

## Author
(https://github.com/1046prt)
