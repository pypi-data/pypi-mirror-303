from tigrina.tg_alphabets import extract_alphabets as get_alphabet_info
from tigrina.tg_code_decode import code_decode_info

alphabet_info = {
    "family_positions": get_alphabet_info.alphabets_info["family_positions"],
    "tigrina_alphabets": get_alphabet_info.alphabets_info["tigrina_alphabets"],
    "tigrina_with_crosponding_english_aphabets": get_alphabet_info.alphabets_info["tigrina_with_crosponding_english_aphabets"],
    "tigrina_alphabet_for_coding": get_alphabet_info.alphabets_info["tigrina_alphabet_for_coding"],
    "family_start_to_end_positions": get_alphabet_info.alphabets_info["family_start_to_end_positions"],
    "specialWords_identification": get_alphabet_info.alphabets_info["special_words_identification"],
    "begining_word_additions": get_alphabet_info.alphabets_info["begining_word_additions"],
    "last_word_additions": get_alphabet_info.alphabets_info["last_word_additions"]
}

def remove_match_from_start(text, match):
    if text.startswith(match):
        return text[len(match):]
    return text

def remove_match_from_end(text, match):
    if text.endswith(match):
        return text[:-len(match)]
    return text

def modify_text_for_adjectives(text):
    modifyText = list(text)
    first2 = ''.join(modifyText[:2])
    first3 = ''.join(modifyText[:3])
    first4 = ''.join(modifyText[:4])
    last = modifyText[-1]
    last2 = ''.join(modifyText[-2:])
    last3 = ''.join(modifyText[-3:])
    last4 = ''.join(modifyText[-4:])
    last5 = ''.join(modifyText[-5:])
    if first4 in alphabet_info['begining_word_additions']:
        text = remove_match_from_start(text, first4)
    if first3 in alphabet_info['begining_word_additions']:
        text = remove_match_from_start(text, first3)
    if first2 in alphabet_info['begining_word_additions']:
        text = remove_match_from_start(text, first2)
    if last5 in alphabet_info['last_word_additions']:
        text = remove_match_from_end(text, last5)
    if last4 in alphabet_info['last_word_additions']:
        text = remove_match_from_end(text, last4)
    if last3 in alphabet_info['last_word_additions']:
        text = remove_match_from_end(text, last3)
    if last2 in alphabet_info['last_word_additions']:
        text = remove_match_from_end(text, last2)
    if last in alphabet_info['last_word_additions']:
        text = remove_match_from_end(text, last)
    return text

def make_stem_adjective(text):
    preModifications = modify_text_for_adjectives(text)
    text = preModifications
    modificationInfo = {}
    wordToBeModified = list(text)
    word = list(text)
    lettersToBeConverted = word[-2:]
    lettersNotToBeConverted = word[:-len(lettersToBeConverted)]
    final = []
    if len(text) == 2 or len(text) == 1 or len(text) == 0:
        final = list(text)
    else:
        if lettersNotToBeConverted[0] == 'ዝ':
            modificationInfo['degree'] = 'third'
            wordToBeModified = wordToBeModified[1:]
            if lettersToBeConverted[1] == 'ት':
                modificationInfo['pronoun'] = 'she'
                wordToBeModified.pop()
            elif lettersToBeConverted[1] == 'ካ' or lettersToBeConverted[1] == 'ኪ':
                modificationInfo['pronoun'] = 'you'
                wordToBeModified.pop()
            elif lettersToBeConverted[1] == 'ና':
                modificationInfo['pronoun'] = 'we'
                wordToBeModified.pop()
            elif lettersToBeConverted[1] == 'ኩ':
                modificationInfo['pronoun'] = 'i'
                wordToBeModified.pop()
        elif lettersNotToBeConverted[0] == 'ይ':
            modificationInfo['pronoun'] = 'he'
            modificationInfo['degree'] = 'second'
            wordToBeModified = wordToBeModified[1:]
        elif lettersNotToBeConverted[0] == 'ን':
            if lettersNotToBeConverted[1] == 'ነ':
                modificationInfo['pronoun'] = 'we'
                modificationInfo['degree'] = 'second'
                wordToBeModified = ['ን'] + wordToBeModified[1:]
            else:
                if lettersToBeConverted[1] == 'ቲ' or lettersToBeConverted[1] == 'ት':
                    wordToBeModified.pop()
        elif lettersNotToBeConverted[0] == 'ት':
            modificationInfo['pronoun'] = 'she'
            modificationInfo['degree'] = 'second'
            wordToBeModified = wordToBeModified[1:]
        else:
            if lettersToBeConverted[1] == 'ቲ' or lettersToBeConverted[1] == 'ት':
                wordToBeModified.pop()
            modificationInfo['pronoun'] = 'he'
            modificationInfo['degree'] = 'first'
        lettersToBeConverted2 = wordToBeModified[-2:]
        lettersNotToBeConverted2 = wordToBeModified[:-len(lettersToBeConverted2)]
        firstLetterChoices = []
        firstLetterAfterConverstion = []
        secondLetterAfterConverstion = []

        result_1=get_alphabet_info.get_alphabet(lettersNotToBeConverted2[0]) 
        firstLetterChoices.append(result_1['sixth'])
        lettersNotToBeConverted2 = lettersNotToBeConverted2[1:]
       
        result_2=get_alphabet_info.get_alphabet(lettersToBeConverted2[0])
        firstLetterAfterConverstion.append(result_2['second'])
        
        result_3=get_alphabet_info.get_alphabet(lettersToBeConverted2[1])
        secondLetterAfterConverstion.append(result_3['sixth'])
        firstLetterAfterConverstion = [item.strip() for item in firstLetterAfterConverstion]
        lettersNotToBeConverted2 = [item.strip() for item in lettersNotToBeConverted2]
        firstLetterAfterConverstion = [item.strip() for item in firstLetterAfterConverstion]
        secondLetterAfterConverstion = [item.strip() for item in secondLetterAfterConverstion]
        
        final = firstLetterChoices + lettersNotToBeConverted2 + firstLetterAfterConverstion + secondLetterAfterConverstion
    return ''.join(final)

def divide_array(array, lastArrayLength):
    splitIndex = len(array) - lastArrayLength
    firstArray = array[:splitIndex]
    secondArray = array[splitIndex:]
    return [firstArray, secondArray]

def text_manipulation(text):
    firstLetter = []
    mytext = list(text)
    firstParts, lastPart = divide_array(mytext, 3)
    if len(firstParts) > 0:
        firstLetter = [firstParts[0]]
        firstParts = firstParts[1:]
    else:
        firstLetter = [lastPart[0]]
        lastPart = lastPart[1:]
    info = {}
    info['firstLetter'] = firstLetter
    info['firstParts'] = firstParts
    info['lastPart'] = lastPart
    return info

def decoded_manipulation(text, rule, firstCharacter, additionsAtStart, additionsAtEnd):
    textInfo = text_manipulation(text)
    code = code_decode_info.code_translation(text, 'code', '')
    decode = code_decode_info.code_translation(code, 'decode', 'yes')
    if firstCharacter != "" and firstCharacter is not None:
        if len(textInfo['firstLetter']) > 0:
            firstCharacter = int(firstCharacter) - 1
            textInfo['firstLetter'] = [decode['detailInfo'][0]['details'][0]['listOfFamilyMembers'][firstCharacter]]
    lastThree = decode['detailInfo'][0]['details'][-len(textInfo['lastPart']):]
    lastChar1 = ""
    lastChar2 = ""
    lastChar3 = ""
    rule = list(map(lambda item: int(item) - 1, rule))
    if len(lastThree) > 0:
        if len(lastThree) == 3:
            if len(rule) == 3:
                lastChar1 = lastThree[0]['listOfFamilyMembers'][rule[0]]
                lastChar2 = lastThree[1]['listOfFamilyMembers'][rule[1]]
                lastChar3 = lastThree[2]['listOfFamilyMembers'][rule[2]]
            elif len(rule) == 2:
                lastChar1 = textInfo['lastPart'][0]
                lastChar2 = lastThree[1]['listOfFamilyMembers'][rule[0]]
                lastChar3 = lastThree[2]['listOfFamilyMembers'][rule[1]]
            elif len(rule) == 1:
                lastChar1 = textInfo['lastPart'][0]
                lastChar2 = textInfo['lastPart'][1]
                lastChar3 = lastThree[2]['listOfFamilyMembers'][rule[0]]
        elif len(lastThree) == 2:
            if len(rule) == 3:
                lastChar1 = lastThree[0]['listOfFamilyMembers'][rule[0]]
                lastChar2 = lastThree[1]['listOfFamilyMembers'][rule[1]]
            elif len(rule) == 2:
                lastChar1 = lastThree[0]['listOfFamilyMembers'][rule[0]]
                lastChar2 = lastThree[1]['listOfFamilyMembers'][rule[1]]
            elif len(rule) == 1:
                lastChar1 = textInfo['lastPart'][0]
                lastChar2 = lastThree[1]['listOfFamilyMembers'][rule[0]]
        elif len(lastThree) == 1:
            if len(rule) == 3:
                lastChar1 = lastThree[0]['listOfFamilyMembers'][rule[0]]
            elif len(rule) == 2:
                lastChar1 = lastThree[0]['listOfFamilyMembers'][rule[0]]
            elif len(rule) == 1:
                lastChar1 = lastThree[0]['listOfFamilyMembers'][rule[0]]
    finalized = ""
    if lastChar1 != "":
        finalized += lastChar1
    if lastChar2 != "":
        finalized += lastChar2
    if lastChar3 != "":
        finalized += lastChar3
    finalized = (
            additionsAtStart 
            + "".join(textInfo['firstLetter']) 
            + "".join(textInfo['firstParts']) 
            + finalized 
            + additionsAtEnd
    )

    return finalized.strip()
def make_adjective_from_stem(text, degree, toWhom, negativity, in_comparison_to, additions):
    result = text
    inputText = list(text)
    firstLetterInfo = next((value for value in alphabet_info['tigrina_with_crosponding_english_aphabets'] if value['key'] == inputText[0]), None)
    convertFirstLetterTo = ""
    if firstLetterInfo is not None:
        if firstLetterInfo['position'] == 4:
            convertFirstLetterTo = 4
        elif firstLetterInfo['position'] == 6:
            convertFirstLetterTo = 1
    english=""
    if degree=='first':
        if negativity !='' and negativity !=None:
            if negativity=='ዘይ' or negativity=='እንተዘይ' or negativity=='እንተ ዘይ' or negativity=='ምስዘይ' or negativity=='ከምዘይ':
                if negativity=='ዘይ':
                    english="not"
                elif negativity=='እንተዘይ' or negativity=='እንተ ዘይ':
                    english="if it is not"
                if toWhom=='me' or toWhom=='him' or toWhom=='you':
                    result=decoded_manipulation(text,"626","","","")
                elif toWhom=='her' or toWhom=='you_female':
                    result=decoded_manipulation(text,"666","","","ቲ")
                elif toWhom=='them' or toWhom=='us' or toWhom=='them_females':
                    result=decoded_manipulation(text,"624","","","ት")
                elif toWhom=='you_females' or toWhom=='you_males':
                    result=decoded_manipulation(text,"624","","","ት")
                result=negativity+result
            elif negativity=='ከይ':
                english="Without being"
                if toWhom=='me':
                    result=decoded_manipulation(text,"46","1","ከይ","ኩ")
                elif toWhom=='him':
                    result=decoded_manipulation(text,"61","1","ከይ","")
                elif toWhom=='you':
                    result=decoded_manipulation(text,"46","1","ከይ","ካ") 
                elif toWhom=='you_female':
                    result=decoded_manipulation(text,"46","1","ከይ","ኪ") 
                elif toWhom=='you_males':
                    result=decoded_manipulation(text,"46","1","ከይ","ኩም") 
                elif toWhom=='you_females':
                    result=decoded_manipulation(text,"46","1","ከይ","ክን") 
                elif toWhom=='her':
                    result=decoded_manipulation(text,"61","4","ከይ","ት")
                elif toWhom=='them':
                    result=decoded_manipulation(text,"62","1","ከይ","")
                elif toWhom=='them_females':
                    result=decoded_manipulation(text,"64","1","ከይ","")
                elif toWhom=='us':
                    result=decoded_manipulation(text,"46","1","ከይ","ና")
            elif negativity=='ኣይ':
                english="It didn't get"
                if toWhom=='me':
                    result=decoded_manipulation(text,"646","4","ኣይ","ኩን")
                    english="I didn't get"
                elif toWhom=='him':
                    result=decoded_manipulation(text,"661","1","ኣይ","ን")
                    english="he didn't get"
                elif toWhom=='you':
                    result=decoded_manipulation(text,"661","1","ኣይ","ካን")
                    english="you didn't get"
                elif toWhom=='her':
                    result=decoded_manipulation(text,"661","1","ኣይ","ትን")
                    english="she didn't get"
                elif toWhom=='you_female':
                    result=decoded_manipulation(text,"661","1","ኣይ","ክን")
                    english="you didn't get"
                elif toWhom=='them':
                    result=decoded_manipulation(text,"612","1","ኣይ","ን")
                    english="they didn't get"
                elif toWhom=='them_females':
                    result=decoded_manipulation(text,"614","1","ኣይ","ን")
                    english="they didn't get"
                elif toWhom=='us':
                    english="we didn't get"
                    result=decoded_manipulation(text,"646","1","ኣይ","ናን")
                elif toWhom=='you_males':
                    english="you didn't get"
                    result=decoded_manipulation(text,"646","1","ኣይ","ኩምን")
            elif negativity=='ኣብዘይ':
                if toWhom=='me':
                    english="where i don't"
                    result=decoded_manipulation(text,"646","","ኣብዘይ","ኩሉ")
                elif toWhom=='him':
                    english="where he doesn't"
                    result=decoded_manipulation(text,"644","","ኣብዘይ","ሉ")
                elif toWhom=='you':
                    english="where you don't"
                    result=decoded_manipulation(text,"646","","ኣብዘይ","ካሉ")
                elif toWhom=='you_female':
                    english="where you don't"
                    result=decoded_manipulation(text,"646","","ኣብዘይ","ክሉ")
                elif toWhom=='you_females':
                    english="where you don't"
                    result=decoded_manipulation(text,"646","","ኣብዘይ","ክናሉ")
                elif toWhom=='you_males':
                    english="where you don't"
                    result=decoded_manipulation(text,"646","","ኣብዘይ","ክምሉ")
                elif toWhom=='her':
                    english="where she doesn't"
                    result=decoded_manipulation(text,"646","","ኣብዘይ","ትሉ")
                elif toWhom=='them':
                    english="where they don't"
                    result=decoded_manipulation(text,"666","","ኣብዘይ","ሉ")
                elif toWhom=='them_females':
                    english="where they don't"
                    result=decoded_manipulation(text,"644","","ኣብዘይ","ሉ")
                elif toWhom=='us':
                    english="where we don't"
                    result=decoded_manipulation(text,"646","","ኣብዘይ","ናሉ")
            else:
                if toWhom=='me' or toWhom=='him' or toWhom=='you':
                    result=decoded_manipulation(text,"626","","","")
                elif toWhom=='her' or toWhom=='you_female':
                    result=decoded_manipulation(text,"666","","","ቲ")
                elif toWhom=='them' or toWhom=='us' or toWhom=='them_females':
                    result=decoded_manipulation(text,"624","","","ት")
                elif toWhom=='you_females' or toWhom=='you_males':
                    result=decoded_manipulation(text,"624","","","ት")
    elif degree == 'second':
        english = "er"
        if toWhom == 'me' or toWhom == 'him':
            result = decoded_manipulation(text, "66", "", "ይ", "")
        elif toWhom == 'her' or toWhom == 'you':
            result = decoded_manipulation(text, "66", "", "ት", "")
        elif toWhom == 'them':
            result = decoded_manipulation(text, "62", "", "ይ", "")
        elif toWhom == 'us':
            result = decoded_manipulation(text, "66", "", "ን", "")
        elif toWhom == 'you_males':
            result = decoded_manipulation(text, "62", "", "ት", "")
        elif toWhom == 'you_female':
            result = decoded_manipulation(text, "63", "", "ት", "")
        elif toWhom == 'you_females':
            result = decoded_manipulation(text, "64", "", "ት", "")
    elif degree == 'third':
        english = "est"
        if toWhom == 'me':
            result = decoded_manipulation(text, "46", "1", "ዝ", "ኩ")
        elif toWhom == 'him':
            result = decoded_manipulation(text, "61", "1", "ዝ", "")
        elif toWhom == 'her':
            result = decoded_manipulation(text, "61", "1", "ዝ", "ት")
        elif toWhom == 'them':
            result = decoded_manipulation(text, "62", "1", "ዝ", "")
        elif toWhom == 'us':
            result = decoded_manipulation(text, "6", "1", "ዝ", "ና")
        elif toWhom == 'you':
            result = decoded_manipulation(text, "6", "1", "ዝ", "ካ")
        elif toWhom == 'you_male':
            result = decoded_manipulation(text, "6", "1", "ዝ", "ካ")
        elif toWhom == 'you_female':
            result = decoded_manipulation(text, "6", "1", "ዝ", "ኪ")
        elif toWhom == 'you_females':
            result = decoded_manipulation(text, "6", "1", "ዝ", "ክን")
        elif toWhom == 'you_males':
            result = decoded_manipulation(text, "6", "1", "ዝ", "ኩም")
    else:
        if additions == 'ኣብዝ':
            if toWhom == 'me':
                english = "Where i am"
                result = decoded_manipulation(text, "66", "6", "ኣብዝ", "")
            elif toWhom == 'him':
                english = "Where he is"
                result = decoded_manipulation(text, "66", "6", "ኣብዝ", "")
            elif toWhom == 'it':
                english = "Where it is"
                result = decoded_manipulation(text, "66", "6", "ኣብዝ", "")
            elif toWhom == 'you':
                english = "Where you are"
                result = decoded_manipulation(text, "66", "", "ኣብዝ", "")
            elif toWhom == 'you_female':
                english = "Where you are"
                result = decoded_manipulation(text, "63", "", "ኣብት", "")
            elif toWhom == 'you_females':
                english = "Where you are"
                result = decoded_manipulation(text, "64", "", "ኣብት", "")
            elif toWhom == 'you_males':
                english = "Where you are"
                result = decoded_manipulation(text, "62", "", "ኣብት", "")
            elif toWhom == 'her':
                english = "Where she is"
                result = decoded_manipulation(text, "66", "", "ኣብት", "")
            elif toWhom == 'them':
                english = "Where they are"
                result = decoded_manipulation(text, "62", "", "ኣብዝ", "")
            elif toWhom == 'them_females':
                english = "Where they are"
                result = decoded_manipulation(text, "64", "", "ኣብዝ", "")
            elif toWhom == 'us':
                english = "Where we are"
                result = decoded_manipulation(text, "66", "", "ኣብን", "")
        elif additions == 'ብዝ':
            english = 'ly'
            if toWhom == 'me':
                result = decoded_manipulation(text, "66", "6", "ብዝ", "")
            elif toWhom == 'him':
                result = decoded_manipulation(text, "66", "6", "ብዝ", "")
            elif toWhom == 'it':
                result = decoded_manipulation(text, "66", "6", "ብዝ", "")
            elif toWhom == 'you':
                result = decoded_manipulation(text, "66", "", "ብዝ", "")
            elif toWhom == 'you_female':
                result = decoded_manipulation(text, "63", "", "ብት", "")
            elif toWhom == 'you_females':
                result = decoded_manipulation(text, "64", "", "ብት", "")
            elif toWhom == 'you_males':
                result = decoded_manipulation(text, "62", "", "ብት", "")
            elif toWhom == 'her':
                result = decoded_manipulation(text, "66", "", "ብት", "")
            elif toWhom == 'them':
                result = decoded_manipulation(text, "62", "", "ብዝ", "")
            elif toWhom == 'them_females':
                result = decoded_manipulation(text, "64", "", "ብዝ", "")
            elif toWhom == 'us':
                result = decoded_manipulation(text, "66", "", "ብን", "")
        elif additions == 'እንተ':
            if toWhom == 'me':
                english = "if i get"
                result = decoded_manipulation(text, "31", convertFirstLetterTo, "እንተ", "")
            elif toWhom == 'him':
                english = "if he gets"
                result = decoded_manipulation(text, "32", convertFirstLetterTo, "እንተ", "")
            elif toWhom == 'it':
                english = "if it gets"
                result = decoded_manipulation(text, "32", convertFirstLetterTo, "እንተ", "")
            elif toWhom == 'you':
                english = "if you get"
                result = decoded_manipulation(text, "66", convertFirstLetterTo, "እንተ", "ካ")
            elif toWhom == 'you_female':
                english = "if you get"
                result = decoded_manipulation(text, "66", convertFirstLetterTo, "እንተ", "ኪ")
            elif toWhom == 'you_females':
                english = "if you get"
                result = decoded_manipulation(text, "66", convertFirstLetterTo, "እንተ", "ክን")
            elif toWhom == 'you_males':
                english = "if you get"
                result = decoded_manipulation(text, "66", convertFirstLetterTo, "እንተ", "ኩም")
            elif toWhom == 'her':
                english = "if she gets"
                result = decoded_manipulation(text, "34", convertFirstLetterTo, "እንተ", "")
            elif toWhom == 'them':
                english = "if they get"
                result = decoded_manipulation(text, "37", convertFirstLetterTo, "እንተ", "ም")
            elif toWhom == 'them_females':
                english = "if they get"
                result = decoded_manipulation(text, "31", convertFirstLetterTo, "እንተ", "ን")
            elif toWhom == 'us':
                english = "if we get"
                result = decoded_manipulation(text, "36", convertFirstLetterTo, "እንተ", "ና")
        elif additions == 'እንተዝ':
            if toWhom == 'me':
                english = "if only I was"
                result = decoded_manipulation(text, "66", "6", "እንተዝ", "")
            elif toWhom == 'him':
                english = "if only he was"
                result = decoded_manipulation(text, "66", "6", "እንተዝ", "")
            elif toWhom == 'it':
                english = "if only it was"
                result = decoded_manipulation(text, "66", "6", "እንተዝ", "")
            elif toWhom == 'you':
                english = "if only you were"
                result = decoded_manipulation(text, "66", "", "እንተዝ", "")
            elif toWhom == 'you_female':
                english = "if only you were"
                result = decoded_manipulation(text, "63", "", "እንተዝ", "")
            elif toWhom == 'you_females':
                english = "if only you were"
                result = decoded_manipulation(text, "64", "", "እንተዝ", "")
            elif toWhom == 'you_males':
                english = "if only you were"
                result = decoded_manipulation(text, "62", "", "እንተዝ", "")
            elif toWhom == 'her':
                english = "if only she was"
                result = decoded_manipulation(text, "66", "", "እንተዝ", "")
            elif toWhom == 'them':
                english = "if only they were"
                result = decoded_manipulation(text, "62", "", "እንተዝ", "")
            elif toWhom == 'them_females':
                english = "if only thet were"
                result = decoded_manipulation(text, "64", "", "እንተዝ", "")
            elif toWhom == 'us':
                english = "if only we were"
                result = decoded_manipulation(text, "66", "", "እንተን", "")
        elif additions == 'እንተዘ':
            if toWhom == 'me':
                english = 'if i'
                result = decoded_manipulation(text, "66", "1", "እንተዘ", "")
            elif toWhom == 'him':
                english = 'if he'
                result = decoded_manipulation(text, "66", "1", "እንተዘ", "")
            elif toWhom == 'it':
                english = 'if it'
                result = decoded_manipulation(text, "66", "1", "እንተዘ", "")
            elif toWhom == 'you':
                english = 'if you'
                result = decoded_manipulation(text, "66", "1", "እንተዘ", "")
            elif toWhom == 'you_female':
                english = 'if you'
                result = decoded_manipulation(text, "63", "1", "እንተዘ", "")
            elif toWhom == 'you_females':
                english = 'if you'
                result = decoded_manipulation(text, "64", "1", "እንተዘ", "")
            elif toWhom == 'you_males':
                english = 'if you'
                result = decoded_manipulation(text, "62", "1", "እንተዘ", "")
            elif toWhom == 'her':
                english = 'if she'
                result = decoded_manipulation(text, "66", "1", "እንተተ", "")
            elif toWhom == 'them':
                english = 'if they'
                result = decoded_manipulation(text, "62", "1", "እንተዘ", "")
            elif toWhom == 'them_females':
                english = 'if they'
                result = decoded_manipulation(text, "64", "1", "እንተዘ", "")
            elif toWhom == 'us':
                english = 'if we'
                result = decoded_manipulation(text, "66", "1", "እንተነ", "")
        elif additions == 'ምስዝ':
            if toWhom == 'me':
                english = "When i get"
                result = decoded_manipulation(text, "66", "6", "ምስዝ", "")
            elif toWhom == 'him':
                english = "When he gets"
                result = decoded_manipulation(text, "66", "6", "ምስዝ", "")
            elif toWhom == 'it':
                english = "When it gets"
                result = decoded_manipulation(text, "66", "6", "ምስዝ", "")
            elif toWhom == 'you':
                english = "When you get"
                result = decoded_manipulation(text, "66", "6", "ምስት", "")
            elif toWhom == 'you_female':
                english = "When you get"
                result = decoded_manipulation(text, "63", "", "ምስት", "")
            elif toWhom == 'you_females':
                english = "When you get"
                result = decoded_manipulation(text, "64", "", "ምስት", "")
            elif toWhom == 'you_males':
                english = "When you get"
                result = decoded_manipulation(text, "62", "", "ምስት", "")
            elif toWhom == 'her':
                english = "When she gets"
                result = decoded_manipulation(text, "66", "", "ምስት", "")
            elif toWhom == 'them':
                english = "When they get"
                result = decoded_manipulation(text, "62", "", "ምስዝ", "")
            elif toWhom == 'them_females':
                english = "When they get"
                result = decoded_manipulation(text, "64", "", "ምስዝ", "")
            elif toWhom == 'us':
                english = "When we get"
                result = decoded_manipulation(text, "66", "", "ምስን", "")
        elif additions == 'ኣብዝ_ሉ':
            if toWhom == 'me':
                english = "Where i am"
                result = decoded_manipulation(text, "61", "", "ኣብዝ", "ሉ")
            elif toWhom == 'him':
                english = "Where he is"
                result = decoded_manipulation(text, "61", "", "ኣብዝ", "ሉ")
            elif toWhom == 'it':
                english = "Where it is"
                result = decoded_manipulation(text, "61", "", "ኣብዝ", "ሉ")
            elif toWhom == 'you':
                english = "Where you are"
                result = decoded_manipulation(text, "61", "", "ኣብት", "ሉ")
            elif toWhom == 'you_female':
                english = "Where you are"
                result = decoded_manipulation(text, "66", "", "ኣብት", "ሉ")
            elif toWhom == 'you_females':
                english = "Where you are"
                result = decoded_manipulation(text, "64", "", "ኣብት", "ሉ")
            elif toWhom == 'you_males':
                english = "Where you are"
                result = decoded_manipulation(text, "66", "", "ኣብት", "ሉ")
            elif toWhom == 'her':
                english = "Where she is"
                result = decoded_manipulation(text, "61", "", "ኣብት", "ሉ")
            elif toWhom == 'them':
                english = "Where they are"
                result = decoded_manipulation(text, "66", "", "ኣብዝ", "ሉ")
            elif toWhom == 'them_females':
                english = "Where they are"
                result = decoded_manipulation(text, "64", "", "ኣብዝ", "ሉ")
            elif toWhom == 'us':
                english = "Where we are"
                result = decoded_manipulation(text, "61", "", "ኣብን", "ሉ")
        elif additions == 'ምስዝ_ሉ':
            if toWhom == 'me':
                english = "when i"
                result = decoded_manipulation(text, "64", "", "ምስዝ", "ሉ")
            elif toWhom == 'him':
                english = "when he"
                result = decoded_manipulation(text, "64", "", "ምስዝ", "ሉ")
            elif toWhom == 'it':
                english = "when it"
                result = decoded_manipulation(text, "64", "", "ምስዝ", "ሉ")
            elif toWhom == 'you':
                english = "when you"
                result = decoded_manipulation(text, "64", "", "ምስት", "ሉ")
            elif toWhom == 'you_female':
                english = "when you"
                result = decoded_manipulation(text, "66", "", "ምስት", "ሉ")
            elif toWhom == 'you_females':
                english = "when you"
                result = decoded_manipulation(text, "64", "", "ምስት", "ሉ")
            elif toWhom == 'you_males':
                english = "when you"
                result = decoded_manipulation(text, "66", "", "ምስት", "ሉ")
            elif toWhom == 'her':
                english = "when you"
                result = decoded_manipulation(text, "64", "", "ምስት", "ሉ")
            elif toWhom == 'them':
                english = "when you"
                result = decoded_manipulation(text, "66", "", "ምስዝ", "ሉ")
            elif toWhom == 'them_females':
                english = "when you"
                result = decoded_manipulation(text, "64", "", "ምስዝ", "ሉ")
            elif toWhom == 'us':
                english = "when you"
                result = decoded_manipulation(text, "64", "", "ምስን", "ሉ")
        elif additions == 'እንተዝ_ሉ':
            if toWhom == 'me':
                english = "if only i was"
                result = decoded_manipulation(text, "64", "6", "እንተዝ", "ሉ")
            elif toWhom == 'him':
                english = "if only he was"
                result = decoded_manipulation(text, "64", "6", "እንተዝ", "ሉ")
            elif toWhom == 'it':
                english = "if only it was"
                result = decoded_manipulation(text, "64", "6", "እንተዝ", "ሉ")
            elif toWhom == 'you':
                english = "if only you were"
                result = decoded_manipulation(text, "64", "", "እንተት", "ሉ")
            elif toWhom == 'you_female':
                english = "if only you were"
                result = decoded_manipulation(text, "66", "", "እንተዝ", "ሉ")
            elif toWhom == 'you_females':
                english = "if only you were"
                result = decoded_manipulation(text, "64", "", "እንተዝ", "ሉ")
            elif toWhom == 'you_males':
                english = "if only you were"
                result = decoded_manipulation(text, "62", "", "እንተዝ", "ሉ")
            elif toWhom == 'her':
                english = "if only she was"
                result = decoded_manipulation(text, "64", "", "እንተት", "ሉ")
            elif toWhom == 'them':
                english = "if only they were"
                result = decoded_manipulation(text, "66", "", "እንተዝ", "ሉ")
            elif toWhom == 'them_females':
                english = "if only they were"
                result = decoded_manipulation(text, "64", "", "እንተዝ", "ሉ")
            elif toWhom == 'us':
                english = "if only we were"
                result = decoded_manipulation(text, "66", "", "እንተን", "ሉ")
        elif additions == 'እንተዘ_ሉ':
            if toWhom == 'me':
                english = "if i"
                result = decoded_manipulation(text, "64", "1", "እንተዘ", "ሉ")
            elif toWhom == 'him':
                english = "if he"
                result = decoded_manipulation(text, "64", "1", "እንተዘ", "ሉ")
            elif toWhom == 'it':
                english = "if it"
                result = decoded_manipulation(text, "64", "1", "እንተዘ", "ሉ")
            elif toWhom == 'you':
                english = "if you"
                result = decoded_manipulation(text, "64", "1", "እንተዘ", "ሉ")
            elif toWhom == 'you_female':
                english = "if you"
                result = decoded_manipulation(text, "66", "1", "እንተዘ", "ሉ")
            elif toWhom == 'you_females':
                english = "if you"
                result = decoded_manipulation(text, "64", "1", "እንተዘ", "ሉ")
            elif toWhom == 'you_males':
                english = "if you"
                result = decoded_manipulation(text, "62", "1", "እንተዘ", "ሉ")
            elif toWhom == 'her':
                english = "if she"
                result = decoded_manipulation(text, "66", "1", "እንተተ", "ሉ")
            elif toWhom == 'them':
                english = "if they"
                result = decoded_manipulation(text, "62", "1", "እንተዘ", "ሉ")
            elif toWhom == 'them_females':
                english = "if they"
                result = decoded_manipulation(text, "64", "1", "እንተዘ", "ሉ")
            elif toWhom == 'us':
                english = "if we"
                result = decoded_manipulation(text, "66", "1", "እንተነ", "ሉ")
        elif additions == 'እንተ_ሉ':
            if toWhom == 'me':
                english = "if i am"
                result = decoded_manipulation(text, "61", convertFirstLetterTo, "እንተ", "ሉ")
            elif toWhom == 'him':
                english = "if he is"
                result = decoded_manipulation(text, "62", convertFirstLetterTo, "እንተ", "ሉ")
            elif toWhom == 'it':
                english = "if it is"
                result = decoded_manipulation(text, "62", convertFirstLetterTo, "እንተ", "ሉ")
            elif toWhom == 'you':
                english = "if you are"
                result = decoded_manipulation(text, "66", convertFirstLetterTo, "እንተ", "ካሉ")
            elif toWhom == 'you_female':
                english = "if you are"
                result = decoded_manipulation(text, "66", convertFirstLetterTo, "እንተ", "ኪሉ")
            elif toWhom == 'you_females':
                english = "if you are"
                result = decoded_manipulation(text, "66", convertFirstLetterTo, "እንተ", "ክንሉ")
            elif toWhom == 'you_males':
                english = "if you are"
                result = decoded_manipulation(text, "66", convertFirstLetterTo, "እንተ", "ኩምሉ")
            elif toWhom == 'her':
                english = "if she is"
                result = decoded_manipulation(text, "64", convertFirstLetterTo, "እንተ", "ትሉ")
            elif toWhom == 'them':
                english = "if they are"
                result = decoded_manipulation(text, "67", convertFirstLetterTo, "እንተ", "ምሉ")
            elif toWhom == 'them_females':
                english = "if they are"
                result = decoded_manipulation(text, "61", convertFirstLetterTo, "እንተ", "ንሉ")
            elif toWhom == 'us':
                english = "if we are"
                result = decoded_manipulation(text, "66", convertFirstLetterTo, "እንተ", "ናሉ")
        else:
            additionsAtEnd=""
            if in_comparison_to=="him":
                if toWhom=='me':
                    english="i verb_past him"
                    additionsAtEnd="ዮ"
                elif toWhom=='him':
                    english="he verb_past him"
                    additionsAtEnd="ዎ"
                elif toWhom=='it':
                    english="it verb_past him"
                    additionsAtEnd="ዎ"
                elif toWhom=='her':
                    english="she verb_past him"
                    additionsAtEnd="ቶ"
                elif toWhom=='them':
                    english="they verb_past him"
                    additionsAtEnd="ሞ"
                elif toWhom=='them_females':
                    english="they verb_past him"
                    additionsAtEnd="ንኦ"
                elif toWhom=='us':
                    english="we verb_past him"
                    additionsAtEnd="ናዮ"
                elif toWhom=='you':
                    english="you verb_past him"
                    additionsAtEnd="ካዮ"
                elif toWhom=='you_female':
                    english="you verb_past him"
                    additionsAtEnd="ኪዮ"
                elif toWhom=='you_females':
                    english="you verb_past him"
                    additionsAtEnd="ክንኦ"
                elif toWhom=='you_males':
                    english="you verb_past him"
                    additionsAtEnd="ክምዎ"
            elif in_comparison_to=='her':
                if toWhom=='me':
                    english="i verb_past her"
                    additionsAtEnd="ያ"
                elif toWhom=='him':
                    english="he verb_past her"
                    additionsAtEnd="ዋ"
                elif toWhom=='it':
                    english="it verb_past her"
                    additionsAtEnd="ዋ"
                elif toWhom=='her':
                    english="she verb_past her"
                    additionsAtEnd="ታ"
                elif toWhom=='them':
                    english="they verb_past her"
                    additionsAtEnd="ማ"
                elif toWhom=='them_females':
                    english="they verb_past her"
                    additionsAtEnd="ንኣ"
                elif toWhom=='us':
                    english="we verb_past her"
                    additionsAtEnd="ኩማ"
                elif toWhom=='you':
                    english="you verb_past her"
                    additionsAtEnd="ካያ"
                elif toWhom=='you_female':
                    english="you verb_past her"
                    additionsAtEnd="ኪያ"
                elif toWhom=='you_females':
                    english="you verb_past her"
                    additionsAtEnd="ክንኣ"
                elif toWhom=='you_males':
                    english="you verb_past her"
                    additionsAtEnd="ኩማ"
            elif in_comparison_to=='me':
                if toWhom=='me':
                    english="i verb_past me"
                    additionsAtEnd="ኒ"
                elif toWhom=='him':
                    english="he verb_past me"
                    additionsAtEnd="ኒ"
                elif toWhom=='it':
                    english="it verb_past me"
                    additionsAtEnd="ኒ"
                elif toWhom=='her':
                    english="she verb_past me"
                    additionsAtEnd="ትኒ"
                elif toWhom=='them':
                    english="they verb_past me"
                    additionsAtEnd="ምኒ"
                elif toWhom=='them_females':
                    english="they verb_past me"
                    additionsAtEnd="ናኒ"
                elif toWhom=='us':
                    english="we verb_past me"
                    additionsAtEnd="ኩምኒ"
                elif toWhom=='you':
                    english="you verb_past me"
                    additionsAtEnd="ካኒ"
                elif toWhom=='you_female':
                    english="you verb_past me"
                    additionsAtEnd="ክኒ"
                elif toWhom=='you_females':
                    english="you verb_past me"
                    additionsAtEnd="ክናኒ"
                elif toWhom=='you_males':
                    english="you verb_past me"
                    additionsAtEnd="ኩምኒ"
            elif in_comparison_to=='them':
                if toWhom=='me':
                    english="i verb_past them"
                    additionsAtEnd="ሙኒ"
                elif toWhom=='him':
                    english="he verb_past them"
                    additionsAtEnd="ሞ"
                elif toWhom=='it':
                    english="he verb_past them"
                    additionsAtEnd="ሞ"
                elif toWhom=='her':
                    english="she verb_past them"
                    english="she verb_past them"
                    additionsAtEnd="ማ"
                elif toWhom=='them':
                    english="they verb_past them"
                    english="they verb_past them"
                    additionsAtEnd="ሞም"
                elif toWhom=='them_females':
                    english="they verb_past them"
                    english="thet verb_past them"
                    additionsAtEnd="መን"
                elif toWhom=='us':
                    english="we verb_past them"
                    additionsAtEnd="ኩመን"
                elif toWhom=='you':
                    english="you verb_past them"
                    additionsAtEnd="ካዮም"
                elif toWhom=='you_female':
                    english="you verb_past them"
                    additionsAtEnd="ክዮም"
                elif toWhom=='you_females':
                    english="you verb_past them"
                    additionsAtEnd="ክንኦም"
                elif toWhom=='you_males':
                    english="you verb_past them"
                    additionsAtEnd="ኩሞም"
            elif in_comparison_to=='them_females':
                if toWhom=='me':
                    english="i verb_past them"
                    additionsAtEnd="ናኒ"
                elif toWhom=='him':
                    english="he verb_past them"
                    additionsAtEnd="ነኦ"
                elif toWhom=='it':
                    english="it verb_past them"
                    additionsAtEnd="ነኦ"
                elif toWhom=='her':
                    english="she verb_past them"
                    additionsAtEnd="ናኣ"
                elif toWhom=='them':
                    english="they verb_past them"
                    additionsAtEnd="ነኦም"
                elif toWhom=='them_females':
                    english="they verb_past them"
                    additionsAtEnd="ነአን"
                elif toWhom=='us':
                    english="we verb_past them"
                    additionsAtEnd="ኹም"
                elif toWhom=='you':
                    english="you verb_past them"
                    additionsAtEnd="ናኻ"
                elif toWhom=='you_female':
                    english="you verb_past them"
                    additionsAtEnd="ናኺ"
                elif toWhom=='you_females':
                    english="you verb_past them"
                    additionsAtEnd="ናኽን"
                elif toWhom=='you_males':
                    english="you verb_past them"
                    additionsAtEnd="ናኹም"
            else:
                if in_comparison_to == 'us':
                    if toWhom == 'me':
                        english = "i verb_past us"
                        additionsAtEnd = "ኩምኒ"
                    elif toWhom == 'him':
                        english = "he verb_past us"
                        additionsAtEnd = "ኩሞ"
                    elif toWhom == 'it':
                        english = "it verb_past us"
                        additionsAtEnd = "ኩሞ"
                    elif toWhom == 'her':
                        english = "she verb_past us"
                        additionsAtEnd = "ማ"
                    elif toWhom == 'them':
                        english = "they verb_past us"
                        additionsAtEnd = "ሞም"
                    elif toWhom == 'them_females':
                        english = "they verb_past us"
                        additionsAtEnd = "ኩመን"
                    elif toWhom == 'us':
                        english = "we verb_past us"
                        additionsAtEnd = "ኩሞም"
                    elif toWhom == 'you':
                        english = "you verb_past us"
                        additionsAtEnd = "ሙኻ"
                    elif toWhom == 'you_female':
                        english = "you verb_past us"
                        additionsAtEnd = "ሙኺ"
                    elif toWhom == 'you_females':
                        english = "you verb_past us"
                        additionsAtEnd = "ሙኽን"
                    elif toWhom == 'you_males':
                        english = "you verb_past us"
                        additionsAtEnd = "ሙኹም"
                elif in_comparison_to == 'you':
                    if toWhom == 'me':
                        english = "i verb_past you"
                        additionsAtEnd = "ካኒ"
                    elif toWhom == 'him':
                        english = "he verb_past you"
                        additionsAtEnd = "ካዮ"
                    elif toWhom == 'it':
                        english = "it verb_past you"
                        additionsAtEnd = "ካዮ"
                    elif toWhom == 'her':
                        english = "she verb_past you"
                        additionsAtEnd = "ካያ"
                    elif toWhom == 'them':
                        english = "they verb_past you"
                        additionsAtEnd = "ካዮም"
                    elif toWhom == 'them_females':
                        english = "they verb_past you"
                        additionsAtEnd = "ካየን"
                    elif toWhom == 'us':
                        english = "we verb_past you"
                        additionsAtEnd = "ካዮም"
                    elif toWhom == 'you':
                        english = "you verb_past you"
                        additionsAtEnd = "ካዮ"
                    elif toWhom == 'you_female':
                        english = "you verb_past you"
                        additionsAtEnd = "ካያ"
                    elif toWhom == 'you_females':
                        english = "you verb_past you"
                        additionsAtEnd = "ካየን"
                    elif toWhom == 'you_males':
                        english = "you verb_past you"
                        additionsAtEnd = "ካዮም"
                elif in_comparison_to == 'you_males':
                    if toWhom == 'me':
                        english = "i verb_past you"
                        additionsAtEnd = "ኩምኒ"
                    elif toWhom == 'him':
                        english = "he verb_past you"
                        additionsAtEnd = "ኩሞ"
                    elif toWhom == 'her':
                        english = "she verb_past you"
                        additionsAtEnd = "ኩማ"
                    elif toWhom == 'them':
                        english = "they verb_past you"
                        additionsAtEnd = "ኩሞም"
                    elif toWhom == 'them_females':
                        english = "they verb_past you"
                        additionsAtEnd = "ኩመን"
                    elif toWhom == 'us':
                        english = "we verb_past you"
                        additionsAtEnd = "ኩምና"
                    elif toWhom == 'you':
                        english = "you verb_past you"
                        additionsAtEnd = "ኩሞ"
                    elif toWhom == 'you_female':
                        english = "you verb_past you"
                        additionsAtEnd = "ኩማ"
                    elif toWhom == 'you_females':
                        english = "you verb_past you"
                        additionsAtEnd = "ኩመን"
                    elif toWhom == 'you_males':
                        english = "you verb_past you"
                        additionsAtEnd = "ኩሞም"
                elif in_comparison_to == 'you_female':
                    if toWhom == 'me':
                        english = "i verb_past you"
                        additionsAtEnd = "ክኒ"
                    elif toWhom == 'him':
                        english = "he verb_past you"
                        additionsAtEnd = "ክዮ"
                    elif toWhom == 'it':
                        english = "it verb_past you"
                        additionsAtEnd = "ክዮ"
                    elif toWhom == 'her':
                        english = "she verb_past you"
                        additionsAtEnd = "ክያ"
                    elif toWhom == 'them':
                        english = "they verb_past you"
                        additionsAtEnd = "ክዮም"
                    elif toWhom == 'them_females':
                        english = "they verb_past you"
                        additionsAtEnd = "ክየን"
                    elif toWhom == 'us':
                        english = "we verb_past you"
                        additionsAtEnd = "ክዮም"
                    elif toWhom == 'you':
                        english = "you verb_past you"
                        additionsAtEnd = "ክዮ"
                    elif toWhom == 'you_female':
                        english = "you verb_past you"
                        additionsAtEnd = "ክያ"
                    elif toWhom == 'you_females':
                        english = "you verb_past you"
                        additionsAtEnd = "ክየም"
                    elif toWhom == 'you_males':
                        english = "you verb_past you"
                        additionsAtEnd = "ክዮም"
                elif in_comparison_to == 'you_females':
                    if toWhom == 'me':
                        english = "i verb_past you"
                        additionsAtEnd = "ክናኒ"
                    elif toWhom == 'him':
                        english = "he verb_past you"
                        additionsAtEnd = "ክንኦ"
                    elif toWhom == 'it':
                        english = "it verb_past you"
                        additionsAtEnd = "ክንኦ"
                    elif toWhom == 'her':
                        english = "she verb_past you"
                        additionsAtEnd = "ክንኣ"
                    elif toWhom == 'them':
                        english = "they verb_past you"
                        additionsAtEnd = "ክንኦም"
                    elif toWhom == 'them_females':
                        english = "they verb_past you"
                        additionsAtEnd = "ክንአን"
                    elif toWhom == 'us':
                        english = "we verb_past you"
                        additionsAtEnd = "ክንኦም"
                    elif toWhom == 'you':
                        english = "you verb_past you"
                        additionsAtEnd = "ክንኦ"
                    elif toWhom == 'you_female':
                        english = "you verb_past you"
                        additionsAtEnd = "ክንኣ"
                    elif toWhom == 'you_females':
                        english = "you verb_past you"
                        additionsAtEnd = "ክንአን"
                    elif toWhom == 'you_males':
                        english = "you verb_past you"
                        additionsAtEnd = "ክንኦም"
                
                if toWhom == 'me':
                    result = decoded_manipulation(text, "31", convertFirstLetterTo, "", additionsAtEnd)
                elif toWhom == 'him':
                    result = decoded_manipulation(text, "36", convertFirstLetterTo, "", additionsAtEnd)
                elif toWhom == 'you':
                    result = decoded_manipulation(text, "66", convertFirstLetterTo, "", additionsAtEnd)
                elif toWhom == 'you_female':
                    result = decoded_manipulation(text, "66", convertFirstLetterTo, "", additionsAtEnd)
                elif toWhom == 'you_females':
                    result = decoded_manipulation(text, "66", convertFirstLetterTo, "", additionsAtEnd)
                elif toWhom == 'you_males':
                    result = decoded_manipulation(text, "66", convertFirstLetterTo, "", additionsAtEnd)
                elif toWhom == 'her':
                    result = decoded_manipulation(text, "34", convertFirstLetterTo, "", additionsAtEnd)
                elif toWhom == 'them':
                    result = decoded_manipulation(text, "31", convertFirstLetterTo, "", additionsAtEnd)
                elif toWhom == 'them_females':
                    result = decoded_manipulation(text, "31", convertFirstLetterTo, "", additionsAtEnd)
                elif toWhom == 'us':
                    result = decoded_manipulation(text, "36", convertFirstLetterTo, "", additionsAtEnd)
        
    info = {}
    info['text'] = text
    info['degree'] = degree
    info['toWhom'] = toWhom
    info['is_negative'] = negativity
    info['in_comparison_to'] = in_comparison_to
    info['additions'] = additions
    info['result_text_tigrina'] = result
    info['result_text_english'] = english
    return info


class AdjectivesInfo:
    @staticmethod
    def adjective_from_stem(text,degree,toWhome,negativity=None,in_comparison_to=None,additions=None):
        try:
            result=make_adjective_from_stem(text,degree,toWhome,negativity,in_comparison_to,additions)
            return result   
        except Exception as error:
            return f"There is something wrong! {error}"
    
    @staticmethod
    def stem_adjective(text):
        try:
            result=make_stem_adjective(text)
            return result  
        except Exception as error:
            return f"There is something wrong! {error}"
# You can create an instance of the NounInfo class
adjective_info = AdjectivesInfo()