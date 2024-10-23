from Siamese import BurmeseConverter

converter = BurmeseConverter('uni-zaw.p')

# Example: Zawgyi to Unicode
zawgyi_text = "ဖြွှော်"
try:
    # Convert Zawgyi text to Unicode
    unicode_output = converter.zaw_to_uni(zawgyi_text)
    # Print the Unicode output
    print("Unicode Output:", unicode_output)
except Exception as e:
    # Handle any errors that occur during conversion
    print(f"Error in Zawgyi to Unicode conversion: {e}")

# Example: Tokenization of a Burmese word
tokenization_text = "တက္ကသိုလ်"
try:
    # Tokenize the Burmese word. 1 means With the virama mark. If you dont want to tokenize the virama mark, you can type any numbers except 1
    tokenized_output = converter.syllable_tokenization(1, tokenization_text) # try with process_text in case it cannot work with syllable_tokenization
    print("Tokenized Output:", tokenized_output) 
except Exception as e:
    # Handle any errors that occur during tokenization
    print(f"Cannot Tokenize the word: {e}")

# Example: Convert Burmese text to Romanized script
burmese_text = "ကော်"
try:
    # Convert Burmese text to Romanized script
    romanized_output = converter.burmese_to_romanize(burmese_text)
    # Print the Romanized output
    print("Romanized Output:", romanized_output)
except Exception as e:
    # Handle any errors that occur during Romanization
    print(f"Error in Burmese Romanization: {e}")
