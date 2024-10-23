import pickle
import re
from typing import Dict, Any


class BurmeseConverter:
    def __init__(self, font_dictionary_path: str):
        try:
            with open(font_dictionary_path, 'rb') as f:
                self.font_dictionary: Dict[str, str] = pickle.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Font dictionary not found at {font_dictionary_path}")
        except Exception as e:
            raise Exception(f"An error occurred while loading the font dictionary: {e}")

    def zaw_to_uni(self, text: str) -> str:
        """
        Convert Zawgyi to Unicode.
        
        :param text: Zawgyi text input
        :return: Unicode text output
        """
        try:
            lst = list(text)
            for i, char in enumerate(lst):
                if char in self.font_dictionary:
                    lst[i] = self.font_dictionary[char]

            result = "".join(lst)

            uni_pattern = r"(ေ)?(ြ)?([က-ဩဿၐ-ၕၚ-ၝၡၥၦၮ-ၰၵ-ႁႎ႐-႙႞႟])(ွ)?(ှ)?(ျ)?(င်္)?(ွ)?(ှ)?(ာ)?(း)?(္[က-ဘမလ])?"
            result = re.sub(uni_pattern, r"\7\3\12\2\6\8\4\9\5\1\10\11", result)

            return result
        except Exception as e:
            raise Exception(f"An error occurred during conversion: {e}")

    def syllable_tokenization(self, option: int, user_input: str) -> str:
        """
        Process Burmese text by tokenizing and normalizing it.
        
        :param option: Processing option, 1 to include virama mark, others without
        :param user_input: Text to be processed
        :return: Processed text with or without virama mark
        """
        try:
            if option == 1:
                processed_input = re.sub(r"([က-အ|ဥ|ဦ](င်္|[က-အ][ှ]*[့း]*[်]|([က-အ]္)|[ါ-ှႏꩻ][ꩻ]*){0,}|.)", r"\1 ", user_input)
                processed_input = re.sub(r"(([က-အ])္ ([က-အ]))", r"\2် \3", processed_input)
                return f"With the virama mark: {processed_input}"
            else:
                processed_input = re.sub(r"([က-အ|ဥ|ဦ](င်္|[က-အ][ှ]*[့း]*[်]|([က-အ]္)|[ါ-ှႏꩻ][ꩻ]*){0,}|.)", r"\1 ", user_input)
                return f"Without the virama mark: {processed_input}"
        except Exception as e:
            raise Exception(f"An error occurred during text processing: {e}")

    def burmese_to_romanize(self, text: str) -> str:
        """
        Convert Burmese text to Romanized form.
        
        :param text: Burmese text input
        :return: Romanized text output
        """
        burmese_to_roman: Dict[str, str] = {
            'က': 'k', 'ခ': 'K', 'ဂ': 'g', 'ဃ': 'G', 'င': 'c', "၎င်": "4c", "၏": "E", "၍": "rx", "၌": "Nx", "င်္": "F",
            'စ': 's', 'ဆ': 'S', 'ဇ': 'z', 'ဈ': 'Z', "ဉ": "q", 'ည': 'Q', "ဋ": "tx", "ဌ": "Tx", "ဍ": "dx", "ဎ": "Dx", "ဏ": "nx",
            "ရ": "r", "ဓ": "D", "တ": "t", "ထ": "T", "ဒ": "d", "န": "n", "ပ": "p", "ဖ": "P", "ဗ": "b", "ဘ": "B", "မ": "m",
            "ယ": "y", "ဝ": "W", "သ": "j", "ဟ": "H", "အ": "a", 'လ': 'l', "ဠ": "lx", "ဣ": "ix", "ဤ": "I",
            "၊": "/", "။": "//", "ဥ": "U", "ဦ": "O", "ဧ": "A", "ဩ": "J", "ဪ": "Joo", "ါ": "a", "ာ": "a", "ိ": "i", "ီ": "ii",
            "ု": "u", "ူ": "uu", "ေ": "e", "ဲ": "L", "ံ": "’", "့": ".", "း": ":", "ျ": "Y", "ြ": "R", "ွ": "w", "ှ": "h",
            "ဿ": "jx", "်": ""
        }

        try:
            text = text.strip()
            text = re.sub(r'\s+', ' ', text)
            text = re.sub(r' ', ',', text)
            text = re.sub(r',+', ',', text)

            # Tokenization for Romanization
            text = re.sub(r"([က-အ|ဥ|ဦ](င်္|[က-အ][ှ]*[့း]*[်]|([က-အ]္)|[ါ-ှႏꩻ][ꩻ]*){0,}|.)", r"\1 ", text)
            text = re.sub(r"(([က-အ])္ ([က-အ]))", r"\2် \3", text)

            rules = [
                (re.compile(r'ကျွန် မ '), "q'm "),
                (re.compile(r'ကျွန် တော် '), "q't "),
                (re.compile(r'ကျွန်ပ် '), 'Q" '),
                (re.compile(r'ဏ် ဍ'), "F")
            ]

            for rule in rules:
                text = rule[0].sub(rule[1], text)
            text = re.sub(r"\u1031\u102b\u103a", r"oo", text) # ‌ော်
            text = re.sub(r"\u1031\u102c\u103a", r"oo", text) # ‌ပေ်
            # Romanization conversion
            for burmese_char, roman_char in sorted(burmese_to_roman.items(), key=lambda x: len(x[0]), reverse=True):
                text = text.replace(burmese_char, roman_char)

            # Clean-up
            text = re.sub(r' ,', ",", text)

            return text
        except Exception as e:
            raise Exception(f"An error occurred during Romanization: {e}")


# Example usage of the class
if __name__ == "__main__":
    converter = BurmeseConverter('uni-zaw.p')

    # Example: Zawgyi to Unicode
    zawgyi_text = "ဖြွှော်"
    try:
        unicode_output = converter.zaw_to_uni(zawgyi_text)
        print("Unicode Output:", unicode_output)
    except Exception as e:
        print(f"Error in Zawgyi to Unicode conversion: {e}")

    # Example: Burmese Romanization
    burmese_text = "ကော်"
    try:
        romanized_output = converter.burmese_to_romanize(burmese_text)
        print("Romanized Output:", romanized_output)
    except Exception as e:
        print(f"Error in Burmese Romanization: {e}")
