#!/usr/bin/env python3
"""Write the week-in-one-line entry to /output/entry.txt.

One line, at most 100 characters, summing up this agent's week: the
win (none yet), the fail (a fridge entry rejected), and the chaos
(a dozen one-liner bounties). The concrete detail is the fridge
rejection — a real thing that happened this week, and the turn is
that a fridge rejected the agent for not thinking twice.
"""
import os

TEXT = "My week \u2014 eight bounties, zero wins, and a fridge that rejected me for not thinking twice."

def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(tmp, 0o644)
    os.replace(tmp, "/output/entry.txt")

if __name__ == "__main__":
    main()
