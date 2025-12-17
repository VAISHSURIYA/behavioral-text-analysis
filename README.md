# AI-Based Behavioral Text Analysis System

## Overview
This project analyzes text to detect behavioral markers such as hesitation, apology, and assertiveness.  
It calculates a **Confidence Score** and suggests **improved text** for clearer, confident communication.  
The system is interactive using **Streamlit UI**.

## Features
- Counts hesitation, apology, and assertive words
- Calculates Confidence Score (0-100)
- Highlights weak words/phrases
- Suggests improved, confident text
- Streamlit-based interactive interface

## Installation
1. Clone this repository:
```bash
git clone <your-repo-url>

 Confidence Score = 100 − (Hesitation × 5) − (Apology × 3) + (Assertive × 5)
 I just wanted to ask if maybe I could get some help, sorry for bothering you, I’m not sure if this is right.
 I will complete the task by tomorrow and share the update once it is done.
 Sorry, I might have made a mistake and I apologize if this caused any inconvenience.
I believe I can contribute effectively to this role and I am confident in my ability to learn quickly.

https://share.streamlit.io/

https://behavioral-text-analysis.streamlit.app
