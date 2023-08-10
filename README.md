# Text Substitution Tool

A simple Python script that automates text substitution or expansion based on predefined trigger words.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)

## Introduction

Text Substitution Tool is a Python script that allows you to automatically replace trigger words or phrases with predefined replacements while typing. This can be especially useful for inserting frequently used content, shortcuts, or commonly typed phrases without the need to type them out in full.

## Features

- Replace trigger words with predefined replacements.
- Enhance typing efficiency and reduce repetitive tasks.
- Easy customization of trigger-replacement pairs.

## Getting Started

### Prerequisites

- Python 3.x

### Installation 

Clone this repository:
   ```sh
   git clone https://github.com/your-username/text-substitution.git
   cd text-substitution
```
### Usage
1. Install the required library:
   ```pip install keyboard```

2. Customize the text_substitutions dictionary in the script with your own trigger-replacement pairs.
Run the script using Python in the command line:
```python text_substitution.py```

3. Start typing in any text input field.
Whenever you type a space, the script will check if any trigger words are present and replace them with their corresponding replacements.

### Customization
You can customize the behavior of the tool by modifying the text_substitutions dictionary in the script. Add your trigger words as keys and their corresponding replacements as values.

```
text_substitutions = {
    "hlw": "Hello",
    "crT": "create",
    # Add more substitutions as needed
}
```
### Contributing
Contributions are welcome! If you find any issues or have ideas for improvements, feel free to open an issue or submit a pull request.
