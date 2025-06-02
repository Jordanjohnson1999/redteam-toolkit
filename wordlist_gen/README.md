# Custom Wordlist Generator

**Author:** Seneca
**Repo:** [redteam_toolkit](https://github.com/JordanJohnson1999/redteam-toolkit)
**Tool:** `wordlist_gen.py`
**Type:** Wordlist Generator Utility
**Purpose:** Generate realistic, personal wordlists for password auditing and Red Team exercises

---

## Overview

This Python script creates a custom wordlist by combining user-provided details like names, nicknames, pets, special words, and birth years. It's useful for simulating targeted brute-force attacks in ethical hacking labs.

It focuses on generating combinations that mimic real-world password habits.


---

# Features

- Accepts common human-related data (name, nickname, pet, etc.)
- Automatically combines inputs into password-like variations
- Supports appending common suffixes like `123`, `!`, `@2024`, etc.
- Fast, simple, and educational

---

## Usage

Run the tool:

```bash
python3 wordlist_gen.py

---

# Example Output

alex_shadow
shadow1999
shadow_alex
alex@2024
1999shadow
shado_hairy
