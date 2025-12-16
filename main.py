print("AI-Based Behavioral Text Analysis System")
print("-" * 40)

text = input("Enter your text: ")

# Behavioral word lists
hesitation_words = [
    "maybe", "might", "i think", "i guess", "probably", "kind of", "sort of"
]

apology_words = [
    "sorry", "apologize", "apologies", "just", "please"
]

assertive_words = [
    "will", "can", "able", "confident", "sure", "definitely"
]

text_lower = text.lower()

# Count behavioral words
hesitation_count = sum(word in text_lower for word in hesitation_words)
apology_count = sum(word in text_lower for word in apology_words)
assertive_count = sum(word in text_lower for word in assertive_words)

# Calculate confidence score
confidence_score = 100 - (hesitation_count * 5) - (apology_count * 3) + (assertive_count * 5)

# Ensure score stays between 0 and 100
if confidence_score > 100:
    confidence_score = 100
elif confidence_score < 0:
    confidence_score = 0

print("\nBehavioral Word Analysis:")
print("Hesitation words found:", hesitation_count)
print("Apology words found:", apology_count)
print("Assertive words found:", assertive_count)

print("\nConfidence Score:", confidence_score, "/100")

# Final polished improved text suggestion
improved_text = text
highlighted_words = []

# Phrase replacements for confident suggestions
phrase_replacements = {
    "i think i might": "I will",
    "maybe": "",
    "probably": "",
    "sorry if": "Please note,",
    "just": "",
    "kind of": "",
    "sort of": ""
}

# Detect weak words/phrases and highlight
for phrase, replacement in phrase_replacements.items():
    if phrase in improved_text.lower():
        highlighted_words.append(phrase)
        improved_text = improved_text.lower().replace(phrase, replacement)

# Clean extra spaces
improved_text = " ".join(improved_text.split())

# Capitalize first letter
if len(improved_text) > 0:
    improved_text = improved_text[0].upper() + improved_text[1:]

print("\nOriginal Text:")
print(text)

print("\nDetected Weak Words/Phrases:")
if highlighted_words:
    print(", ".join(highlighted_words))
else:
    print("None found")

print("\nSuggested Improved Text:")
print(improved_text)
