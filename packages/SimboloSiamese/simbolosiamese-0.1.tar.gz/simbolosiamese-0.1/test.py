from Siamese.main import BurmeseConverter

converter = BurmeseConverter('uni-zaw.p') 

zawgyi_text = "ဖြွှော်"
try:
    unicode_output = converter.zaw_to_uni(zawgyi_text)
    print("Unicode Output:", unicode_output)
except Exception as e:
    print(f"Error in Zawgyi to Unicode conversion: {e}")

burmese_text = "ကော်"
try:
    romanized_output = converter.burmese_to_romanize(burmese_text)
    print("Romanized Output:", romanized_output)
except Exception as e:
    print(f"Error in Burmese Romanization: {e}")
