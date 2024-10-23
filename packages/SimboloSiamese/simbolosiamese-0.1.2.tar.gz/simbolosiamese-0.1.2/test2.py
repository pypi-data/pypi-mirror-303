from Siamese import BurmeseConverter
from myanmartools import ZawgyiDetector
detector = ZawgyiDetector()
text = "မင္းကလဲကြာ"
score = detector.get_zawgyi_probability(text)
if score >= 0.5:
    converter = BurmeseConverter('uni-zaw.p')
    zawgyi_text = text
    unicode_output = converter.zaw_to_uni(zawgyi_text)
    romanized_output = converter.burmese_to_romanize(unicode_output)
    print(romanized_output)
print(score)