from autocorrect import Speller
from language_tool_python import LanguageTool
import requests

# Function to check spelling and grammar in the provided text
def check_spelling_grammar(text):
    spell = Speller()  # Initialize the spell checker from the autocorrect library
    spelling_corrections = {}  # Dictionary to store spelling corrections

    # Correct each word's spelling in the input text and gather corrections
    corrected_words = [spell(word) for word in text.split()]  # Correct spelling for each word in the input text
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
            'context': match.context,  # Context of the error
            'message': match.message,  # Message describing the error
            'suggestions': [replacement for replacement in match.replacements]  # Suggestions for fixing the error
        }

    corrected_text = tool.correct(corrected_sentence)  # Apply grammar corrections to the sentence

    # Return all corrections and the corrected text
    return spelling_corrections, grammar_corrections, corrected_text

# Function to fetch definitions of words using an online dictionary API
def get_definitions(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")  # Make a GET request to the dictionary API
    if response.status_code == 200:  # Check if the API request was successful
        return response.json()[0]["meanings"][0]["definitions"][0]["definition"]  # Return the first definition from the API response
    else:
        return None  # Return None if the word is not found or an error occurs

# Main function to run the script
def main():
    # Get text input from the user
    text = input("Enter text to check for spelling and grammar errors:\n")  # Prompt the user to enter text

    # Perform spelling and grammar check
    spelling_corrections, grammar_corrections, corrected_text = check_spelling_grammar(text)  # Call the function to check spelling and grammar

    # Display spelling corrections
    if spelling_corrections:
        print("\nSpelling Corrections:")  # Print a heading for spelling corrections
        for word, correction in spelling_corrections.items():
            print(f"- Original: {word}")  # Print the original word with a spelling error
            print(f"  Correction: {correction['spelling']}")  # Print the corrected spelling
            definition = get_definitions(correction['spelling'])  # Fetch the definition of the corrected word
            if definition:
                print(f"  Definition: {definition}")  # Print the definition if found

    # Display grammar corrections
    if grammar_corrections:
        print("\nGrammar Corrections:")  # Print a heading for grammar corrections
        for offset, correction in grammar_corrections.items():
            print(f"- Error Context: {correction['context']}")  # Print the context of the grammar error
            print(f"  Message: {correction['message']}")  # Print the message describing the error
            print(f"  Suggestions: {', '.join(correction['suggestions'])}")  # Print suggestions for fixing the error

    # Display the corrected text
    print("\nCorrected Text:")  # Print a heading for the corrected text
    print(corrected_text)  # Print the fully corrected text

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
