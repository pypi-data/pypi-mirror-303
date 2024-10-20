import re
from tigrina.tg_alphabets import extract_alphabets as get_alphabet_info
from tigrina.tg_verb_to_be import verb_to_be_info as verb_to_be_info
import locale
from tigrina.tg_verbs import verb_info as verb
from tigrina.tg_nouns import noun_info as noun_info
from tigrina.tg_code_decode import code_decode_info as code_decode
from tigrina.tg_adjectives import adjective_info as adjective
from tigrina.tg_data_process import data_management_info
from tigrina.tg_common import normalize_pandas_dataFrame_to_objects
import platform
os_name = platform.system()
os_info = platform.platform()
if 'macOS' not in os_info:
    locale.setlocale(locale.LC_COLLATE, 'ti_ER.UTF-8')
alphabet_info = {
    'family_positions': get_alphabet_info.alphabets_info['family_positions'],
    'tigrina_alphabets': get_alphabet_info.alphabets_info['tigrina_alphabets'],
    'tigrina_with_crosponding_english_aphabets': get_alphabet_info.alphabets_info['tigrina_with_crosponding_english_aphabets'],
    'tigrina_alphabet_for_coding': get_alphabet_info.alphabets_info['tigrina_alphabet_for_coding'],
    'family_start_to_end_positions': get_alphabet_info.alphabets_info['family_start_to_end_positions'],
    'specialWords_identification': get_alphabet_info.alphabets_info['special_words_identification'],
}

def compare(a, b):
    if a['order'] < b['order']:
        return -1
    if a['order'] > b['order']:
        return 1
    return 0

def convert_to_tigrina_alphabet(name):
    array_a = []
    splited_name = list(name)

    for index, data in enumerate(splited_name):
        alphabets_info_for_conversion_to_tigrina = {}

        if data == 'a':
            before_a = splited_name[index - 1] if index > 0 else None
            if before_a is None or before_a == ' ':
                alphabets_info_for_conversion_to_tigrina['order'] = index
                alphabets_info_for_conversion_to_tigrina['combinedLetters'] = data
                array_a.append(alphabets_info_for_conversion_to_tigrina)
            elif before_a == 'u':
                pass
            else:
                alphabets_info_for_conversion_to_tigrina['order'] = index - 1
                alphabets_info_for_conversion_to_tigrina['combinedLetters'] = before_a + data
                array_a.append(alphabets_info_for_conversion_to_tigrina)

        elif data == 'e':
            before_e = splited_name[index - 1] if index > 0 else None
            if before_e is None or before_e == ' ':
                alphabets_info_for_conversion_to_tigrina['order'] = index
                alphabets_info_for_conversion_to_tigrina['combinedLetters'] = data
                array_a.append(alphabets_info_for_conversion_to_tigrina)
            elif before_e == 'i':
                pass
            else:
                alphabets_info_for_conversion_to_tigrina['order'] = index - 1
                alphabets_info_for_conversion_to_tigrina['combinedLetters'] = before_e + data
                array_a.append(alphabets_info_for_conversion_to_tigrina)

        elif data == 'i':
            before_i = splited_name[index - 1] if index > 0 else None
            after_i = splited_name[index + 1] if index + 1 < len(splited_name) else None
            if before_i is None or before_i == ' ':
                if after_i == 'e':
                    alphabets_info_for_conversion_to_tigrina['order'] = index
                    alphabets_info_for_conversion_to_tigrina['combinedLetters'] = 'ie'
                    array_a.append(alphabets_info_for_conversion_to_tigrina)
                else:
                    alphabets_info_for_conversion_to_tigrina['order'] = index
                    alphabets_info_for_conversion_to_tigrina['combinedLetters'] = data
                    array_a.append(alphabets_info_for_conversion_to_tigrina)
            elif after_i == 'e':
                alphabets_info_for_conversion_to_tigrina['order'] = index - 1
                alphabets_info_for_conversion_to_tigrina['combinedLetters'] = before_i + 'ie'
                array_a.append(alphabets_info_for_conversion_to_tigrina)
            else:
                alphabets_info_for_conversion_to_tigrina['order'] = index - 1
                alphabets_info_for_conversion_to_tigrina['combinedLetters'] = before_i + data
                array_a.append(alphabets_info_for_conversion_to_tigrina)

        elif data == 'o':
            before_o = splited_name[index - 1] if index > 0 else None
            if before_o is None or before_o == ' ':
                alphabets_info_for_conversion_to_tigrina['order'] = index
                alphabets_info_for_conversion_to_tigrina['combinedLetters'] = data
                array_a.append(alphabets_info_for_conversion_to_tigrina)
            else:
                alphabets_info_for_conversion_to_tigrina['order'] = index - 1
                alphabets_info_for_conversion_to_tigrina['combinedLetters'] = before_o + data
                array_a.append(alphabets_info_for_conversion_to_tigrina)

        elif data == 'u':
            before_u = splited_name[index - 1] if index > 0 else None
            after_u = splited_name[index + 1] if index + 1 < len(splited_name) else None
            if before_u is None or before_u == ' ':
                alphabets_info_for_conversion_to_tigrina['order'] = index
                alphabets_info_for_conversion_to_tigrina['combinedLetters'] = data
                array_a.append(alphabets_info_for_conversion_to_tigrina)
            elif after_u == 'a':
                alphabets_info_for_conversion_to_tigrina['order'] = index - 1
                alphabets_info_for_conversion_to_tigrina['combinedLetters'] = before_u + data + 'a'
                array_a.append(alphabets_info_for_conversion_to_tigrina)
            elif after_u == 'o':
                alphabets_info_for_conversion_to_tigrina['order'] = index - 1
                alphabets_info_for_conversion_to_tigrina['combinedLetters'] = before_u + data + 'o'
                array_a.append(alphabets_info_for_conversion_to_tigrina)
            else:
                alphabets_info_for_conversion_to_tigrina['order'] = index - 1
                alphabets_info_for_conversion_to_tigrina['combinedLetters'] = before_u + data
                array_a.append(alphabets_info_for_conversion_to_tigrina)

        else:
            consonant = splited_name[index]
            next_to_consonant = splited_name[index + 1] if index + 1 < len(splited_name) else None
            if next_to_consonant not in ['a', 'e', 'i', 'o', 'u']:
                alphabets_info_for_conversion_to_tigrina['order'] = index
                alphabets_info_for_conversion_to_tigrina['combinedLetters'] = consonant
                array_a.append(alphabets_info_for_conversion_to_tigrina)

    # Remove duplicates based on the 'order'
    non_duplicated_result = [dict(t) for t in {tuple(d.items()) for d in array_a}]

    translated_alphabets = []
    for item in non_duplicated_result:
        for mapping in alphabet_info['tigrina_with_crosponding_english_aphabets']:
            if item['combinedLetters'] == mapping['value']:
                translated_alphabets.append({'key': mapping['key'], 'order': item['order']})

    # Sort by 'order'
    translated_alphabet_orders = sorted(translated_alphabets, key=lambda x: x['order'])

    # Collect the final translated letters
    final_name_translation_collector = [item['key'] for item in translated_alphabet_orders]

    # Join the final translated letters into a string
    english_alphabet_to_tigrina_alphabet = ''.join(final_name_translation_collector)

    return english_alphabet_to_tigrina_alphabet
def convert_sentence_to_tigrina_alphabet(text):
     # Split the input text into a list of words
    text_array = text.split(" ")
    sentence_trans_collector = []

    # Regular expression to match English alphabet characters
    reg_exp = re.compile(r'[a-zA-Z]')
    
    for item in text_array:
        # Check if the word contains English alphabet characters
        has_alphabets = reg_exp.search(item) is not None
        
        if has_alphabets:
            # Convert English word to Tigrina alphabet
            english_to_tigrina_letters = convert_to_tigrina_alphabet(item)
            sentence_trans_collector.append(english_to_tigrina_letters)
        else:
            sentence_trans_collector.append(item)

    # Join the list back into a sentence
    return " ".join(sentence_trans_collector)
def text_breaker(text, breakers):
    escaped_breakers = [re.escape(char) for char in breakers]
    regex_pattern = f"({'|'.join(escaped_breakers)})"
    parts = re.split(regex_pattern, text)
    sub_arrays = []
    for part in parts:
        if part in breakers:
            if sub_arrays:
                sub_arrays[-1] += part
            else:
                sub_arrays.append(part)
        else:
            sub_arrays.append(part)
    cleaned_array = [item.strip() for item in sub_arrays if item.strip()]
    return cleaned_array
def order_tg(data,selected_field_for_ordering,order_type):
    try:
        if len(data) > 0:
            if selected_field_for_ordering !="":
                if order_type=='asc' or order_type=='tg_asc' or order_type=='tg_ሀ_ፐ':
                        data = sorted(data, key=lambda x: locale.strxfrm(x[selected_field_for_ordering]))
                else:
                    data = sorted(data, key=lambda x: locale.strxfrm(x[selected_field_for_ordering]), reverse=True)
            else:
                if order_type=='asc' or order_type=='tg_asc' or order_type=='tg_ሀ_ፐ':
                        data = sorted(data, key=lambda x: locale.strxfrm(x))
                else:
                    data = sorted(data, key=lambda x: locale.strxfrm(x), reverse=True)
        return data
    except Exception as error:
        return f"There is something wrong!, {error}"
def tigrina_to_english_alphabet(text):
    text_array = text.split(" ")
    
    sentence_trans_collector = []
    for item in text_array:
        my_item = list(item)
        
        local_store = []
        for char in my_item:
            key_info = next((value for value in alphabet_info['tigrina_with_crosponding_english_aphabets'] if value['key'] == char), None)
            if key_info is not None:
                local_store.append(key_info['value'])
            else:
                local_store.append(char)

        output = ''.join(local_store)
        sentence_trans_collector.append(output)

    return ' '.join(sentence_trans_collector)

class TigrinaInfo:
    @staticmethod
    def code_translation(text, action, details_on_decoding=None):
        # try:
            mycode = code_decode.code_translation(text, action, details_on_decoding)
            return mycode
        # except Exception as error:
        #     return f"There is something wrong!, {error}"
    
    @staticmethod
    def convert_sentence_to_tigrina(text):
        try:
            my_tigrina_converted_text = convert_sentence_to_tigrina_alphabet(text)
            return my_tigrina_converted_text
        except Exception as error:
            return f"There is something wrong!, {error}"
    @staticmethod
    def convert_tigrina_to_english_alphabet(text):
        try:
            my_tigrina_converted_text = tigrina_to_english_alphabet(text)
            return my_tigrina_converted_text
        except Exception as error:
            return f"There is something wrong!, {error}"
    alphabet_info = alphabet_info
    @staticmethod
    def verb_to_be(text):
        try:
            result = verb_to_be_info.verb_to_be(text)
            return result
        except Exception as error:
            return f"There is something wrong!, {error}"
    def verb_to_be_trans(self):
        try:
            result = verb_to_be_info.verb_to_be_trans()
            return result
        except Exception as error:
            return f"There is something wrong!, {error}"
    @staticmethod
    def noun(text):
        try:
            result = noun_info.noun_stem_from_possesses(text)
            return result
        except Exception as error:
            return f"There is something wrong!, {error}"
    class verb:
        @staticmethod
        def create_stem_from_verb(text):
            # try:
                result = verb.make_stem_verb(text)
                return result
            # except Exception as error:
            #     return f"There is something wrong!, {error}"

        @staticmethod
        def create_verb_from_stem(text, situation, person, third_person=None, negativitiesOrFrontAdditions=None, usingLeyLetter=None):
            try:
                result = verb.make_verb_from_stem(text, situation, person, third_person, negativitiesOrFrontAdditions, usingLeyLetter)
                return result
            except Exception as error:
                return f"There is something wrong!, {error}"
    class adjective:
        @staticmethod
        def make_adjective_from_stem(text, degree, toWhome, negativity=None, in_comparison_to=None, additions=None):
            try:
                result = adjective.adjective_from_stem(text, degree, toWhome, negativity, in_comparison_to, additions)
                return result
            except Exception as error:
                return f"There is something wrong!, {error}"

        @staticmethod
        def make_stem_from_adjective(text):
            try:
                result = adjective.stem_adjective(text)
                return result
            except Exception as error:
                return f"There is something wrong!, {error}"
    @staticmethod
    def break_text(text, breakers=None):
        extras = ['.', ',', '?', 'and', 'or', '::', "።", "፡", ";", "፣", "፥", ":", "፤", "፦", ";-", "..", "፥"]
        if not breakers:
            breakers = verb_to_be_info.breakers() + extras
        textChunks = text_breaker(text, breakers)
        return textChunks
    @staticmethod
    def get_family(text):
        try:
            result = get_alphabet_info.get_family(text)
            return result
        except Exception as error:
            return f"there is something wrong. {error}"
    @staticmethod
    def order_tg(data,selected_field_for_ordering,order_type):
        try:
            result=order_tg(data,selected_field_for_ordering,order_type)
            return result
        except Exception as error:
                    return f"there is something wrong. {error}"
    @staticmethod
    def order_tg(data, selected_field_for_ordering, order_type):
        try:
            result = order_tg(data, selected_field_for_ordering, order_type)
            return result
        except Exception as error:
            return f"There is something wrong: {error}"
    @staticmethod
    def pandas_data_frame_to_object(data):
        try:
            if len(data) > 0:
                object=normalize_pandas_dataFrame_to_objects(data)
                return object
            else:
                return []
        except Exception as error:
            return f"There is something wrong: {error}"
    class Data:
        @staticmethod
        def select(query):
            try:
                result = data_management_info.get_data(query)
                return result
            except Exception as error:
                return f"There is something wrong: {error}"

        @staticmethod
        def insert(query):
            try:
                result = data_management_info.insert_data(query)
                return result
            except Exception as error:
                    return f"There is something wrong: {error}"

        @staticmethod
        def update(query):
            try:
                result = data_management_info.update_data(query)
                return result
            except Exception as error:
                    return f"There is something wrong: {error}"

        @staticmethod
        def delete(query):
            try:
                result = data_management_info.delete_data(query)
                return result
            except Exception as error:
                    return f"There is something wrong: {error}"

        @staticmethod
        def get_tables(query):
            try:
                result = data_management_info.get_tables(query)
                return result
            except Exception as error:
                    return f"There is something wrong: {error}"

        @staticmethod
        def get_fields(query):
            try:
                result = data_management_info.get_fields(query)
                return result
            except Exception as error:
                    return f"There is something wrong: {error}"
Tigrina_words = TigrinaInfo()