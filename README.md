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

1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/text-substitution.git
   cd text-substitution

### Usage
2. Install the required library:
   ```pip install keyboard```

3. Customize the text_substitutions dictionary in the script with your own trigger-replacement pairs.
Run the script using Python in the command line:
```python text_substitution.py```

4. Start typing in any text input field.
Whenever you type a space, the script will check if any trigger words are present and replace them with their corresponding replacements.
