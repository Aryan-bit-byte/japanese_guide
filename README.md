# Japanese Learning Guide

A comprehensive Japanese learning application that combines particle explanations with vocabulary management.

## Overview

This project consists of two integrated programs:
- **guide.py**: Interactive guide for learning Japanese grammar particles
- **words.py**: Word management system for storing and retrieving Japanese vocabulary

## Features

### Japanese Particle Guide (guide.py)
Learn about essential Japanese particles and their usage:
- **WA (は)**: Topic particle
- **GA (が)**: Subject particle (used with existence expressions)
- **O (を)**: Object marker (used before verbs like eat, drink, see, listen, read, write, buy, study, etc.)
- **E (へ)**: Direction particle (used with movement verbs like go, come, return)
- **NI (に)**: Location and time particle
- **DE (で)**: Location or means particle

Each particle includes detailed explanations and example use cases.
More particles will be added.

### Word Management System (words.py)
- Add new Japanese words with their meanings to a local SQLite database
- Search for word meanings instantly
- Persistent storage of vocabulary

## Requirements

- Python 3.10+
- sqlite3 (included with Python)

## Installation

1. Clone or download the project files
2. Ensure both `guide.py` and `words.py` are in the same directory
3. No additional package installation needed

## Usage

### Running the Guide
```bash
python guide.py
```

**Menu Options:**
1. **Particles** - Learn about specific Japanese particles
2. **Word meaning** - Search for stored word meanings
3. **Add new word** - Add Japanese words to your vocabulary database
4. **Exit** - Exit the program

### Running Word Management (Standalone)
```bash
python words.py
```

**Menu Options:**
1. **Add word** - Add a new Japanese word and its meaning
2. **Search word** - Look up a word's meaning
3. **Exit** - Exit the program

## Database

The application uses SQLite to store vocabulary:
- **File**: `words.db` (created automatically in the same directory)
- **Table**: `Japanese_words` with columns:
  - `name` (Japanese word)
  - `meaning` (English translation)

## Examples

### Adding a Word
```
Enter Japanese word: こんにちは
Enter meaning: Hello
```

### Searching for a Word
```
Enter word to find meaning: こんにちは
こんにちは - Hello
```

### Learning Particles
```
Select what to learn:
1. Particles
2. Word meaning
3. Add new word
4. Exit

Enter your choice: 1
Enter particle (wa, ga, o, e, ni, de): wa
Topic particle.
```

## Integration

The guide program seamlessly integrates word management features, allowing you to:
- Learn particle grammar
- Look up word meanings while studying
- Add new words to your database for future reference

All without switching between programs!

## Notes

- Words are stored permanently in the SQLite database
- The database file is created automatically on first run
- Invalid input is handled gracefully with error messages
- All particle explanations include practical usage examples

## Author
Japanese Language Learning Guide
