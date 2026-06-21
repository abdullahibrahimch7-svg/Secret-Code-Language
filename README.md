# Secret Code Language

## Description

This is a Python project that encrypts and decrypts words using a custom secret language. It was created as part of my Python learning journey while following CodeWithHarry's 100 Days of Code challenge.

## Features

* Encrypt words
* Decrypt encrypted words
* Reverse words with less than 3 characters
* Add random characters during encryption
* Handle invalid user input
* Menu-driven interface

## Technologies Used

* Python
* Random Module
* Exception Handling

## How It Works

### Encryption

* If the word length is less than 3, the word is reversed.
* Otherwise:

  * The first character is moved to the end.
  * Reverse the word.
  * Three random characters are added at the beginning.
  * Three random characters are added at the end.

### Decryption

* Removes the first three characters.
* Removes the last three characters.
* Reverse the word to get the original word
* Moves the last character back to the beginning to restore the original word.

## How to Run

1. Clone the repository.
2. Open the project folder.
3. Run the Python file.
4. Choose an option from the menu.

## Author

Abdullah Ibrahim
