import re
from tigrina.tg_main import Tigrina_words as tigrina_words

converttotg=tigrina_words.convert_sentence_to_tigrina("kemey")
print("converttotg:",converttotg)
# converttoeng=tigrina_words.convert_tigrina_to_english_alphabet("ከመይ ኣለኻ")
# print("converttoeng:",converttoeng)
# verb=tigrina_words.verb.create_stem_from_verb("ይመጽእዎም")
# print("verb:",verb)
# verb_2=tigrina_words.verb.create_verb_from_stem("መጽአ","present","he","they","zey","no")
# print("verb_2:",verb_2)
# resultAdjective_makeAdjectiveFromStem = tigrina_words.adjective.make_adjective_from_stem('ብርቱዕ', '', 'her', '', '', 'እንተዘይ') 
# print("resultAdjective_makeAdjectiveFromStem:",resultAdjective_makeAdjectiveFromStem)
# resultAdjective_makeStemFromAdjective = tigrina_words.adjective.make_stem_from_adjective('ሓይላ')
# print("resultAdjective_makeStemFromAdjective:",resultAdjective_makeStemFromAdjective)