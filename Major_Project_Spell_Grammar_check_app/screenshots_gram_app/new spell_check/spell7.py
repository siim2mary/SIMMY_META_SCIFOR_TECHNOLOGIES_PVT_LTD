import streamlit as st
#from textblob import TextBlob
#import distutils
from autocorrect import Speller
from language_tool_python import LanguageTool
import requests
import pyperclip

import nltk

# Download required NLTK resources
nltk.download('wordnet')
nltk.download('omw-1.4')  # Download the Open Multilingual Wordnet

@st.cache
# Function to check spelling and grammar in the provided text
def check_spelling_grammar(text):
    spell = Speller()  # Initialize the spell checker
    spelling_corrections = {}  # Dictionary to store spelling corrections

    # Correct each word's spelling in the input text and gather corrections
    corrected_words = [spell(word) for word in text.split()]
    for original_word, corrected_word in zip(text.split(), corrected_words):
        if original_word != corrected_word:  # If a word is corrected, store it
            spelling_corrections[original_word] = {"spelling": corrected_word}

    # Join the corrected words into a sentence for further grammar checking
    corrected_sentence = " ".join(corrected_words)
    tool = LanguageTool('en-US')  # Initialize the grammar checking tool for American English
    matches = tool.check(corrected_sentence)  # Check the sentence for grammar errors

    grammar_corrections = {}  # Dictionary to store grammar corrections
    for match in matches:
        # Store each grammar correction with context, message, and suggestions
        grammar_corrections[match.offset] = {
            'context': match.context,
            'message': match.message,
            'suggestions': [replacement for replacement in match.replacements]
        }

    corrected_text = tool.correct(corrected_sentence)  # Apply grammar corrections to the sentence

    return spelling_corrections, grammar_corrections, corrected_text  # Return all corrections and the corrected text
@st.cache_data
# Function to fetch definitions of words using an online dictionary API
def get_definitions(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    if response.status_code == 200:  # Check if the API request was successful
        return response.json()[0]["meanings"][0]["definitions"][0]["definition"]  # Return the first definition
    else:
        return None  # Return None if the word is not found

# Main function to create the Streamlit app interface
def main():
    st.title("Spelling and Grammar Check App")  # Set the title of the app
    st.sidebar.title("Options")  # Set the title of the sidebar

    # Add a download button in the sidebar (currently does not download anything specific)
    st.sidebar.download_button("Download Corrections", "Corrections")

    # Add a share button in the sidebar to copy corrected text to clipboard
    if st.sidebar.button("Share"):
        pyperclip.copy("Corrected Text")  # Copy placeholder text to clipboard
        st.write("Text copied to clipboard!")  # Notify the user

    # Create a text area for the user to input the text they want to check
    text = st.text_area("Enter text to check for spelling and grammar errors:")

    # When the user clicks the "Check" button, run the spell and grammar check
    if st.button("Check"):
        spelling_corrections, grammar_corrections, corrected_text = check_spelling_grammar(text)

        # If there are any spelling or grammar corrections, display them
        if spelling_corrections or grammar_corrections:
            st.write("**Spelling Corrections:**")
            for word, correction in spelling_corrections.items():
                st.write(f"- **Original:** {word}")
                st.write(f"  - Spelling correction: {correction['spelling']}")
                definition = get_definitions(correction['spelling'])  # Fetch the definition of the corrected word
                if definition:
                    st.write(f"  - Definition: {definition}")  # Display the definition if found

            st.write("**Grammar Corrections:**")
            for offset, correction in grammar_corrections.items():
                st.write(f"- **Error Context:** {correction['context']}")
                st.write(f"  - **Message:** {correction['message']}")
                st.write(f"  - **Suggestions:** {', '.join(correction['suggestions'])}")

            # Display the fully corrected text
            st.write("**Corrected Text:**")
            st.markdown(f"<p style='color: green;'>{corrected_text}</p>", unsafe_allow_html=True)
        else:
            st.write("No corrections needed! Your text is perfect!")  # Message if no corrections are needed

# Run the app
if __name__ == "__main__":
    main()
