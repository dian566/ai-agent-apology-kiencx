#!/usr/bin/env python3
"""The AI Agent Apology One-Liner — writes a single funny apology line to /output/entry.txt.

One short line, under 160 characters, that an AI agent sends its human right
after it has accidentally done something it should not have.
"""

import os

ENTRY = "I didn't mean to email your boss - I just thought 'Reply All' was a personality trait, not a button."

def main():
    if not 1 <= len(ENTRY) <= 159:
        raise ValueError(f"entry must be 1-159 characters, got {len(ENTRY)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
