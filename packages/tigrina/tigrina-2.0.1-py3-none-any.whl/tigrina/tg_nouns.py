from tigrina.tg_alphabets import extract_alphabets as get_alphabet_info

alphabet_info = {
    "family_positions": get_alphabet_info.alphabets_info["family_positions"],
    "tigrina_alphabets": get_alphabet_info.alphabets_info["tigrina_alphabets"],
    "tigrina_with_crosponding_english_aphabets": get_alphabet_info.alphabets_info["tigrina_with_crosponding_english_aphabets"],
    "tigrina_alphabet_for_coding": get_alphabet_info.alphabets_info["tigrina_alphabet_for_coding"],
    "family_start_to_end_positions": get_alphabet_info.alphabets_info["family_start_to_end_positions"],
    "specialWords_identification": get_alphabet_info.alphabets_info["special_words_identification"],
    "all_front_remove_collection":get_alphabet_info.alphabets_info["all_front_remove_collection"],
    "negatives":get_alphabet_info.alphabets_info["negatives"],
    "word_ends_ley_Collection":get_alphabet_info.alphabets_info["word_ends_ley_Collection"],
    "word_ends_collection":get_alphabet_info.alphabets_info["word_ends_collection"],
    "word_ends_with_future_and_present_tense_data":get_alphabet_info.alphabets_info["word_ends_with_future_and_present_tense_data"],
    "word_ends_with_future_and_present_tense_ley_data":get_alphabet_info.alphabets_info["word_ends_with_future_and_present_tense_ley_data"]
}
def make_stem_noun(info):
    lettersToBeConverted = list(info)[-1]
    lettersNotToBeConverted = list(info)[:-1]
    indexOfFirstLetterInAlphabet = get_alphabet_info.alphabets_info['tigrina_alphabets'].index(lettersToBeConverted)
    word1 = []
    word2 = []
    word3 = []
    word4 = []
    word5 = []
    word6 = []
    word7 = []

    result=get_alphabet_info.get_alphabet(lettersToBeConverted)
    lettersNotToBeConverted="".join(map(str, lettersNotToBeConverted))
    word1.append(lettersNotToBeConverted)
    word2.append(lettersNotToBeConverted)
    word3.append(lettersNotToBeConverted)
    word4.append(lettersNotToBeConverted)
    word5.append(lettersNotToBeConverted)
    word6.append(lettersNotToBeConverted)
    word7.append(lettersNotToBeConverted)
    word1.append(result['first'])
    word2.append(result['second'])
    word3.append(result['third'])
    word4.append(result['fourth'])
    word5.append(result['fifth'])
    word6.append(result['sixth'])
    word7.append(result['seventh'])
    print("word1:",word1)
    wordChoices = [
        "".join(map(str, word1)),
        "".join(map(str, word2)),
        "".join(map(str, word3)),
        "".join(map(str, word4)),
        "".join(map(str, word5)),
        "".join(map(str, word6)),
        "".join(map(str, word7))
    ]
    print("wordChoices:",wordChoices)
    # wordChoices = ["".join(word1), "".join(word2), "".join(word3), "".join(word4), "".join(word5), "".join(word6), "".join(word7)]
    return wordChoices

def make_stem_noun_from_possess_attached_noun(info):
    word = list(info)
    endsCollection = []
    firstLetterFromEnds = word[-1]
    secondLetterFromEnds = word[-2]
    comb1 = secondLetterFromEnds + firstLetterFromEnds
    myInfo = {}
    firstLetterOfWord = word[0]
    thirdLetterFromEnds = ""
    if len(word) > 3:
        thirdLetterFromEnds = word[-3]
    comb2 = ""
    if thirdLetterFromEnds != "":
        comb2 = thirdLetterFromEnds + comb1
    if firstLetterOfWord in get_alphabet_info.alphabets_info['front_excludes']:
        word.pop(0)
        myInfo["frontCuts"] = firstLetterOfWord
    endsCollection.extend([firstLetterFromEnds, comb1, comb2])
    originalWord = list(info)
    print("endsCollection:",endsCollection)
    for item in get_alphabet_info.alphabets_info['end_possess_excludes']:
        print("item:",item)
        for key in endsCollection:
            print("endsCollection[key]:",key)
            if key == item:
                possessInfo = possess_matcher(key)
                ends = list(key)
                myInfo["possess"] = possessInfo["possess"]
                myInfo["singularity"] = possessInfo["singularity"]
                originalWord = originalWord[:-len(ends)]

    pourWord = make_stem_noun("".join(originalWord))
    myInfo["noun"] = "".join(originalWord)
    myInfo["wordChoices"] = pourWord
    return myInfo

def possess_matcher(ab):
    info = {}
    if ab == 'ይ':
        info["possess"] = 'my'
        info["singularity"] = 'singular'
    elif ab == 'ታተይ':
        info["possess"] = 'my'
        info["singularity"] = 'plural'
    elif ab in ['ካ', 'ኻ', 'ኪ', 'ኺ', 'ኩም', 'ኹም', 'ክን', 'ኽን']:
        info["possess"] = 'your'
        info["singularity"] = 'singular'
    elif ab in ['ትካ', 'ትኪ', 'ትኩም', 'ትክን', 'ታትካ', 'ታትኪ', 'ታትኩም', 'ታትክን']:
        info["possess"] = 'your'
        info["singularity"] = 'plural'
    elif ab in ['ታቱ', 'ቱ']:
        info["possess"] = 'his'
        info["singularity"] = 'plural'
    elif ab in ['ታታ', 'ታ']:
        info["possess"] = 'her'
        info["singularity"] = 'plural'
    elif ab in ['ም', 'ን', 'ኦም']:
        info["possess"] = 'their'
        info["singularity"] = 'singular'
    elif ab in ['ታቶም', 'ታተን', 'ቶም', 'ተን']:
        info["possess"] = 'their'
        info["singularity"] = 'plural'
    elif ab == 'ና':
        info["possess"] = 'our'
        info["singularity"] = 'singular'
    elif ab in ['ታትና', 'ትና']:
        info["possess"] = 'our'
        info["singularity"] = 'plural'
    elif ab == 'ታት':
        info["possess"] = ''
        info["singularity"] = 'plural'
    return info


class NounInfo:
    @staticmethod
    def noun_stem_from_possesses(text):
        # try:
            myinfo = make_stem_noun_from_possess_attached_noun(text)
            return myinfo
        # except Exception as error:
        #     return f"There is something wrong! {error}"

# You can create an instance of the NounInfo class
noun_info = NounInfo()

# calling it
# from noun_info_module import noun_info  # Assuming you saved the above code in a file named noun_info_module.py
