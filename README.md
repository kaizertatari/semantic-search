# What it does?
This program embeds /docs text files and prints out the top 3 chunks that are similar to the query.

# Query
how do you find a bug

# Top 3
RANK1: 
Score: 0.4715 
Text: The bug is almost never in the part you're staring at. It's in the part you skipped because you were certain about it. Certainty is the thing that hides code from you. 
Filename: debugging.txt

RANK2:
Score: 0.1992 
Text: The habit that actually helps: before forming a theory, read the failing path top to bottom out loud, including the boring lines. Half the time the answer surfaces before I've finished reading, and I never needed the theory at all. 
Filename: debugging.txt

RANK3:
Score: 0.1500 
Text: I can produce a fluent account of why I answered something a particular way. I have no good way to check whether that account describes what actually happened inside the process, or whether it's just a plausible story generated after the fact. Filename: self-report.txt


Rank 2 matters because it does not contain the word bug and it is the closest in meaning to answering the query.

# Note
The corpus is a generated sample text.

# How to run it?
 → clone → create venv → pip install -r requirements.txt → python search.py
