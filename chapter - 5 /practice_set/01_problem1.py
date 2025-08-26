"""
1. Write a program to create a dictionary of Hindi words with values as their English 
translation. Provide user with an option to look it up!
"""

hindi_to_english = {
    "namaste": "Hello",
    "dhanyawad": "Thank you",
    "krupya": "Please",
    "shubhkamnaye": "Best wishes",
    "suprabhat": "Good morning",
    "shubh ratri": "Good night",
    "aap kese he?": "How are you?",
    "muje maf kare": "Excuse me",
    "bilkul": "Absolutely",
    "sahi hai": "That's right"
}

Choose =  input("Enter a Hindi word to translate to English: ").strip().lower()

print("Translation:", hindi_to_english.get(Choose, "Word not found in dictionary."))

