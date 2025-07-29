# 🔢 Word to Number Converter

This is a fun coding challenge inspired by a prompt I saw on Instagram. The goal was to take a number written in words (like `"one hundred twenty five"`) as input and convert it to its integer form (`125`).

## 💡 Example

**Input:** `Please provide a number: one hundred twenty five`  
**Output:** `125`


## 🚀 How It Works

- Takes a **string input** representing a number in words.
- Converts the words into their numeric equivalent using a dictionary mapping.
- Supports values up to **billions** and handles multipliers like *hundred*, *thousand*, *million*, and *billion*.

## 🧠 Concepts Used

- Dictionary mapping
- String parsing
- Word-to-number conversion logic
- Basic number rules (e.g., multiplication for hundred/thousand, cumulative addition)

## 📄 Code Overview

1. The key dictionary:
```python
nums = {
    'one': 1, 'two': 2, ..., 'billion': 1000000000
}
```

2. The logic:
- Loop through each word
- Multiply on encountering "hundred", "thousand", etc.
- Accumulate the result and print the final total

## ⚙️ How to Run
```bash
python word_to_number.py
```
You’ll be prompted to enter a number in words (in English), and the script will return the integer equivalent.

## 📌 Notes
- Input must be lowercase or will be converted to lowercase.
- Only works for correctly structured number phrases (e.g., two thousand four hundred ten).
- Doesn’t handle negative numbers or decimals.
