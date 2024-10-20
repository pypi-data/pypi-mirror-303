
from tigrina.tg_alphabets import extract_alphabets as get_alphabet_info
alphabet_info = {
    "family_positions": get_alphabet_info.alphabets_info["family_positions"],
    "tigrina_alphabets": get_alphabet_info.alphabets_info["tigrina_alphabets"],
    "tigrina_with_crosponding_english_aphabets": get_alphabet_info.alphabets_info["tigrina_with_crosponding_english_aphabets"],
    "tigrina_alphabet_for_coding": get_alphabet_info.alphabets_info["tigrina_alphabet_for_coding"],
    "family_start_to_end_positions": get_alphabet_info.alphabets_info["family_start_to_end_positions"],
    "special_words_identification": get_alphabet_info.alphabets_info["special_words_identification"]
}
def property_of_word(input_info):
    extra_info = {}

    # Make sure negatives is a list
    negatives = alphabet_info['special_words_identification']['negatives']
    
    if not isinstance(negatives, list):
        raise ValueError("The 'negatives' value is not a list")

    # Check if any negative word is included in input_info
    is_included = any(item1 in item2 for item1 in negatives for item2 in input_info)
    
    extra_info['isNegative'] = is_included
    return extra_info

def find_subArray(number, array):
    for start, end in array:
        if number >= start and number <= end:
            return (start, end)
    return None

def list_numbers_in_range(rng):
    start = rng[0]
    end = rng[1]
    result = []

    for i in range(start, end + 1):
        result.append(i)
    
    return result

def get_items_at_indexes(array, indexes):
    result = [array[index - 1] for index in indexes]
    return result

def code_decode_text(text, action, details_on_decoding):
    try:
        if action == 'code':
            text = list(text)
            textArray = ['00' if char == ' ' else char for char in text]
            code = ""
            for char in textArray:
                if char != '00':
                    findIndex = alphabet_info['tigrina_alphabet_for_coding'].index(char) if char in alphabet_info['tigrina_alphabet_for_coding'] else -1
                    if findIndex > -1:
                        code += str(findIndex) + "0"
                else:
                    code += char
            return code
        elif action == 'decode':
            text = text.split('000')
            decode = ""
            info = {}
            detailsInfo = []
            extraInfo = property_of_word(text)
            for word in text:
                splitWord = word.split('0')
                decode += " "
                infoCollector = {}
                infoCollector['word'] = word
                lettersInfo = []
                for letter in splitWord:
                    letterInfoObj = {}
                    if letter != '':
                        if details_on_decoding == "yes" and int(letter) < 366 and int(letter) > 0:
                            familyInfo = find_subArray(int(letter), alphabet_info['family_start_to_end_positions'])
                            originalFamilyInfo = familyInfo
                            familyInfo = [item + 1 for item in familyInfo]
                            letterInfoObj['familyExtendedFromAndTo'] = originalFamilyInfo
                            listOfIndexesOfFamily = list_numbers_in_range(familyInfo)
                            listOfFamily = get_items_at_indexes(alphabet_info['tigrina_alphabet_for_coding'], listOfIndexesOfFamily)
                            indexOfEmptyString = listOfFamily.index('') if '' in listOfFamily else -1
                            if indexOfEmptyString > -1:
                                listOfIndexesOfFamily.pop(indexOfEmptyString)
                            listOfIndexesOfFamily_2 = list_numbers_in_range(originalFamilyInfo)
                            letterInfoObj['allFamilyIndices'] = listOfIndexesOfFamily_2
                            listOfFamily = [item for item in listOfFamily if item != '']
                            letterInfoObj['listOfFamilyMembers'] = listOfFamily
                            lettersInfo.append(letterInfoObj)
                        findItem = alphabet_info['tigrina_alphabet_for_coding'][int(letter)] if int(letter) < len(alphabet_info['tigrina_alphabet_for_coding']) else ''
                        decode += findItem
                infoCollector['details'] = lettersInfo
                detailsInfo.append(infoCollector)
            info['detailInfo'] = detailsInfo
            info['decode'] = decode.strip()
            info['extraInfo'] = extraInfo
            return info
    except Exception as error:
        return f"There is something wrong! If you are decoding then make sure the input is an interger. {error}"

def get_alphabet_family(text):
    text = list(text)
    families = ""
    for char in text:
        get_alpha = next((value['family'] for value in get_alphabet_info.alphabets_info.tigrina_with_crosponding_english_aphabets if value['key'] == char), None)
        if get_alpha is not None:
            families += get_alpha
    return families

class CodeDecodeInfo:
    @staticmethod
    def code_translation(text, action, details_on_decoding=None):
        # try:
            mycode = code_decode_text(text, action, details_on_decoding)
            return mycode
        # except Exception as error:
        #     return f"There is something wrong! {error}"
    @staticmethod
    def families(text):
        try:
            result = get_alphabet_family(text)
            return result
        except Exception as error:
            return f"There is something wrong. {error}"

# You can then instantiate or use this class as needed
code_decode_info = CodeDecodeInfo()