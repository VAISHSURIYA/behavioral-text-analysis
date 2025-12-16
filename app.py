import streamlit as st

# Behavioral word lists and phrase replacements
hesitation_words = ["maybe", "might", "i think", "i guess", "probably", "kind of", "sort of"]
apology_words = ["sorry", "apologize", "apologies", "just", "please"]
assertive_words = ["will", "can", "able", "confident", "sure", "definitely"]

phrase_replacements = {
    "i think i might": "I will",
    "maybe": "",
    "probably": "",
    "sorry if": "Please note,",
    "just": "",
    "kind of": "",
    "sort of": ""
}

# Streamlit UI
st.title("AI-Based Behavioral Text Analysis System")
st.write("Analyze your text for confidence, hesitation, and polite expressions.")

# Text input
text = st.text_area("Enter your text here:")

if st.button("Analyze"):
    if text.strip() == "":
        st.warning("Please enter some text to analyze!")
    else:
        text_lower = text.lower()
        
        # Count behavioral words
        hesitation_count = sum(word in text_lower for word in hesitation_words)
        apology_count = sum(word in text_lower for word in apology_words)
        assertive_count = sum(word in text_lower for word in assertive_words)
        
        # Confidence score
        confidence_score = 100 - (hesitation_count * 5) - (apology_count * 3) + (assertive_count * 5)
        confidence_score = max(0, min(100, confidence_score))
        
        # Smart improved text
        improved_text = text
        highlighted_words = []
        for phrase, replacement in phrase_replacements.items():
            if phrase in improved_text.lower():
                highlighted_words.append(phrase)
                improved_text = improved_text.lower().replace(phrase, replacement)
        improved_text = " ".join(improved_text.split())
        if len(improved_text) > 0:
            improved_text = improved_text[0].upper() + improved_text[1:]
        
        # Display results
        st.subheader("Behavioral Analysis")
        st.write(f"Hesitation words found: {hesitation_count}")
        st.write(f"Apology words found: {apology_count}")
        st.write(f"Assertive words found: {assertive_count}")
        st.write(f"Confidence Score: {confidence_score}/100")
        
        st.subheader("Detected Weak Words/Phrases")
        if highlighted_words:
            st.write(", ".join(highlighted_words))
        else:
            st.write("None found")
        
        st.subheader("Suggested Improved Text")
        st.write(improved_text)
