from tigrina.tg_alphabets import extract_alphabets as get_alphabet_info
from tigrina.tg_code_decode import code_decode_info
# code=code_decode_info.code_translation("ዘይብርትዕቲ ኔራ","code",'')


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
word_ends=[
    {
        'you_m':{
            'he':['ካዮ','him','to him'],
            'she':['ካያ','her','to her'],
            'they':['ካዮም','them','to them'],
            'they_2':['ካየን','them','to them'],
            'we':['ካና','us','to us'],
            'i':['ካኒ','me','to me'],
            'starts':{
                'present':['ይ'],
                'future':['ክት'],
                'past':[]
            },
            'ends_future_present':[6],
            'ends_stem_past':['ካ'],
        },
        'you_f':{
            'he':['ኪዮ','him','to him'],
            'she':['ኪያ','her','to her'],
            'they':['ክዮም','them','to them'],
            'they_2':['ክየን','them','to them'],
            'we':['ክና','us','to us'],
            'i':['ክኒ','me','to me'],
            'starts':{
                'present':['ት'],
                'future':['ክት'],
                'past':[]
            },
            'ends_future_present':[3],
            'ends_stem_past':['ኪ'],
            
        },
        'you_m_2':{
            'he':['ኩሞ','him','to him'],
            'she':['ኩማ','her','to her'],
            'they':['ኩሞም','them','to them'],
            'they_2':['ኩመን','them','to them'],
            'we':['ኩምና','us','to us'],
            'i':['ኩምኒ','me','to me'],
            'starts':{
                'present':['ት'],
                'future':['ክት'],
                'past':[]
            },
            'ends_future_present':[2],
            'ends_stem_past':['ኩም']
            
        },
        'you_f_2':{
            'he':['ክንኦ','him','to him'],
            'she':['ክንኣ','her','to her'],
            'they':['ክንኦም','them','to them'],
            'they_2':['ክንአን','them','to them'],
            'we':['ክናና','us','to us'],
            'i':['ክናኒ','me','to me'],
            'starts':{
                'present':['ት'],
                'future':['ክት'],
                'past':[]
            },
            'ends_future_present':[4],
            'ends_stem_past':['ክን']
            
        },
        'he':{
            'he':['ዎ','him','to him'],
            'she':['ዋ','her','to her'],
            'they':['ዎም','them','to them'],
            'they_2':['ወን','them','to them'],
            'we':['ና','us','to us'],
            'i':['ኒ','me','to me'],
            'you_m':['ካ','you','to you'],
            'you_m_2':['ኩም','you','to you'],
            'you_f':['ኪ','you','to you'],
            'you_f_2':['ክን','you','to you'],
            'starts':{
                'present':['ይ'],
                'future':['ክ'],
                'past':[]
            },
            'ends_future_present':[6],
            'ends_stem_past':[2]
            
        },
        'she':{
            'he':['ቶ','him','to him'],
            'she':['ታ','her','to her'],
            'they':['ቶም','them','to them'],
            'they_2':['ተን','them','to them'],
            'we':['ትና','us','to us'],
            'i':['ትኒ','me','to me'],
            'you_m':['ትካ','you','to you'],
            'you_m_2':['ትኩም','you','to you'],
            'you_f':['ትኪ','you','to you'],
            'you_f_2':['ትክን','you','to you'],
            'starts':{
                'present':['ት'],
                'future':['ክት'],
                'past':[]
            },
            'ends_future_present':[6],
            'ends_stem_past':[4]
            
        },
        'they':{
            'he':['ሞ','him','to him'],
            'she':['ማ','her','to her'],
            'they':['ሞም','them','to them'],
            'they_2':['መን','them','to them'],
            'we':['ምና','us','to us'],
            'i':['ምኒ','me','to me'],
            'you_m':['ምኻ','you','to you'],
            'you_m_2':['ምኹም','you','to you'],
            'you_f':['ምኺ','you','to you'],
            'you_f_2':['ምኽን','you','to you'],
            'starts':{
                'present':['ይ'],
                'future':['ክ'],
                'past':[]
            },
            'ends_future_present':[2],
            'ends_stem_past':['ም']
            
        },
        'they_2':{
            'he':['ንኦ','him','to him'],
            'she':['ንኣ','her','to her'],
            'they':['ንኦም','them','to them'],
            'they_2':['ንአን','them','to them'],
            'we':['ናና','us','to us'],
            'i':['ናኒ','me','to me'],
            'you_m':['ናኻ','you','to you'],
            'you_m_2':['ናኹም','you','to you'],
            'you_f':['ናኺ','you','to you'],
            'you_f_2':['ናኽን','you','to you'],
            'starts':{
                'present':['ይ'],
                'future':['ክ']
            },
            'ends_future_present':[4],
            'ends_stem_past':['ን']
            
        },
        'we':{
            'he':['ናዮ','him','to him'],
            'she':['ናያ','her','to her'],
            'they':['ናዮም','them','to them'],
            'they_2':['ናየን','them','to them'],
            'we':['ናኩም','us','to us'],
            'i':['ናካ','me','to me'],
            'you_m':['ናካ','you','to you'],
            'you_m_2':['ናኩም','you','to you'],
            'you_f':['ናኪ','you','to you'],
            'you_f_2':['ናክን','you','to you'],
            'starts':{
                'present':['ን'],
                'future':['ክን'],
                'past':['ን']
            },
            'ends_future_present':[6],
            'ends_stem_past':['ና']
            
        },
        'i':{
            'he':['ዮ','him','to him'],
            'she':['ያ','her','to her'],
            'they':['ዮም','them','to them'],
            'they_2':['የን','them','to them'],
            'we':['ኩም','us','to us'],
            'i':['ካኒ','me','to me'],
            'you_m':['ካ','you','to you'],
            'you_m_2':['ኩም','you','to you'],
            'you_f':['ኪ','you','to you'],
            'you_f_2':['ክን','you','to you'],
            'starts':{
                'present':['ይ'],
                'future':['ክ'],
                'past':[]
            },
            'ends_future_present':[6],
            'ends_stem_past':[1]
            
        }
    }
]
word_ends_ley=[
    {
        'you_m':{
            'he':['ካሉ','him','for him'],
            'she':['ካላ','her','for her'],
            'they':['ካሎም','them','for them'],
            'they_2':['ካለን','them','for them'],
            'we':['ካልና','us','for us'],
            'i':['ካለይ','me','for me'],
            'starts':{
                'present':['ይ'],
                'future':['ክት'],
                'past':[]
            },
            'ends_future_present':[6],
            'ends_stem_past':['ካ'],
        },
        'you_f':{
            'he':['ክሉ','him','for him'],
            'she':['ክላ','her','for her'],
            'they':['ክሎም','them','for them'],
            'they_2':['ክለን','them','for them'],
            'we':['ክልና','us','for us'],
            'i':['ክለይ','me','for me'],
            'starts':{
                'present':['ት'],
                'future':['ክት'],
                'past':[]
            },
            'ends_future_present':[3],
            'ends_stem_past':['ኪ'],
            
        },
        'you_m_2':{
            'he':['ኩምሉ','him','for him'],
            'she':['ኩምላ','her','for her'],
            'they':['ኩምሎም','them','for them'],
            'they_2':['ኩምለን','them','for them'],
            'we':['ኩምልና','us','for us'],
            'i':['ኩምለይ','me','for me'],
            'starts':{
                'present':['ት'],
                'future':['ክት'],
                'past':[]
            },
            'ends_future_present':[2],
            'ends_stem_past':['ኩም']
            
        },
        'you_f_2':{
            'he':['ክናሉ','him','for him'],
            'she':['ክናላ','her','for her'],
            'they':['ክናሎም','them','for them'],
            'they_2':['ክናለን','them','for them'],
            'we':['ክናልና','us','for us'],
            'i':['ክናለይ','me','for me'],
            'starts':{
                'present':['ት'],
                'future':['ክት'],
                'past':[]
            },
            'ends_future_present':[4],
            'ends_stem_past':['ክን']
            
        },
        'he':{
            'he':['ሉ','him','for him'],
            'she':['ላ','her','for her'],
            'they':['ሎም','them','for them'],
            'they_2':['ለን','them','for them'],
            'we':['ልና','us','for us'],
            'i':['ለይ','me','for me'],
            'you_m':['ልካ','you','for you'],
            'you_m_2':['ልኩም','you','for you'],
            'you_f':['ልኪ','you','for you'],
            'you_f_2':['ልክን','you','for you'],
            'starts':{
                'present':['ይ'],
                'future':['ክ'],
                'past':[]
            },
            'ends_future_present':[6],
            'ends_stem_past':['ሂቡ']
            
        },
        'she':{
            'he':['ትሉ','him','for him'],
            'she':['ትላ','her','for her'],
            'they':['ትሎም','them','for them'],
            'they_2':['ትለን','them','for them'],
            'we':['ትልና','us','for us'],
            'i':['ትለይ','me','for me'],
            'you_m':['ካላ','you','for you'],
            'you_m_2':['ትልኩም','you','for you'],
            'you_f':['ትልኪ','you','for you'],
            'you_f_2':['ትልክን','you','for you'],
            'starts':{
                'present':['ት'],
                'future':['ክት'],
                'past':[]
            },
            'ends_future_present':[6],
            'ends_stem_past':[4]
            
        },
        'they':{
            'he':['ምሉ','him','for him'],
            'she':['ምላ','her','for her'],
            'they':['ምሎም','them','for them'],
            'they_2':['ምለን','them','for them'],
            'we':['ምልና','us','for us'],
            'i':['ምለይ','me','for me'],
            'you_m':['ምልካ','you','for you'],
            'you_m_2':['ምልኩም','you','for you'],
            'you_f':['ምልኪ','you','for you'],
            'you_f_2':['ምልክን','you','for you'],
            'starts':{
                'present':['ይ'],
                'future':['ክ'],
                'past':[]
            },
            'ends_future_present':[2],
            'ends_stem_past':['ም']
            
        },
        'they_2':{
            'he':['ናሉ','him','for him'],
            'she':['ናላ','her','for her'],
            'they':['ናሎም','them','for them'],
            'they_2':['ናለን','them','for them'],
            'we':['ናልና','us','for us'],
            'i':['ናለይ','me','for me'],
            'you_m':['ናልካ','you','for you'],
            'you_m_2':['ናልኩም','you','for you'],
            'you_f':['ናልኪ','you','for you'],
            'you_f_2':['ናልክን','you','for you'],
            'starts':{
                'present':['ይ'],
                'future':['ክ'],
            },
            'ends_future_present':[4],
            'ends_stem_past':['ን']
            
        },
        'we':{
            'he':['ናሉ','him','for him'],
            'she':['ናላ','her','for her'],
            'they':['ናሎም','them','for them'],
            'they_2':['ናለን','them','for them'],
            'we':['ናልኩም','us','for us'],
            'i':['ኩምለይ','me','for me'],
            'you_m':['ናልካ','you','for you'],
            'you_m_2':['ናልኩም','you','for you'],
            'you_f':['ናልኪ','you','for you'],
            'you_f_2':['ናክን','you','for you'],
            'starts':{
                'present':['ን'],
                'future':['ክን'],
                'past':['ን']
            },
            'ends_future_present':[6],
            'ends_stem_past':['ና']
            
        },
        'i':{
            'he':['ሉ','him','for him'],
            'she':['ላ','her','for her'],
            'they':['ሎም','them','for them'],
            'they_2':['ለን','them','for them'],
            'we':['ልኩም','us','for us'],
            'i':['ካለይ','me','to me'],
            'you_m':['ልካ','you','for you'],
            'you_m_2':['ልኩም','you','for you'],
            'you_f':['ልኪ','you','for you'],
            'you_f_2':['ልክን','you','for you'],
            'starts':{
                'present':['ይ'],
                'future':['ክ'],
                'past':[]
            },
            'ends_future_present':[6],
            'ends_stem_past':[1]
            
        }
    }
]
word_ends_with_future_and_present_tense = [
    {
        'you_m': {
            'he': [7, 'him', 'to him'],
            'she': [4, 'her', 'to her'],
            'they': ['7ም', 'them', 'to them'],
            'they_2': ['1ን', 'them', 'to them'],
            'we': ['1ና', 'us', 'to us'],
            'i': ['1ኒ', 'me', 'to me'],
        },
        'you_f': {
            'he': ['6ዮ', 'him', 'to him'],
            'she': ['6ያ', 'her', 'to her'],
            'they': ['6ዮም', 'them', 'to them'],
            'they_2': ['6የን', 'them', 'to them'],
            'we': ['6ና', 'us', 'to us'],
            'i': ['6ኒ', 'me', 'to me'],
        },
        'you_m_2':{
            'he':['6ዎ','him','to him'],
            'she':['6ዋ','her','to her'],
            'they':['6ዎም','them','to them'],
            'they_2':['6ወን','them','to them'],
            'we':['2ና','us','to us'],
            'i':['2ኒ','me','to me'],
        },
        'you_f_2':{
            'he':['6ኦ','him','to him'],
            'she':['6ኣ','her','to her'],
            'they':['6ኦም','them','to them'],
            'they_2':['6አን','them','to them'],
            'we':['4ና','us','to us'],
            'i':['4ኒ','me','to me'],
        },
        'he':{
            'he':[7,'him','to him'],
            'she':[4,'her','to her'],
            'they':['7ም','them','to them'],
            'they_2':['1ን','them','to them'],
            'we':['1ና','us','to us'],
            'i':['1ኒ','me','to me'],
            'you_m':['1ካ','you','to you'],
            'you_m_2':['1ኩም','you','to you'],
            'you_f':['1ኪ','you','to you'],
            'you_f_2':['1ክን','you','to you'],
        },
        'she':{
            'he':[7,'him','to him'],
            'she':[4,'her','to her'],
            'they':['7ም','them','to them'],
            'they_2':['1ን','them','to them'],
            'we':['1ና','us','to us'],
            'i':['1ኒ','me','to me'],
            'you_m':['1ካ','you','to you'],
            'you_m_2':['1ኩም','you','to you'],
            'you_f':['1ኪ','you','to you'],
            'you_f_2':['1ክን','you','to you'],
        },
        'they':{
            'he':['ዎ','him','to him'],
            'she':['ዋ','her','to her'],
            'they':['ዎም','them','to them'],
            'they_2':['ወን','them','to them'],
            'we':['2ና','us','to us'],
            'i':['2ኒ','me','to me'],
            'you_m':['2ኻ','you','to you'],
            'you_m_2':['2ኹም','you','to you'],
            'you_f':['2ኺ','you','to you'],
            'you_f_2':['2ኽን','you','to you'],
        },
        'they_2': {
            'he': ['6ኦ', 'him', 'to him'],
            'she': ['6ኣ', 'her', 'to her'],
            'they': ['6ኦም', 'them', 'to them'],
            'they_2': ['6አን', 'them', 'to them'],
            'we': ['4ና', 'us', 'to us'],
            'i': ['4ኒ', 'me', 'to me'],
            'you_m': ['4ኻ', 'you', 'to you'],
            'you_m_2': ['4ኹም', 'you', 'to you'],
            'you_f': ['4ኺ', 'you', 'to you'],
            'you_f_2': ['4ኽን', 'you', 'to you'],
        },
        'we':{
            'he':[7,'him','to him'],
            'she':[4,'her','to her'],
            'they':['7ም','them','to them'],
            'they_2':['1የን','them','to them'],
            'we':['1ኩም','us','to us'],
            'i':['2ካ','me','to me'],
            'you_m':['1ካ','you','to you'],
            'you_m_2':['1ኩም','you','to you'],
            'you_f':['1ኪ','you','to you'],
            'you_f_2':['1ክን','you','to you'],
        },
        'i':{
            'he':[7,'him','to him'],
            'she':[4,'her','to her'],
            'they':['7ም','them','to them'],
            'they_2':['1ን','them','to them'],
            'we':['1ኩም','us','to us'],
            'i':['1ኒ','me','to me'],
            'you_m':['1ካ','you','to you'],
            'you_m_2':['1ኩም','you','to you'],
            'you_f':['1ኪ','you','to you'],
            'you_f_2':['1ክን','you','to you'],
        }
    }
]

word_ends_with_future_and_present_tense = [
    {
        'you_m':{
            'he':['1ሉ','him','for him'],
            'she':['1ላ','her','for her'],
            'they':['1ሎም','them','for them'],
            'they_2':['1ለን','them','for them'],
            'we':['1ልና','us','for us'],
            'i':['1ለይ','me','for me'],
        },
        'you_f':{
            'he':['6ሉ','him','for him'],
            'she':['6ላ','her','for her'],
            'they':['6ሎም','them','for them'],
            'they_2':['6ለን','them','for them'],
            'we':['6ልና','us','for us'],
            'i':['6ለይ','me','for me'],
        },
        'you_m_2':{
            'he':['6ሉ','him','for him'],
            'she':['2ላ','her','for her'],
            'they':['2ሎም','them','for them'],
            'they_2':['2ለን','them','for them'],
            'we':['2ልና','us','for us'],
            'i':['2ለይ','me','for me'],
        },
        'you_f_2':{
            'he':['4ሉ','him','for him'],
            'she':['4ላ','her','for her'],
            'they':['4ሎም','them','for them'],
            'they_2':['4ለን','them','for them'],
            'we':['4ልና','us','for us'],
            'i':['4ለይ','me','for me'],
        },
        'he':{
            'he':['1ሉ','him','for him'],
            'she':['1ላ','her','for her'],
            'they':['1ሎም','them','for them'],
            'they_2':['1ለን','them','for them'],
            'we':['1ልና','us','for us'],
            'i':['1ለይ','me','for me'],
            'you_m':['1ልካ','you','for you'],
            'you_m_2':['1ልኩም','you','for you'],
            'you_f':['1ልኪ','you','for you'],
            'you_f_2':['1ልክን','you','for you'],
        },
        'she':{
            'he':['1ሉ','him','for him'],
            'she':['1ላ','her','for her'],
            'they':['1ሎም','them','for them'],
            'they_2':['1ለን','them','for them'],
            'we':['1ልና','us','for us'],
            'i':['1ለይ','me','for me'],
            'you_m':['1ልካ','you','for you'],
            'you_m_2':['1ልኩም','you','for you'],
            'you_f':['1ልኪ','you','for you'],
            'you_f_2':['1ልክን','you','for you'],
        },
        'they':{
            'he':['6ሉ','him','for him'],
            'she':['2ላ','her','for her'],
            'they':['6ሎም','them','for them'],
            'they_2':['2ለን','them','for them'],
            'we':['2ልና','us','for us'],
            'i':['2ለይ','me','for me'],
            'you_m':['2ልካ','you','for you'],
            'you_m_2':['2ልኹም','you','for you'],
            'you_f':['2ልኺ','you','for you'],
            'you_f_2':['2ልኽን','you','for you'],
        },
        'they_2': {
            'he': ['4ሉ', 'him', 'for him'],
            'she': ['4ላ', 'her', 'for her'],
            'they': ['4ሎም', 'them', 'for them'],
            'they_2': ['4ለን', 'them', 'for them'],
            'we': ['4ልና', 'us', 'for us'],
            'i': ['4ለይ', 'me', 'for me'],
            'you_m': ['4ልካ', 'you', 'for you'],
            'you_m_2': ['4ልኩም', 'you', 'for you'],
            'you_f': ['4ልኪ', 'you', 'for you'],
            'you_f_2': ['4ልክን', 'you', 'for you'],
        },
        'we':{
            'he':['1ሉ','him','for him'],
            'she':['1ላ','her','for her'],
            'they':['1ሎም','them','for them'],
            'they_2':['1ለን','them','for them'],
            'we':['1ልኩም','us','for us'],
            'i':['2ለይ','me','for me'],
            'you_m':['1ልካ','you','for you'],
            'you_m_2':['1ልኩም','you','for you'],
            'you_f':['1ልኪ','you','for you'],
            'you_f_2':['1ልክን','you','for you'],
        },
        'i':{
            'he':['1ሉ','him','for him'],
            'she':['1ላ','her','for her'],
            'they':['1ሎም','them','for them'],
            'they_2':['1ለን','them','for them'],
            'we':['1ልኩም','us','for us'],
            'i':['1ለይ','me','for me'],
            'you_m':['1ልካ','you','for you'],
            'you_m_2':['1ልኩም','you','for you'],
            'you_f':['1ልኪ','you','for you'],
            'you_f_2':['1ልክን','you','for you'],
        }
    }
]
word_ends_with_future_and_present_tense_ley=[
    {
        'you_m':{
            'he':['1ሉ','him','for him'],
            'she':['1ላ','her','for her'],
            'they':['1ሎም','them','for them'],
            'they_2':['1ለን','them','for them'],
            'we':['1ልና','us','for us'],
            'i':['1ለይ','me','for me'],
        },
        'you_f':{
            'he':['6ሉ','him','for him'],
            'she':['6ላ','her','for her'],
            'they':['6ሎም','them','for them'],
            'they_2':['6ለን','them','for them'],
            'we':['6ልና','us','for us'],
            'i':['6ለይ','me','for me'],
        },
        'you_m_2':{
            'he':['6ሉ','him','for him'],
            'she':['2ላ','her','for her'],
            'they':['2ሎም','them','for them'],
            'they_2':['2ለን','them','for them'],
            'we':['2ልና','us','for us'],
            'i':['2ለይ','me','for me'],
        },
        'you_f_2':{
            'he':['4ሉ','him','for him'],
            'she':['4ላ','her','for her'],
            'they':['4ሎም','them','for them'],
            'they_2':['4ለን','them','for them'],
            'we':['4ልና','us','for us'],
            'i':['4ለይ','me','for me'],
        },
        'he':{
            'he':['1ሉ','him','for him'],
            'she':['1ላ','her','for her'],
            'they':['1ሎም','them','for them'],
            'they_2':['1ለን','them','for them'],
            'we':['1ልና','us','for us'],
            'i':['1ለይ','me','for me'],
            'you_m':['1ልካ','you','for you'],
            'you_m_2':['1ልኩም','you','for you'],
            'you_f':['1ልኪ','you','for you'],
            'you_f_2':['1ልክን','you','for you'],
        },
        'she':{
            'he':['1ሉ','him','for him'],
            'she':['1ላ','her','for her'],
            'they':['1ሎም','them','for them'],
            'they_2':['1ለን','them','for them'],
            'we':['1ልና','us','for us'],
            'i':['1ለይ','me','for me'],
            'you_m':['1ልካ','you','for you'],
            'you_m_2':['1ልኩም','you','for you'],
            'you_f':['1ልኪ','you','for you'],
            'you_f_2':['1ልክን','you','for you'],
        },
        'they':{
            'he':['6ሉ','him','for him'],
            'she':['2ላ','her','for her'],
            'they':['6ሎም','them','for them'],
            'they_2':['2ለን','them','for them'],
            'we':['2ልና','us','for us'],
            'i':['2ለይ','me','for me'],
            'you_m':['2ልካ','you','for you'],
            'you_m_2':['2ልኹም','you','for you'],
            'you_f':['2ልኺ','you','for you'],
            'you_f_2':['2ልኽን','you','for you'],
        },
        'they_2': {
        'he': ['4ሉ', 'him', 'for him'],
        'she': ['4ላ', 'her', 'for her'],
        'they': ['4ሎም', 'them', 'for them'],
        'they_2': ['4ለን', 'them', 'for them'],
        'we': ['4ልና', 'us', 'for us'],
        'i': ['4ለይ', 'me', 'for me'],
        'you_m': ['4ልካ', 'you', 'for you'],
        'you_m_2': ['4ልኩም', 'you', 'for you'],
        'you_f': ['4ልኪ', 'you', 'for you'],
        'you_f_2': ['4ልክን', 'you', 'for you']
        },
        'we':{
            'he':['1ሉ','him','for him'],
            'she':['1ላ','her','for her'],
            'they':['1ሎም','them','for them'],
            'they_2':['1ለን','them','for them'],
            'we':['1ልኩም','us','for us'],
            'i':['2ለይ','me','for me'],
            'you_m':['1ልካ','you','for you'],
            'you_m_2':['1ልኩም','you','for you'],
            'you_f':['1ልኪ','you','for you'],
            'you_f_2':['1ልክን','you','for you'],
        },
        'i':{
            'he':['1ሉ','him','for him'],
            'she':['1ላ','her','for her'],
            'they':['1ሎም','them','for them'],
            'they_2':['1ለን','them','for them'],
            'we':['1ልኩም','us','for us'],
            'i':['1ለይ','me','for me'],
            'you_m':['1ልካ','you','for you'],
            'you_m_2':['1ልኩም','you','for you'],
            'you_f':['1ልኪ','you','for you'],
            'you_f_2':['1ልክን','you','for you'],
        }
    }
]
verbs_length_2=["ሾመ","ኢሉ","በለ","ሓዘ","ዖደ","ቆመ","ኰነ","ኮነ","ኾነ","ገረ","ጌረ","ጾረ","ሞተ","ወጸ","ሃበ","ዖለ","ገሸ","ጾመ","ጸመ","ኮነ",
    "ሸነ","ሸመ","ሸጠ","ዞረ","መቘ","ከደ","ኸደ","ጋዛ","ጠሸ","ሞቐ","ፋጻ","መጸ","ባጫ","ጕየ","ሸኻ","ሒሕ",
    "ዔገ","ዋዒ","ቈመ","ኾነ","ናቱ","ነው","ቦታ","ነጽ","ዕዳ","ጭጭ"]
def verbs_with_length2_modifier(info):
    tigrinaSen = info.split(' ')
    default_value = None
    for key in range(len(tigrinaSen)):
        wordFromSentence = list(tigrinaSen[key])
        # firstLetterFromSentenceWord = wordFromSentence[0]
        # secondLetterFromSentenceWord = wordFromSentence[1]
        # thirdLetterFromSentenceWord = wordFromSentence[2]
        # fourthLetterFromSentenceWord = wordFromSentence[3]
        # fifthLetterFromSentenceWord = wordFromSentence[4]
        # sixthLetterFromSentenceWord = wordFromSentence[5]
        firstLetterFromSentenceWord = wordFromSentence[0] if len(wordFromSentence) > 0 else default_value
        secondLetterFromSentenceWord = wordFromSentence[1] if len(wordFromSentence) > 1 else default_value
        thirdLetterFromSentenceWord = wordFromSentence[2] if len(wordFromSentence) > 2 else default_value
        fourthLetterFromSentenceWord = wordFromSentence[3] if len(wordFromSentence) > 3 else default_value
        fifthLetterFromSentenceWord = wordFromSentence[4] if len(wordFromSentence) > 4 else default_value
        sixthLetterFromSentenceWord = wordFromSentence[5] if len(wordFromSentence) > 5 else default_value
        
        default_value_2 = ''  # or any other string you want to use as default
        # combination = firstLetterFromSentenceWord + secondLetterFromSentenceWord
        # combinationOfThree = firstLetterFromSentenceWord + secondLetterFromSentenceWord + thirdLetterFromSentenceWord
        # combinationOfFour = firstLetterFromSentenceWord + secondLetterFromSentenceWord + thirdLetterFromSentenceWord + fourthLetterFromSentenceWord
        # combinationOfFive = combinationOfFour + fifthLetterFromSentenceWord
        # combinationOfSix = combinationOfFive + sixthLetterFromSentenceWord
        
        combination = firstLetterFromSentenceWord + (secondLetterFromSentenceWord or default_value_2)
        combinationOfThree = firstLetterFromSentenceWord + (secondLetterFromSentenceWord or default_value_2 + thirdLetterFromSentenceWord or default_value_2)
        combinationOfFour = firstLetterFromSentenceWord + (secondLetterFromSentenceWord or default_value_2 + thirdLetterFromSentenceWord or default_value_2 + fourthLetterFromSentenceWord or default_value_2)
        
        combinationOfFive = combinationOfFour + (fifthLetterFromSentenceWord or default_value_2)
        combinationOfSix = combinationOfFive + (sixthLetterFromSentenceWord or default_value_2)
        aykn = 'ኣይክን'
        aykt = 'ኣይክት'
        ayk = 'ኣይክ'
        keyt = 'ከይት'
        keyn = 'ከይን'
        zeyn = 'ዘይን'
        zeyt = 'ዘይት'
        zeym = 'ዘይም'
        zeykn = 'ዘይክን'
        zeykt = 'ዘይክት'
        addingCombinationLater = ''
        negativeExcludes = ["ኣይ", "ከይ", "ዘይ", "ክት", "ክን"]
        negativeExcludes2_mszey = 'ምስዘይ'
        negativeExcludes2_mszeyn = 'ምስዘይን'
        negativeExcludes2_mszeyt = 'ምስዘይት'
        negativeExcludes2_kemzey = 'ከምዘይ'
        negativeExcludes2_kemzeyn = 'ከምዘይን'
        negativeExcludes2_kemzeyt = 'ከምዘይት'
        excludes2_kemz = 'ከምዝ'
        excludes2_kemd = 'ከምድ'
        excludes2_msz = 'ምስዝ'
        excludes2_mst = 'ምስት'
        excludes2_msn = 'ምስን'
        excludes2_ms = 'ምስ'
        excludes2_kemt = 'ከምት'
        excludes2_kemn = 'ከምን'
        excludes = ["ክ", 'ት', 'ይ', 'ም', 'ኽ']
        ente = 'እንተ'
        entez = 'እንተዝ'
        entet = 'እንተት'
        enten = 'እንተን'
        entezey = 'እንተዘይ'
        entezeyt = 'እንተዘይት'
        entezeyn = 'እንተዘይን'
        ambey = 'ኣምበይ'
        z = 'ዝ'
        ze = 'ዘ'
        if combination in negativeExcludes:
            if combination == 'ከይ':
                localExcludes = ['ከይደ', 'ከይዱ', 'ከይዲ', 'ከይዳ', 'ከይዶም', 'ከይደን', 'ከይድና']
                if tigrinaSen[key] in localExcludes:
                    addingCombinationLater = ""
                else:
                    addingCombinationLater = combination
                    wordFromSentence.pop(0)
            else:
                addingCombinationLater = combination
                wordFromSentence.pop(0)
        elif firstLetterFromSentenceWord in excludes:
            addingCombinationLater = firstLetterFromSentenceWord
            wordFromSentence.pop(0)
        if excludes2_kemz == combinationOfThree or excludes2_kemt == combinationOfThree or excludes2_kemn == combinationOfThree or excludes2_kemd == combinationOfThree:
            addingCombinationLater = combinationOfThree
            wordFromSentence.pop(0)
        elif excludes2_ms == combination:
            addingCombinationLater = combination
            wordFromSentence.pop(0)
        elif excludes2_msz == combinationOfThree or excludes2_mst == combinationOfThree or excludes2_msn == combinationOfThree:
            addingCombinationLater = combinationOfThree
            wordFromSentence.pop(0)
        elif keyn == combinationOfThree or keyt == combinationOfThree or zeyn == combinationOfThree or zeyt == combinationOfThree or ayk == combinationOfThree or zeym == combinationOfThree:
            addingCombinationLater = combinationOfThree
            wordFromSentence.pop(0)
        if negativeExcludes2_kemzey == combinationOfFour:
            addingCombinationLater = combinationOfFour
            wordFromSentence.pop(0)
        elif negativeExcludes2_mszey == combinationOfFour:
            addingCombinationLater = combinationOfFour
            wordFromSentence.pop(0)
        elif aykn == combinationOfFour or aykt == combinationOfFour or zeykn == combinationOfFour or zeykt == combinationOfFour:
            addingCombinationLater = combinationOfFour
            wordFromSentence.pop(0)
        if ambey == combinationOfFour:
            addingCombinationLater = combinationOfFour
            wordFromSentence.pop(0)
        if z == firstLetterFromSentenceWord or ze == firstLetterFromSentenceWord:
            addingCombinationLater = firstLetterFromSentenceWord
            wordFromSentence.pop(0)
        if ente == combinationOfThree:
            if entez == combinationOfFour or entet == combinationOfFour or enten == combinationOfFour:
                addingCombinationLater = combinationOfFour
                wordFromSentence.pop(0)
            elif entezey == combinationOfFive:
                if entezeyt == combinationOfSix:
                    addingCombinationLater = combinationOfSix
                    wordFromSentence.pop(0)
                elif entezeyn == combinationOfSix:
                    addingCombinationLater = combinationOfSix
                    wordFromSentence.pop(0)
                else:
                    addingCombinationLater = combinationOfFive
                    wordFromSentence.pop(0)
            else:
                addingCombinationLater = combinationOfThree
                wordFromSentence.pop(0)
        if negativeExcludes2_mszeyn == combinationOfFive or negativeExcludes2_kemzeyn == combinationOfFive or negativeExcludes2_mszeyt == combinationOfFive or negativeExcludes2_kemzeyt == combinationOfFive:
            addingCombinationLater = combinationOfFive
            wordFromSentence.pop(0)
        if len(wordFromSentence) > 2:
            for key2 in range(len(verbs_length_2)):
                wordFromVerb = list(verbs_length_2[key2])
                if wordFromVerb[0] == wordFromSentence[0]:
                    if wordFromSentence[1] == 'ይ' or wordFromSentence[1] == 'ው':
                        thirdWord = wordFromVerb[1]
                        indexOfThirdWord = alphabet_info.tigrina_alphabets.index(thirdWord)
                        family = []
                        alphabet_info_result=get_alphabet_info.get_alphabet(thirdWord)
                        family.append(alphabet_info_result['first'])
                        family.append(alphabet_info_result['second'])
                        family.append(alphabet_info_result['third'])
                        family.append(alphabet_info_result['fourth'])
                        family.append(alphabet_info_result['fifth'])
                        family.append(alphabet_info_result['sixth'])
                        if wordFromSentence[2] in family:
                            indexOfY = wordFromSentence.index(wordFromSentence[1])
                            wordFromSentence.pop(indexOfY)
                            newWord = addingCombinationLater + wordFromSentence
                            tigrinaSen[key] = ''.join(newWord)
                    else:
                        tigrinaSen[key] = addingCombinationLater + ''.join(wordFromSentence)
    return tigrinaSen
wordInfo = {}
def front_text_cut_offs(info):
    # Extract the word from the input dictionary
    mytext = list(info['word'])

    # Initialize the letters based on the word length
    first_letter = mytext[0] if len(mytext) > 0 else ""
    second_letter = mytext[1] if len(mytext) > 1 else ""
    third_letter = mytext[2] if len(mytext) > 2 else ""
    fourth_letter = mytext[3] if len(mytext) > 3 else ""
    fifth_letter = mytext[4] if len(mytext) > 4 else ""
    sixth_letter = mytext[5] if len(mytext) > 5 else ""

    # Create combinations of letters
    combination_two = first_letter + second_letter
    combination_three = combination_two + third_letter if third_letter != "" else ""
    combination_four = combination_three + fourth_letter if fourth_letter != "" else ""
    combination_five = combination_four + fifth_letter if fifth_letter != "" else ""
    combination_six = combination_five + sixth_letter if sixth_letter != "" else ""

    combinations_collection = [first_letter, combination_two, combination_three, combination_four, combination_five]
    founds = []

    # Check for matching combinations in all_front_remove_collection
    for item in alphabet_info['all_front_remove_collection']:
        for combo in combinations_collection:
            if item == combo:
                founds.append(item)
    
    # Determine the longest matching string (cutoff)
    cutoff = ""
    if founds:
        cutoff = longest_str_in_array(founds)
    
    # Slice the word after the cutoff
    word = ''.join(mytext)[len(cutoff):]
    
    # Return the modified word info
    return {
        'frontErases1': cutoff,
        'wordAfterErases1': word
    }
def longest_str_in_array(arra):
    max_str = len(arra[0])
    ans = arra[0]
    for i in range(1, len(arra)):
        maxi = len(arra[i])
        if maxi > max_str:
            ans = arra[i]
            max_str = maxi
    return ans

def stem_futurePresentPastCoder(code, lastLetter, lastLetterCode, secondLetter, secondLetterCode, sentenceType):
    print("code:",code)
    secondCodeCheckup = str(lastLetterCode) + lastLetter
    thridTriesCodeCheckup = str(secondLetterCode) + lastLetter
    fourthTriesCodeCheckup = str(secondLetterCode) + secondLetter
    codes = [code, secondCodeCheckup, thridTriesCodeCheckup, fourthTriesCodeCheckup]
    print("codes:",codes)
    stem_future_present_past = [
        {
            'you_m': {
                'future': ['ክት', '6'],
                'present': ['ት', '6'],
                'past': ['6', 'ካ']
            },
            'you_m_2': {
                'future': ['ክት', '2'],
                'present': ['ት', '2'],
                'past': ['6', 'ኩም']
            },
            'you_f': {
                'future': ['ክት', '3'],
                'present': ['ት', '3'],
                'past': ['6', 'ኪ']
            },
            'you_f_2': {
                'future': ['ክት', '4'],
                'present': ['ት', '4'],
                'past': ['6', 'ክን']
            },
            'he': {
                'future': ['ክ', '6'],
                'present': ['ይ', '6'],
                'past': ['2']
            },
            'she': {
                'future': ['ክት', '6'],
                'present': ['ት', '6'],
                'past': ['4']
            },
            'they': {
                'future': ['ክ', '2'],
                'present': ['ይ', '2'],
                'past': ['7', 'ም']
            },
            'they_2': {
                'future': ['ክ', '4'],
                'present': ['ይ', '4'],
                'past': ['1', 'ን']
            },
            'we': {
                'future': ['ክን', '6'],
                'present': ['ን', '6'],
                'past': ['6', 'ና']
            },
            'i': {
                'future': ['ክ', '6'],
                'present': ['ይ', '6'],
                'past': ['1'],
                'past2': ['6', 'ኩ']
            }
        }
    ]
    codeInfo = {}
    found = False
    if sentenceType == 'future':
        for item in stem_future_present_past:
            if codes.count(''.join(item['you_m']['future'])) or codes.count(''.join(item['you_m_2']['future'])) or codes.count(''.join(item['you_f']['future'])) or codes.count(''.join(item['you_f_2']['future'])):
                codeInfo['pronoun'] = 'you'
                found = True
            elif codes.count(''.join(item['he']['future'])):
                codeInfo['pronoun'] = 'he'
                found = True
            elif codes.count(''.join(item['she']['future'])):
                codeInfo['pronoun'] = 'she'
                found = True
            elif codes.count(''.join(item['they']['future'])) or codes.count(''.join(item['they_2']['future'])):
                codeInfo['pronoun'] = 'they'
                found = True
            elif codes.count(''.join(item['we']['future'])):
                codeInfo['pronoun'] = 'we'
                found = True
            elif codes.count(''.join(item['i']['future'])):
                codeInfo['pronoun'] = 'i'
                found = True
    elif sentenceType == 'present':
        for item in stem_future_present_past:
            if codes.count(''.join(item['you_m']['present'])) or codes.count(''.join(item['you_m_2']['present'])) or codes.count(''.join(item['you_f']['present'])) or codes.count(''.join(item['you_f_2']['present'])):
                codeInfo['pronoun'] = 'you'
                found = True
            elif codes.count(''.join(item['he']['present'])):
                codeInfo['pronoun'] = 'he'
                found = True
            elif codes.count(''.join(item['she']['present'])):
                codeInfo['pronoun'] = 'she'
                found = True
            elif codes.count(''.join(item['they']['present'])) or codes.count(''.join(item['they_2']['present'])):
                codeInfo['pronoun'] = 'they'
                found = True
            elif codes.count(''.join(item['we']['present'])):

                codeInfo['pronoun'] = 'we'
                found = True
            elif codes.count(''.join(item['i']['present'])):
                codeInfo['pronoun'] = 'i'
                found = True
    elif sentenceType == 'past':
        for item in stem_future_present_past:
            if code == ''.join(item['you_m']['past']) or code == ''.join(item['you_m_2']['past']) or code == ''.join(item['you_f']['past']) or code == ''.join(item['you_f_2']['past']):
                codeInfo['pronoun'] = 'you'
                codeInfo['removes'] = code
                found = True
            elif code == ''.join(item['he']['past']):
                codeInfo['pronoun'] = 'he'
                codeInfo['removes'] = code
                found = True
            elif code == ''.join(item['she']['past']):
                codeInfo['pronoun'] = 'she'
                codeInfo['removes'] = code
                found = True
            elif code == ''.join(item['they']['past']) or code == ''.join(item['they_2']['past']):
                codeInfo['pronoun'] = 'they'
                codeInfo['removes'] = code
                found = True
            elif code == ''.join(item['we']['past']):
                codeInfo['pronoun'] = 'we'
                codeInfo['removes'] = code
                found = True
            elif code == ''.join(item['i']['past']) or code == ''.join(item['i']['past2']):
                codeInfo['pronoun'] = 'i'
                codeInfo['removes'] = code
                found = True
            if not found:
                if codes.count(''.join(item['you_m']['past'])) or codes.count(''.join(item['you_m_2']['past'])) or codes.count(''.join(item['you_f']['past'])) or codes.count(''.join(item['you_f_2']['past'])):
                    codeInfo['pronoun'] = 'you'
                    if codes.count(''.join(item['you_m_2']['past'])):
                        codeInfo['removes'] = ''.join(item['you_m_2']['past'])
                    elif codes.count(''.join(item['you_m']['past'])):
                        codeInfo['removes'] = ''.join(item['you_m']['past'])
                    elif codes.count(''.join(item['you_f']['past'])):
                        codeInfo['removes'] = ''.join(item['you_f']['past'])
                    elif codes.count(''.join(item['you_f_2']['past'])):
                        codeInfo['removes'] = ''.join(item['you_f_2']['past'])
                    found = True
                elif codes.count(''.join(item['he']['past'])):
                    codeInfo['pronoun'] = 'he'
                    codeInfo['removes'] = ''.join(item['he']['past'])
                    found = True
                elif codes.count(''.join(item['she']['past'])):
                    codeInfo['pronoun'] = 'she'
                    codeInfo['removes'] = ''.join(item['she']['past'])
                    found = True
                elif codes.count(''.join(item['they']['past'])) or codes.count(''.join(item['they_2']['past'])):
                    codeInfo['pronoun'] = 'they'
                    codeInfo['removes'] = ''.join(item['they']['past'])
                    if codes.count(''.join(item['they_2']['past'])):
                        codeInfo['removes'] = ''.join(item['they_2']['past'])
                    found = True
                elif codes.count(''.join(item['we']['past'])):
                    codeInfo['pronoun'] = 'we'
                    codeInfo['removes'] = ''.join(item['we']['past'])
                    found = True
                elif codes.count(''.join(item['i']['past'])) or codes.count(''.join(item['i']['past2'])):
                    codeInfo['pronoun'] = 'i'
                    codeInfo['removes'] = ''.join(item['i']['past'])
                    found = True
    answer = []
    if found:
        answer.append(codeInfo)
    return answer

def sentence_identifier_and_front_text_cut_off2(textInfo):
    word = list(textInfo['wordAfterErases1'])
    firstLetter=""
    if word:
        firstLetter = word[0]
    secondLetter=""
    if len(word) > 1:
      secondLetter = word[1]
    thirdLetter = ""
    if len(word) > 3:
        thirdLetter = word[2]
    combination = firstLetter + secondLetter
    combinationthree = ""
    if thirdLetter != "":
        combinationthree = combination + thirdLetter
    founds = []
    combinationsCollection = [firstLetter, combination, combinationthree]
    fronts = ['ይ', 'ክ', 'ት', 'ክት', 'ንከነ', 'ንኸነ', 'ን', 'ክን', 'ኽን', 'ንክን', 'ንክ', 'ንኽ', 'ንኽን']
    for item in fronts:
        for key in range(len(combinationsCollection)):
            if item == combinationsCollection[key]:
                founds.append(item)
    cutoff = ""
    if len(founds) != 0:
        cutoff = max(founds, key=len)
    word2 = ''.join(word).lstrip(cutoff)
    if cutoff == 'ይ' or cutoff == 'ን' or cutoff == 'ት':
        wordInfo['sentenceType'] = 'present'
    elif cutoff == 'ክ' or cutoff == 'ክን' or cutoff == 'ክት':
        wordInfo['sentenceType'] = 'future'
    else:
        wordInfo['sentenceType'] = 'past'
    wordInfo['frontErases2'] = cutoff
    wordInfo['wordAfterErases2'] = word2
    return wordInfo


def ends_with_self_explaining_or_stem_expression(info):
    # print("infoff:",info)
    cutoff=""
    founds=[]
    newCombination=[]
    for item in info['combinationsCollection']:
        if info['lastLetter']=='ን' or info['lastLetter']=='ም' or info['lastLetter']=='ና':
            item = str(info['secondFromLastLetterOrderIs']) + item
        else:
            item = str(info['lastLetterOrderIs']) + item
        newCombination.append(item)
    
    for item in info['data']:
        for key in range(len(newCombination)):
            if item == newCombination[key]:
                founds.append(item)
    
    if len(founds) != 0:
        cutoff = max(founds, key=len)
    
    results = {}
    guesPronounFromCode = stem_futurePresentPastCoder(str(info['code']), str(info['lastLetter']), str(info['lastLetterOrderIs']), str(info['secondFromLastLetter']), str(info['secondFromLastLetterOrderIs']), str(info['sentenceType']))
    if len(guesPronounFromCode) != 0:
        results['pronoun'] = guesPronounFromCode[0]['pronoun']
        if 'removes' in guesPronounFromCode[0]:
            cutoff = guesPronounFromCode[0]['removes']
    
    if cutoff !="":
        results['cutoff'] = cutoff[0]
    else:
       results['cutoff'] = ""
    return results

def ends_and_pronoun_matcher_on_talking_to_someone(data, word, lastLetterOrderIs, sentenceType, frontErase, lastLetter, secondLastLetter):
    answer = []
    if sentenceType != 'past':
        if word == '':
            word = lastLetterOrderIs
        else:
            word = str(lastLetterOrderIs) + word

    if data[0]['you_m']['he'][0] == word:
        answer.append({'toMatcher': data[0]['you_m']['he'], 'pronoun': 'you'})
    if data[0]['you_m']['she'][0] == word:
        answer.append({'toMatcher': data[0]['you_m']['she'], 'pronoun': 'you'})
    if data[0]['you_m']['they'][0] == word:
        answer.append({'toMatcher': data[0]['you_m']['they'], 'pronoun': 'you'})
    if data[0]['you_m']['they_2'][0] == word:
        answer.append({'toMatcher': data[0]['you_m']['they_2'], 'pronoun': 'you'})
    if data[0]['you_m']['we'][0] == word:
        answer.append({'toMatcher': data[0]['you_m']['we'], 'pronoun': 'you'})
    if data[0]['you_m']['i'][0] == word:
        answer.append({'toMatcher': data[0]['you_m']['i'], 'pronoun': 'you'})
    if data[0]['you_m_2']['he'][0] == word:
        answer.append({'toMatcher': data[0]['you_m_2']['he'], 'pronoun': 'you'})
    if data[0]['you_m_2']['she'][0] == word:
        answer.append({'toMatcher': data[0]['you_m_2']['she'], 'pronoun': 'you'})
    if word in data[0]['you_m_2']['they'][0]:
        answer.append({'toMatcher': data[0]['you_m_2']['they'], 'pronoun': 'you'})
    if data[0]['you_m_2']['they_2'][0] == word:
        answer.append({'toMatcher': data[0]['you_m_2']['they_2'], 'pronoun': 'you'})
    if data[0]['you_m_2']['we'][0] == word:
        answer.append({'toMatcher': data[0]['you_m_2']['we'], 'pronoun': 'you'})
    if data[0]['you_m_2']['i'][0] == word:
        answer.append({'toMatcher': data[0]['you_m_2']['i'], 'pronoun': 'you'})
    if data[0]['you_f']['he'][0] == word:
        answer.append({'toMatcher': data[0]['you_f']['he'], 'pronoun': 'you'})
    if data[0]['you_f']['she'][0] == word:
        answer.append({'toMatcher': data[0]['you_f']['she'], 'pronoun': 'you'})
    if data[0]['you_f']['they'][0] == word:
        answer.append({'toMatcher': data[0]['you_f']['they'], 'pronoun': 'you'})
    if data[0]['you_f']['they_2'][0] == word:
        answer.append({'toMatcher': data[0]['you_f']['they_2'], 'pronoun': 'you'})
    if data[0]['you_f']['we'][0] == word:
        answer.append({'toMatcher': data[0]['you_f']['we'], 'pronoun': 'you'})
    if data[0]['you_f']['i'][0] == word:
        answer.append({'toMatcher': data[0]['you_f']['i'], 'pronoun': 'you'})
    if data[0]['you_f_2']['he'][0] == word:
        answer.append({'toMatcher': data[0]['you_f_2']['he'], 'pronoun': 'you'})
    if data[0]['you_f_2']['she'][0] == word:
        answer.append({'toMatcher': data[0]['you_f_2']['she'], 'pronoun': 'you'})
    if data[0]['you_f_2']['they'][0] == word:
        answer.append({'toMatcher': data[0]['you_f_2']['they'], 'pronoun': 'you'})
    if data[0]['you_f_2']['they_2'][0] == word:
        answer.append({'toMatcher': data[0]['you_f_2']['they'], 'pronoun': 'you'})
    if data[0]['you_f_2']['we'][0] == word:
        answer.append({'toMatcher': data[0]['you_f_2']['we'], 'pronoun': 'you'})
    if data[0]['you_f_2']['i'][0] == word:
        answer.append({'toMatcher': data[0]['you_f_2']['i'], 'pronoun': 'you'})
    if data[0]['he']['he'][0] == word:
        answer.append({'toMatcher': data[0]['he']['he'], 'pronoun': 'he'})
    if data[0]['he']['she'][0] == word:
        answer.append({'toMatcher': data[0]['he']['she'], 'pronoun': 'he'})
    if data[0]['he']['they'][0] == word:
        answer.append({'toMatcher': data[0]['he']['they'], 'pronoun': 'he'})
    if data[0]['he']['they_2'][0] == word:
        answer.append({'toMatcher': data[0]['he']['they_2'], 'pronoun': 'he'})
    if data[0]['he']['we'][0] == word:
        answer.append({'toMatcher': data[0]['he']['we'], 'pronoun': 'he'})
    if data[0]['he']['i'][0] == word:
        answer.append({'toMatcher': data[0]['he']['i'], 'pronoun': 'he'})
    if data[0]['he']['you_m'][0] == word:
        answer.append({'toMatcher': data[0]['he']['you_m'], 'pronoun': 'he'})
    if data[0]['he']['you_m_2'][0] == word:
        answer.append({'toMatcher': data[0]['he']['you_m_2'], 'pronoun': 'he'})
    if data[0]['he']['you_f'][0] == word:
        answer.append({'toMatcher': data[0]['he']['you_f'], 'pronoun': 'he'})
    if data[0]['he']['you_f_2'][0] == word:
        answer.append({'toMatcher': data[0]['he']['you_f_2'], 'pronoun': 'he'})
    if data[0]['she']['he'][0] == word:
        answer.append({'toMatcher': data[0]['she']['he'], 'pronoun': 'she'})
    if data[0]['she']['she'][0] == word:
        answer.append({'toMatcher': data[0]['she']['she'], 'pronoun': 'she'})
    if data[0]['she']['they'][0] == word:
        answer.append({'toMatcher': data[0]['she']['they'], 'pronoun': 'she'})
    if data[0]['she']['they_2'][0] == word:
        answer.append({'toMatcher': data[0]['she']['they_2'], 'pronoun': 'she'})
    if data[0]['she']['we'][0] == word:
        answer.append({'toMatcher': data[0]['she']['we'], 'pronoun': 'she'})
    if data[0]['she']['i'][0] == word:
        answer.append({'toMatcher': data[0]['she']['i'], 'pronoun': 'she'})
    if data[0]['she']['you_m'][0] == word:
        answer.append({'toMatcher': data[0]['she']['you_m'], 'pronoun': 'she'})
    if data[0]['she']['you_m_2'][0] == word:
        answer.append({'toMatcher': data[0]['she']['you_m_2'], 'pronoun': 'she'})
    if data[0]['she']['you_f'][0] == word:
        answer.append({'toMatcher': data[0]['she']['you_f'], 'pronoun': 'she'})
    if data[0]['she']['you_f_2'][0] == word:
        answer.append({'toMatcher': data[0]['she']['you_f_2'], 'pronoun': 'she'})
    if data[0]['they']['he'][0] == word:
        answer.append({'toMatcher': data[0]['they']['he'], 'pronoun': 'they'})
    if data[0]['they']['they'][0] == word:
        answer.append({'toMatcher': data[0]['they']['they'], 'pronoun': 'they'})
    if data[0]['they']['they'][0] == word:
        answer.append({'toMatcher': data[0]['they']['they'], 'pronoun': 'they'})
    if data[0]['they']['they_2'][0] == word:
        answer.append({'toMatcher': data[0]['they']['they_2'], 'pronoun': 'they'})
    if data[0]['they']['we'][0] == word:
        answer.append({'toMatcher': data[0]['they']['we'], 'pronoun': 'they'})
    if data[0]['they']['i'][0] == word:
        answer.append({'toMatcher': data[0]['they']['i'], 'pronoun': 'they'})
    if data[0]['they']['you_m'][0] == word:
        answer.append({'toMatcher': data[0]['they']['you_m'], 'pronoun': 'they'})
    if data[0]['they']['you_m_2'][0] == word:
        answer.append({'toMatcher': data[0]['they']['you_m_2'], 'pronoun': 'they'})
    if data[0]['they']['you_f'][0] == word:
        answer.append({'toMatcher': data[0]['they']['you_f'], 'pronoun': 'they'})
    if data[0]['they']['you_f_2'][0] == word:
        answer.append({'toMatcher': data[0]['they']['you_f_2'], 'pronoun': 'they'})
    if data[0]['they_2']['he'][0] == word:
        answer.append({'toMatcher': data[0]['they_2']['he'], 'pronoun': 'they'})
    if data[0]['they_2']['they'][0] == word:
        answer.append({'toMatcher': data[0]['they_2']['they'], 'pronoun': 'they'})
    if data[0]['they_2']['they'][0] == word:
        answer.append({'toMatcher': data[0]['they_2']['they'], 'pronoun': 'they'})
    if data[0]['they_2']['they_2'][0] == word:
        answer.append({'toMatcher': data[0]['they_2']['they_2'], 'pronoun': 'they'})
    if data[0]['they_2']['we'][0] == word:
        answer.append({'toMatcher': data[0]['they_2']['we'], 'pronoun': 'they'})
    if data[0]['they_2']['i'][0] == word:
        answer.append({'toMatcher': data[0]['they_2']['i'], 'pronoun': 'they'})
    if data[0]['they_2']['you_m'][0] == word:
        answer.append({'toMatcher': data[0]['they_2']['you_m'], 'pronoun': 'they'})
    if data[0]['they_2']['you_m_2'][0] == word:
        answer.append({'toMatcher': data[0]['they_2']['you_m_2'], 'pronoun': 'they'})
    if data[0]['they_2']['you_f'][0] == word:
        answer.append({'toMatcher': data[0]['they_2']['you_f'], 'pronoun': 'they'})
    if data[0]['they_2']['you_f_2'][0] == word:
        answer.append({'toMatcher': data[0]['they_2']['you_f_2'], 'pronoun': 'they'})
    if data[0]['we']['he'][0] == word:
        answer.append({'toMatcher': data[0]['we']['he'], 'pronoun': 'we'})
    if data[0]['we']['she'][0] == word:
        answer.append({'toMatcher': data[0]['we']['she'], 'pronoun': 'we'})
    if data[0]['we']['they'][0] == word:
        answer.append({'toMatcher': data[0]['we']['they'], 'pronoun': 'we'})
    if data[0]['we']['they_2'][0] == word:
        answer.append({'toMatcher': data[0]['we']['they_2'], 'pronoun': 'we'})
    if data[0]['we']['we'][0] == word:
        answer.append({'toMatcher': data[0]['we']['we'], 'pronoun': 'we'})
    if data[0]['we']['i'][0] == word:
        answer.append({'toMatcher': data[0]['we']['i'], 'pronoun': 'we'})
    if data[0]['we']['you_m'][0] == word:
        answer.append({'toMatcher': data[0]['we']['you_m'], 'pronoun': 'we'})
    if data[0]['we']['you_m_2'][0] == word:
        answer.append({'toMatcher': data[0]['we']['you_m_2'], 'pronoun': 'we'})
    if data[0]['we']['you_f'][0] == word:
        answer.append({'toMatcher': data[0]['we']['you_f'], 'pronoun': 'we'})
    if data[0]['we']['you_f_2'][0] == word:
        answer.append({'toMatcher': data[0]['we']['you_f_2'], 'pronoun': 'we'})
    if data[0]['i']['he'][0] == word:
        answer.append({'toMatcher': data[0]['i']['he'], 'pronoun': 'i'})
    if data[0]['i']['she'][0] == word:
        answer.append({'toMatcher': data[0]['i']['she'], 'pronoun': 'i'})
    if data[0]['i']['they'][0] == word:
        answer.append({'toMatcher': data[0]['i']['they'], 'pronoun': 'i'})
    if data[0]['i']['they_2'][0] == word:
        answer.append({'toMatcher': data[0]['i']['they_2'], 'pronoun': 'i'})
    if data[0]['i']['we'][0] == word:
        answer.append({'toMatcher': data[0]['i']['we'], 'pronoun': 'i'})
    if data[0]['i']['i'][0] == word:
        answer.append({'toMatcher': data[0]['i']['i'], 'pronoun': 'i'})
    if data[0]['i']['you_m'][0] == word:
        answer.append({'toMatcher': data[0]['i']['you_m'], 'pronoun': 'i'})
    if data[0]['i']['you_m_2'][0] == word:
        answer.append({'toMatcher': data[0]['i']['you_m_2'], 'pronoun': 'i'})
    if data[0]['i']['you_f'][0] == word:
        answer.append({'toMatcher': data[0]['i']['you_f'], 'pronoun': 'i'})
    if data[0]['i']['you_f_2'][0] == word:
        answer.append({'toMatcher': data[0]['i']['you_f_2'], 'pronoun': 'i'})
    bestMatch = []
    # code = ""
    # if frontErase != '':
    #     code = frontErase + lastLetterOrderIs
    # else:
    #     code = lastLetterOrderIs
    if sentenceType == 'past':
        pass
    else:
        if frontErase == 'ክ' or frontErase == 'ይ':
            for key in answer:
                if answer[key]['pronoun'] == 'i':
                    bestMatch.append(answer[key])
                elif answer[key]['pronoun'] == 'he':
                    bestMatch.append(answer[key])
        elif frontErase == 'ክት' or frontErase == 'ት':
            for key in answer:
                if answer[key]['pronoun'] == 'you':
                    bestMatch.append(answer[key])
                elif answer[key]['pronoun'] == 'she':
                    bestMatch.append(answer[key])
        elif frontErase == 'ክን' or frontErase == 'ን':
            for key in answer:
                if answer[key]['pronoun'] == 'we':
                    bestMatch.append(answer[key])
    print("bestMatch:",bestMatch)
    print("answer:",answer)
    if bestMatch:
        return bestMatch
    else:
        return answer

def negativity_identifier(text):
    print("text:",text)
    print("frontErases1:",frontErases1)
    negativeCollections = ['ኣይ', 'ዘይ', 'ከይ', 'እንተዘይ', 'ከምዘይ', 'ኣምበይ', 'ኣምበይም', 'ምስዘይ', 'ብዘይ', 'ብዘይም', 'ዘይም']
    if text['frontErases1'] in negativeCollections:
        wordInfo['negativity'] = {'text': text['frontErases1']}

def end_word_additions_cut_off(text):
    word_info={}
    pronoun = ""
    talking_about = ""
    word_type = ""
    word = list(text['wordAfterErases2'])
    first_letter = ""
    if word:
       first_letter = word[-1]
    second_letter = word[-2] if len(word) > 2 else ""
    third_letter = word[-3] if len(word) > 3 else ""
    fourth_letter = word[-4] if len(word) > 4 else ""

    combination = second_letter + first_letter
    combination_three = third_letter + combination if third_letter else ""
    combination_four = fourth_letter + combination_three if fourth_letter else ""

    combinations_collection = [first_letter, combination, combination_three, combination_four]
    founds = []
    is_word_ley_form = False

    if text['sentenceType'] == 'past':
        for item in alphabet_info['word_ends_collection']:
            if item in combinations_collection:
                founds.append(item)
                is_word_ley_form = False

        if not founds:
            for item in alphabet_info['word_ends_ley_Collection']:
                if item in combinations_collection:
                    founds.append(item)
                    is_word_ley_form = True

    elif text['sentenceType'] in ['future', 'present']:
        for item in alphabet_info['word_ends_with_future_and_present_tense_data']:
            if item in combinations_collection:
                founds.append(item)
                is_word_ley_form = False

        for item in alphabet_info['word_ends_with_future_and_present_tense_ley_data']:
            if item in combinations_collection:
                founds.append(item)
                is_word_ley_form = True

    cutoff = longest_str_in_array(founds) if founds else ""
    sliced_word = word[:-len(cutoff)] if cutoff else word
    last_letter=""
    if sliced_word:
        last_letter = sliced_word[-1]
        # index_of_last_letter_in_alphabets = alphabet_info['tigrina_alphabets'].index(last_letter)
        last_letter_order_is = None
        # print("last_letter:",last_letter)
        result = get_alphabet_info.get_alphabet(last_letter)
        
        if last_letter == result['first']:
            last_letter_order_is = 1
        elif last_letter == result['second']:
            last_letter_order_is = 2
        elif last_letter == result['third']:
            last_letter_order_is = 3
        elif last_letter == result['fourth']:
            last_letter_order_is = 4
        elif last_letter == result['fifth']:
            last_letter_order_is = 5
        elif last_letter == result['sixth']:
            last_letter_order_is = 6
        elif last_letter == result['seventh']:
            last_letter_order_is = 7

        second_from_last_letter = sliced_word[-2]
        
        # index_of_second_letter_in_alphabets = alphabet_info['tigrina_alphabets'].index(second_from_last_letter)
        second_from_last_letter_order_is = None
        # print("index_of_second_letter_in_alphabets:",index_of_second_letter_in_alphabets)
        result = get_alphabet_info.get_alphabet(second_from_last_letter)
        # print("result get_alphabet_info:",result)
        if second_from_last_letter == result['first']:
            second_from_last_letter_order_is = 1
        elif second_from_last_letter == result['second']:
            second_from_last_letter_order_is = 2
        elif second_from_last_letter == result['third']:
            second_from_last_letter_order_is = 3
        elif second_from_last_letter == result['fourth']:
            second_from_last_letter_order_is = 4
        elif second_from_last_letter == result['fifth']:
            second_from_last_letter_order_is = 5
        elif second_from_last_letter == result['sixth']:
            second_from_last_letter_order_is = 6
        elif second_from_last_letter == result['seventh']:
            second_from_last_letter_order_is = 7

        if cutoff or last_letter_order_is in [7, 4]:
            if not is_word_ley_form:
                if text['sentenceType'] == 'past':
                    myinfo = ends_and_pronoun_matcher_on_talking_to_someone(word_ends, cutoff, last_letter_order_is, text['sentenceType'], text['frontErases2'], last_letter, second_from_last_letter_order_is)
                else:
                    myinfo = ends_and_pronoun_matcher_on_talking_to_someone(word_ends_with_future_and_present_tense, cutoff, last_letter_order_is, text['sentenceType'], text['frontErases2'], last_letter, second_from_last_letter_order_is)
            else:
                if text['sentenceType'] == 'past':
                    myinfo = ends_and_pronoun_matcher_on_talking_to_someone(word_ends_ley, cutoff, last_letter_order_is, text['sentenceType'], text['frontErases2'], last_letter, second_from_last_letter_order_is)
                else:
                    myinfo = ends_and_pronoun_matcher_on_talking_to_someone(alphabet_info['word_ends_with_future_and_present_tense_ley_data'], cutoff, last_letter_order_is, text['sentenceType'], text['frontErases2'], last_letter, second_from_last_letter_order_is)

            if myinfo:
                pronoun = myinfo[0]['pronoun']
                talking_about = myinfo[0]['toMatcher']

        if not founds:
            word_type = "stem_1"
            info_params = {
                'data': alphabet_info['word_ends_with_future_and_present_tense_data'],
                'frontErase': text['frontErases2'],
                'combinationsCollection': combinations_collection,
                'lastLetter': last_letter,
                'lastLetterOrderIs': last_letter_order_is,
                'secondFromLastLetter': second_from_last_letter,
                'secondFromLastLetterOrderIs': second_from_last_letter_order_is,
                'sentenceType': text['sentenceType']
            }
            mycode = ""
            if text['frontErases2'] != "":
                if text['sentenceType'] == 'past':
                    mycode = str(last_letter_order_is) + text['frontErases2']
                else:
                    mycode = text['frontErases2'] + str(last_letter_order_is)
            else:
                mycode = str(last_letter_order_is)

            info_params['code'] = mycode
            result_info = ends_with_self_explaining_or_stem_expression(info_params)
            print("result_info:nnnnnnn",result_info)
            excluded_numbers = [1, 2, 3, 4, 5, 6, 7]
            print("sliced_word::::",sliced_word)
            # if result_info['cutoff'] in excluded_numbers:
            #     my_new_sliced_word = sliced_word
            # else:
            #     my_new_sliced_word = sliced_word[:-len(result_info['cutoff'])]
            
            # sliced_word = my_new_sliced_word
            pronoun = result_info['pronoun']
            talking_about = ""
        first_letter_from_ends = ""
        second_letter_from_ends = ""
        if len(sliced_word) >= 2:
            first_letter_from_ends = sliced_word[-1]
            second_letter_from_ends = sliced_word[-2]
        
        end_combination = second_letter_from_ends + first_letter_from_ends
        none_found_extras_first_from_ends = ['ኩ', 'ኹ', 'ን', 'ይ', 'ት', '2ን', '4ን', 'ና']
        none_found_extras_letters_from_ends = ['ኩን', 'ካን', 'ክን', 'ኩምን', 'ክንን', 'ንን', 'ትን', 'ናን']

        if end_combination in none_found_extras_letters_from_ends:
            sliced_word = sliced_word[:-2]
            if end_combination in ['ኩን', 'ንን']:
                pronoun = 'i'
            elif end_combination in ['ካን', 'ክን', 'ኩምን', 'ክንን']:
                pronoun = 'you'
            elif end_combination == 'ትን':
                pronoun = 'she'
            elif end_combination == 'ናን':
                pronoun = 'we'

        if first_letter_from_ends in none_found_extras_first_from_ends:
            sliced_word = sliced_word[:-1]
            if first_letter_from_ends == 'ኩ':
                pronoun = 'i'
            elif first_letter_from_ends in ['ካ', 'ኪ']:
                pronoun = 'you'
            elif first_letter_from_ends == 'ን':
                pronoun = 'he'
            elif first_letter_from_ends == 'ት':
                pronoun = 'she'
            elif first_letter_from_ends == 'ና':
                pronoun = 'we'
            elif first_letter_from_ends == 'ይ':
                pronoun = 'i'

        word_info = {
            'pronoun': pronoun,
            'wordType': word_type,
            'talkingAbout': talking_about,
            'endErases': cutoff,
            'wordAfterEndErases': ''.join(sliced_word),
            'lastLetterOrderIs': last_letter_order_is,
            'secondFromLastLetterOrderIs': second_from_last_letter_order_is,
            'leyForm': is_word_ley_form
        }
    return word_info


def generate_multiple_choices_of_word(text):
    word = list(text)
    letters_to_be_converted = word[-2:]
    first_letter_on_none_conv = word[0]
    second_letter_on_none_conv=""
    if len(word)>1:
        second_letter_on_none_conv = word[1]
    word1=[]
    word2=[]
    word3=[]
    word4=[]
    word5=[]
    word6=[]
    word7=[]
    word8=[]
    word9=[]
    word10=[]
    word11=[]
    word12=[]
    word13=[]
    word14=[]
    word15=[]
    word16=[]
    word17=[]
    word18=[]
    word19=[]
    word20=[]
    word21=[]
    word22=[]
    word23=[]
    word24=[]
    if len(list(text)) == 2:
        result = get_alphabet_info.get_alphabet(first_letter_on_none_conv)
        word1.append(result['first'])
        word2.append(result['seventh'])
        word3.append(result['fourth'])
        word4.append(result['third'])
        if second_letter_on_none_conv != "":
            result_2 = get_alphabet_info.get_alphabet(second_letter_on_none_conv)
            word1.append(result_2['first'])
            word2.append(result_2['first'])
            word3.append(result_2['first'])
            word4.append(result_2['second'])

    elif len(list(text)) == 3:
        result = get_alphabet_info.get_alphabet(first_letter_on_none_conv)
        word1.append(result['first'])
        word2.append(result['first'])
        word3.append(result['fourth'])
        word4.append(result['first'])

        word6.append(result['first'])
        word7.append(result['fourth'])
        
        result_2 = get_alphabet_info.get_alphabet(second_letter_on_none_conv)
        word1.append(result_2['first'])
        word2.append(result_2['sixth'])
        word3.append(result_2['first'])
        word4.append(result_2['fourth'])
        word6.append(result_2['seventh'])
        word7.append(result_2['sixth'])
        result_3= get_alphabet_info.get_alphabet(letters_to_be_converted[1])
        word1.append(result_3['first'])
        word2.append(result_3['first'])
        word3.append(result_3['first'])
        word4.append(result_3['first'])

        word6.append(result_3['first'])
        word7.append(result_3['first'])

    elif len(list(text)) == 4:
        result = get_alphabet_info.get_alphabet(first_letter_on_none_conv)
        word1.append(result['fourth'])
        word2.append(result['first'])
        word3.append(result['first'])
        word4.append(result['fourth'])
        word5.append(result['first'])
        word6.append(result['first'])
        word7.append(result['fourth'])
        word8.append(result['fourth'])
        word9.append(result['sixth'])
        word10.append(result['first'])
        word11.append(result['fourth'])
        word12.append(result['first'])
        word13.append(result['fourth'])
        word14.append(result['fourth'])
        word15.append(result['sixth'])
        word16.append(result['first'])
        word17.append(result['fourth'])
        word18.append(result['first'])
        word19.append(result['first'])
        word20.append(result['first'])
        word21.append(result['seventh'])
        word22.append(result['first'])
        word23.append(result['fourth'])
        word24.append(result['fourth'])
        result_2 = get_alphabet_info.get_alphabet(second_letter_on_none_conv)
        word1.append(result_2['sixth'])
        word2.append(result_2['fourth'])
        word3.append(result_2['first'])
        word4.append(result_2['sixth'])
        word5.append(result_2['seventh'])
        word6.append(result_2['fourth'])
        word7.append(result_2['sixth'])
        word8.append(result_2['fourth'])
        word9.append(result_2['sixth'])
        word10.append(result_2['sixth'])
        word11.append(result_2['first'])
        word12.append(result_2['first'])
        word13.append(result_2['fourth'])
        word14.append(result_2['fourth'])
        word15.append(result_2['sixth'])
        word16.append(result_2['sixth'])
        word17.append(result_2['first'])
        word18.append(result_2['first'])
        word19.append(result_2['sixth'])
        word20.append(result_2['fourth'])
        word20.append(result_2['sixth'])
        word22.append(result_2['fourth'])
        word23.append(result_2['sixth'])
        word24.append(result_2['sixth'])
        result_3 = get_alphabet_info.get_alphabet(letters_to_be_converted[0])
        word1.append(result_3['first'])
        word2.append(result_3['sixth'])
        word3.append(result_3['first'])
        word4.append(result_3['sixth'])
        word5.append(result_3['first'])
        word6.append(result_3['first'])
        word7.append(result_3['fourth'])
        word8.append(result_3['first'])
        word9.append(result_3['fourth'])
        word10.append(result_3['sixth'])
        word11.append(result_3['first'])
        word12.append(result_3['sixth'])
        word13.append(result_3['sixth'])
        word14.append(result_3['first'])
        word15.append(result_3['fourth'])
        word16.append(result_3['sixth'])
        word17.append(result_3['first'])
        word18.append(result_3['sixth'])
        word19.append(result_3['first'])
        word20.append(result_3['seventh'])
        word20.append(result_3['seventh'])
        word22.append(result_3['sixth'])
        word23.append(result_3['fourth'])
        word24.append(result_3['seventh'])
        result_4 = get_alphabet_info.get_alphabet(letters_to_be_converted[1])
        word1.append(result_4['first'])
        word2.append(result_4['first'])
        word3.append(result_4['first'])
        word4.append(result_4['first'])
        word5.append(result_4['first'])
        word6.append(result_4['first'])
        word7.append(result_4['first'])
        word8.append(result_4['first'])
        word9.append(result_4['sixth'])
        word10.append(result_4['first'])
        word11.append(result_4['first'])
        word12.append(result_4['first'])
        word13.append(result_4['first'])
        word14.append(result_4['first'])
        word15.append(result_4['sixth'])
        word16.append(result_4['first'])
        word17.append(result_4['first'])
        word18.append(result_4['first'])
        word19.append(result_4['first'])
        word20.append(result_4['first'])
        word20.append(result_4['first'])
        word22.append(result_4['first'])
        word23.append(result_4['first'])
        word24.append(result_4['first'])

    elif len(list(text)) > 4:
        middle_letters = ''.join(word[2:-2])
        result = get_alphabet_info.get_alphabet(first_letter_on_none_conv)
        word1.append(result['fourth'])
        word2.append(result['first'])
        word3.append(result['fourth'])
        word4.append(result['fourth'])
        word5.append(result['fourth'])
        word6.append(result['first'])
        word7.append(result['fourth'])
        word8.append(result['first'])
        word9.append(result['sixth'])
        word10.append(result['first'])
        word11.append(result['fourth'])
        word12.append(result['fourth'])
        word13.append(result['fourth'])
        word14.append(result['fourth'])
        word15.append(result['first'])
        result_2 = get_alphabet_info.get_alphabet(second_letter_on_none_conv)
        word1.append(result_2['seventh'])
        word2.append(result_2['first'])
        word3.append(result_2['first'])
        word4.append(result_2['first'])
        word5.append(result_2['sixth'])
        word6.append(result_2['fourth'])
        word7.append(result_2['sixth'])
        word8.append(result_2['fourth'])
        word9.append(result_2['sixth'])
        word10.append(result_2['first'])
        word11.append(result_2['seventh'])
        word12.append(result_2['first'])
        word13.append(result_2['second'])
        word14.append(result_2['first'])
        word15.append(result_2['fourth'])

        word1.append(middle_letters)
        word2.append(middle_letters)
        word3.append(middle_letters)
        word4.append(middle_letters)
        word5.append(middle_letters)
        word6.append(middle_letters)
        word7.append(middle_letters)
        word8.append(middle_letters)
        word9.append(middle_letters)
        word10.append(middle_letters)
        word11.append(middle_letters)
        word12.append(middle_letters)
        word13.append(middle_letters)
        word14.append(middle_letters)
        word15.append(middle_letters)
        result_3 = get_alphabet_info.get_alphabet(letters_to_be_converted[0])
        word1.append(result_3['first'])
        word2.append(result_3['first'])
        word3.append(result_3['first'])
        word4.append(result_3['first'])
        word5.append(result_3['first'])
        word6.append(result_3['first'])
        word7.append(result_3['fourth'])
        word8.append(result_3['first'])
        word9.append(result_3['fourth'])
        word10.append(result_3['first'])
        word11.append(result_3['first'])
        word12.append(result_3['sixth'])
        word13.append(result_3['first'])
        word14.append(result_3['sixth'])
        word15.append(result_3['first'])
        result_4 = get_alphabet_info.get_alphabet(letters_to_be_converted[0])
        word1.append(result_4['sixth'])
        word2.append(result_4['first'])
        word3.append(result_4['first'])
        word4.append(result_4['first'])
        word5.append(result_4['first'])
        word6.append(result_4['first'])
        word7.append(result_4['first'])
        word8.append(result_4['first'])
        word9.append(result_4['sixth'])
        word10.append(result_4['first'])
        word11.append(result_4['first'])
        word12.append(result_4['first'])
        word13.append(result_4['first'])
        word14.append(result_4['first'])
        word15.append(result_4['first'])
    choices = {}
    choices_collection = []

    if len(word1) != 0:
        choices['word1'] = ''.join(word1)
        choices_collection.append(choices['word1'])
    if len(word2) != 0:
        choices['word2'] = ''.join(word2)
        choices_collection.append(choices['word2'])
    if len(word3) != 0:
        choices['word3'] = ''.join(word3)
        choices_collection.append(choices['word3'])
    if len(word4) != 0:
        choices['word4'] = ''.join(word4)
        choices_collection.append(choices['word4'])
    if len(word5) != 0:
        choices['word5'] = ''.join(word5)
        choices_collection.append(choices['word5'])
    if len(word5) != 0:
        choices['word5'] = ''.join(word5)
        choices_collection.append(choices['word5'])
    if len(word6) != 0:
        choices['word6'] = ''.join(word6)
        choices_collection.append(choices['word6'])
    if len(word7) != 0:
        choices['word7'] = ''.join(word7)
        choices_collection.append(choices['word7'])
    if len(word8) != 0:
        choices['word8'] = ''.join(word8)
        choices_collection.append(choices['word8'])
    if len(word9) != 0:
        choices['word9'] = ''.join(word9)
        choices_collection.append(choices['word9'])
    if len(word10) != 0:
        choices['word10'] = ''.join(word10)
        choices_collection.append(choices['word10'])
    if len(word11) != 0:
        choices['word11'] = ''.join(word11)
        choices_collection.append(choices['word11'])
    if len(word12) != 0:
        choices['word12'] = ''.join(word12)
        choices_collection.append(choices['word12'])
    if len(word13) != 0:
        choices['word13'] = ''.join(word13)
        choices_collection.append(choices['word13'])
    if len(word14) != 0:
        choices['word14'] = ''.join(word14)
        choices_collection.append(choices['word14'])
    if len(word15) != 0:
        choices['word15'] = ''.join(word15)
        choices_collection.append(choices['word15'])
    if len(word16) != 0:
        choices['word16'] = ''.join(word16)
        choices_collection.append(choices['word16'])
    if len(word17) != 0:
        choices['word17'] = ''.join(word17)
        choices_collection.append(choices['word17'])
    if len(word18) != 0:
        choices['word18'] = ''.join(word18)
        choices_collection.append(choices['word18'])
    if len(word19) != 0:
        choices['word19'] = ''.join(word19)
        choices_collection.append(choices['word19'])
    if len(word20) != 0:
        choices['word20'] = ''.join(word20)
        choices_collection.append(choices['word20'])
    if len(word21) != 0:
        choices['word21'] = ''.join(word21)
        choices_collection.append(choices['word21'])
    if len(word22) != 0:
        choices['word22'] = ''.join(word22)
        choices_collection.append(choices['word22'])
    if len(word23) != 0:
        choices['word23'] = ''.join(word23)
        choices_collection.append(choices['word23'])
    if len(word24) != 0:
        choices['word24'] = ''.join(word24)
        choices_collection.append(choices['word24'])
    return choices_collection

def get_info(info):
    word_info = {}
    # negativity = negativity_identifier(info)
    word = verbs_with_length2_modifier(info)
    print("word:",word)
    word_info["word"] = ''.join(word)
    
    front_cuts = front_text_cut_offs(word_info)
    word_info["frontErases1"] = front_cuts["frontErases1"]
    word_info["wordAfterErases1"] = front_cuts["wordAfterErases1"]
    # print("word_info:",word_info)
    sentence_identifier_and_front_erases = sentence_identifier_and_front_text_cut_off2(word_info)
    # print("sentence_identifier_and_front_erases:",sentence_identifier_and_front_erases)
    word_info["sentenceType"] = sentence_identifier_and_front_erases["sentenceType"]
    word_info["frontErases2"] = sentence_identifier_and_front_erases["frontErases2"]
    word_info["wordAfterErases2"] = sentence_identifier_and_front_erases["wordAfterErases2"]
    # print("word_info bbbbbbb:",word_info)
    final_word_info = end_word_additions_cut_off(word_info)
    print("final_word_info:",final_word_info)
    word_info["talkingAbout"] = final_word_info["talkingAbout"]
    word_info["wordType"] = final_word_info["wordType"]
    word_info["pronoun"] = final_word_info["pronoun"]
    
    main_word = list(final_word_info["wordAfterEndErases"])
    print("main_word:",main_word)
    word2 = generate_multiple_choices_of_word(final_word_info["wordAfterEndErases"])
    print("word2:",word2)
    word3 = []
    
    if main_word[0] == 'ኸ':
        main_word[0] = 'ከ'
        word3 = generate_multiple_choices_of_word(''.join(main_word))
    elif main_word[0] == 'ተ':
        main_word[0] = 'ኣ'
        word3 = generate_multiple_choices_of_word(''.join(main_word))
    elif main_word[0] == 'የ':
        main_word[0] = 'ኣ'
        word3 = generate_multiple_choices_of_word(''.join(main_word))
    elif main_word[0] == 'ከ':
        main_word[0] = 'ኣ'
        word3 = generate_multiple_choices_of_word(''.join(main_word))
    elif main_word[0] == 'ነ':
        main_word[0] = 'ኣ'
        word3 = generate_multiple_choices_of_word(''.join(main_word))
    elif main_word[0] == 'ኣ':
        main_word[0] = 'ተ'
        word3 = generate_multiple_choices_of_word(''.join(main_word))
    
    word4, word5, word6, word7 = [], [], [], []
    # print("final_word_info:",final_word_info)
    if 'frontErases1' in final_word_info and final_word_info['frontErases1'] == 'ከም':
        word3 = generate_multiple_choices_of_word(''.join(main_word))
        print("word3:",word3)
        w1 = 'ም' + final_word_info["wordAfterEndErases"]
        w2 = 'ከም' + final_word_info["wordAfterEndErases"]
        w3 = 'ኣም' + final_word_info["wordAfterEndErases"]
        word4 = generate_multiple_choices_of_word(w1)
        word5 = generate_multiple_choices_of_word(w2)
        word6 = generate_multiple_choices_of_word(w3)
    
    ke = ['ከ', 'ኩ', 'ኪ', 'ካ', 'ኬ', 'ክ', 'ኮ']
    to_be_checked_in = list(final_word_info.get('wordAfterErases2', ''))
    
    for key in range(len(to_be_checked_in)):
        if to_be_checked_in[key] in ke:
            index = to_be_checked_in.index(to_be_checked_in[key])
            to_be_checked_in[index] = 'ኸ'
            word7 = generate_multiple_choices_of_word(''.join(to_be_checked_in))
    
    word_info["endsHerarchyOfWord"] = word3 + word2 + word6 + word5 + word4 + word7
    
    return word_info

def assembler(text):
    word = text
    info = {}
    uniq_exceptions = ['ኢሉ', 'ኢላ', 'ኢሎም', 'ኢለን']
    result_of_verb_corrector = get_info(word)

    if result_of_verb_corrector["frontErases1"] == 'ብም':
        info["attachementWithVerb"] = 'by'
        result_of_verb_corrector["sentenceType"] = 'Gerund'
        info["sentenceType"] = 'present'
    elif result_of_verb_corrector["frontErases1"] == 'ንዘይ':
        info["attachementWithVerb"] = 'for the one who does not'
        result_of_verb_corrector["sentenceType"] = 'simple'
        info["sentenceType"] = 'simple'
    elif result_of_verb_corrector["frontErases1"] in ['ንኸይ', 'ንከይ']:
        info["attachementWithVerb"] = 'not to'
        result_of_verb_corrector["sentenceType"] = 'simple'
        info["sentenceType"] = 'simple'
    elif result_of_verb_corrector["frontErases1"] == 'ብዝ':
        info["attachementWithVerb"] = 'by what'
        result_of_verb_corrector["sentenceType"] = 'PresentTense'
        info["sentenceType"] = 'present'
    elif result_of_verb_corrector["frontErases1"] in ['ከምዝ', 'ከምድ']:
        pronoun = result_of_verb_corrector.get("pronoun", "it")
        info["attachementWithVerb"] = f'that {pronoun} will '
        result_of_verb_corrector["sentenceType"] = 'future'
        info["sentenceType"] = 'future'
    elif result_of_verb_corrector["frontErases1"] == 'ዝ':
        result_of_verb_corrector["sentenceType"] = 'past'
        result_of_verb_corrector["needTo_AboutTalking"] = "no"
        info["sentenceType"] = 'past'
    elif result_of_verb_corrector["frontErases1"] == 'ምስ':
        pronoun = result_of_verb_corrector.get("pronoun", "it")
        info["attachementWithVerb"] = f'when {pronoun}'
        result_of_verb_corrector["sentenceType"] = 'simple'
        info["sentenceType"] = 'present simple'
    elif result_of_verb_corrector["frontErases1"] == 'ብዘይም':
        info["attachementWithVerb"] = 'for not'
        result_of_verb_corrector["sentenceType"] = 'Gerund'
        info["sentenceType"] = 'present'
    elif result_of_verb_corrector["frontErases1"] == 'ብዘይ':
        info["attachementWithVerb"] = 'by not'
        result_of_verb_corrector["sentenceType"] = 'Gerund'
        info["sentenceType"] = 'present'
    elif result_of_verb_corrector["frontErases1"] == 'ዘይም':
        info["attachementWithVerb"] = 'not'
        result_of_verb_corrector["sentenceType"] = 'Gerund'
        info["sentenceType"] = 'present'
    elif result_of_verb_corrector["frontErases1"] in ['ምስት', 'ምስዝ']:
        info["attachementWithVerb"] = 'when'
        result_of_verb_corrector["sentenceType"] = 'simple'
        info["sentenceType"] = 'present simple'
    elif result_of_verb_corrector["frontErases1"] in ['ምስዘይ', 'ምስዘይት']:
        info["attachementWithVerb"] = 'when not'
        result_of_verb_corrector["sentenceType"] = 'Gerund'
        info["sentenceType"] = 'present'
    elif result_of_verb_corrector["frontErases1"] in ['እንተ', 'እንተዝ']:
        pronoun = result_of_verb_corrector.get("pronoun", "it")
        info["attachementWithVerb"] = f'if {pronoun}'
        info["sentenceType"] = 'if'
    elif result_of_verb_corrector["frontErases1"] == 'ከምዘይ':
        pronoun = result_of_verb_corrector.get("pronoun", "it")
        info["attachementWithVerb"] = f'that {pronoun} will not '
        result_of_verb_corrector["sentenceType"] = 'future'
        info["sentenceType"] = 'future'
    elif result_of_verb_corrector["frontErases1"] == 'እንተዘይ':
        pronoun = result_of_verb_corrector.get("pronoun", "it")
        verb_to_be = ""
        if result_of_verb_corrector["sentenceType"] == 'past':
            verb_to_be = "did"
            result_of_verb_corrector["sentenceType"] = 'future'
            info["sentenceType"] = 'future'
        elif result_of_verb_corrector["sentenceType"] == 'future':
            verb_to_be = "will"
            info["sentenceType"] = 'future'
        else:
            verb_to_be = "does" if pronoun in ['he', 'she', 'it'] else "do"
            info["sentenceType"] = 'present simple'
        info["attachementWithVerb"] = f'if {pronoun} {verb_to_be} not'
    elif result_of_verb_corrector["frontErases1"] in ['ኣምበይ', 'ኣምበይም']:
        pronoun = result_of_verb_corrector.get("pronoun", "it")
        info["attachementWithVerb"] = f'{pronoun} would not'
        info["sentenceType"] = 'future'
        result_of_verb_corrector["sentenceType"] = 'future'
    elif result_of_verb_corrector["frontErases1"] in ['ኣይ', 'ከይ', 'ዘይ']:
        if text.get("extraInfo", '') == '':
            info["attachementWithVerb"] = "will not"
            result_of_verb_corrector["sentenceType"] = 'future'
            info["sentenceType"] = 'future'

    if len(result_of_verb_corrector["endsHerarchyOfWord"]) == 0:
        if result_of_verb_corrector["wordAfterErases2"] in uniq_exceptions:
            result_of_verb_corrector["endsHerarchyOfWord"].append('አለ')

    info["mainResult"] = result_of_verb_corrector
    return info

def divide_array(array, last_array_length):
    # Calculate the split index
    split_index = len(array) - last_array_length
    
    # Create the first array from the start to the split index
    first_array = array[:split_index]
    
    # Create the second array from the split index to the end
    second_array = array[split_index:]
    
    return [first_array, second_array]
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
        if len(textInfo.firstLetter) > 0:
            firstCharacter = int(firstCharacter) - 1
            textInfo.firstLetter = [decode.detailInfo[0].details[0].listOfFamilyMembers[firstCharacter]]
    lastThree = decode.detailInfo[0].details[-len(textInfo.lastPart):]
    lastChar1 = ""
    lastChar2 = ""
    lastChar3 = ""
    rule = list(map(lambda item: item - 1, rule.split('')))
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
    finalized = additionsAtStart + textInfo.firstLetter.join('') + textInfo.firstParts.join('') + finalized + additionsAtEnd
    return finalized.strip()

def decoded_manipulation(text, rule, firstCharacter, additionsAtStart, additionsAtEnd):
    textInfo = text_manipulation(text)
    code = code_decode_info.code_translation(text, 'code', '')
    decode = code_decode_info.code_translation(code, 'decode', 'yes')
    # print("decode:",decode)
    if firstCharacter != "" and firstCharacter is not None:
        if len(textInfo.firstLetter) > 0:
            firstCharacter = int(firstCharacter) - 1
            textInfo.firstLetter = [decode.detailInfo[0].details[0].listOfFamilyMembers[firstCharacter]]
    lastThree = decode['detailInfo'][0]['details'][-len(textInfo['lastPart']):]
    lastChar1 = ""
    lastChar2 = ""
    lastChar3 = ""
    rule = list(map(lambda item: item - 1, map(int, list(rule))))
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
    finalized = additionsAtStart + ''.join(textInfo['firstLetter']) + ''.join(textInfo['firstParts']) + finalized + additionsAtEnd
    return finalized.strip()

def verb_conversion(text, first_person, third_person, situation, using_ley_letter):
    result = ""

    # Normalize third_person values
    if third_person == "you_male":
        third_person = "you_m"
    elif third_person == "you_female":
        third_person = "you_f"
    elif third_person == "you_females":
        third_person = "you_f_2"
    elif third_person == "you_males":
        third_person = "you_m_2"
    elif third_person == "they_females":
        third_person = "they_2"

    # Normalize first_person values
    if first_person == "you":
        first_person = "you_m"
    elif first_person == "you_female":
        first_person = "you_f"
    elif first_person == "you_females":
        first_person = "you_f_2"
    elif first_person == "you_males":
        first_person = "you_m_2"
    elif first_person == "they_females":
        first_person = "they_2"

    word_end_info = word_ends[0][first_person]
    front_addition = "".join(word_end_info["starts"][situation])

    # Determine the correct ending
    print("using_ley_letter:",using_ley_letter)
    if using_ley_letter and using_ley_letter != 'no':
        end_match = word_ends_with_future_and_present_tense_ley[0][first_person][third_person]
    else:
        print("first_person:",first_person)
        print("third_person:",third_person)
        print("alphabet_info['word_ends_with_future_and_present_tense_ley_data'][0]:",alphabet_info['word_ends_with_future_and_present_tense_ley_data'][0])
        end_match = word_ends_with_future_and_present_tense[0][first_person][third_person]

    if end_match[0].isdigit():
        result = decoded_manipulation(text, end_match[0], "", front_addition, "")
    else:
        diff = list(end_match[0])
        if diff[0].isdigit():
            if diff[1:]:
                merg_ends = "".join(diff[1:])
                result = decoded_manipulation(text, diff[0], "", front_addition, merg_ends)
            else:
                result = decoded_manipulation(text, diff[0], "", front_addition, "")
        else:
            merg_ends = end_match[0]
            result = decoded_manipulation(text, "66", "", front_addition, merg_ends)

    return result
def make_verb(text, situation, person, third_person, negativities_or_front_additions, using_ley_letter):
    person = person.lower()
    result = ""
    english = ""
    result_info = {}

    # Handle third_person if provided
    if third_person:
        result = verb_conversion(text, person, third_person, situation, using_ley_letter)
    else:
        # Handle different situations (present, past, future)
        if situation == 'present':
            if person in ['i', 'he', 'it']:
                if person == 'i':
                    english = "I am"
                elif person == 'he':
                    english = "he is"
                elif person == 'it':
                    english = "it is"
                result = decoded_manipulation(text, "66", "", "ይ", "")
            elif person in ['she', 'you', 'you_female']:
                if person == 'she':
                    english = "she is"
                elif person == 'you':
                    english = "you are"
                elif person == 'you_female':
                    english = "you are"
                result = decoded_manipulation(text, "66", "", "ት", "")
            elif person == 'they':
                english = "they are"
                result = decoded_manipulation(text, "62", "", "ይ", "")
            elif person == 'they_females':
                english = "they are"
                result = decoded_manipulation(text, "64", "", "ይ", "")
            elif person == 'we':
                english = "we are"
                result = decoded_manipulation(text, "66", "", "ን", "")
            elif person == 'you_females':
                english = "you are"
                result = decoded_manipulation(text, "64", "", "ት", "")
            elif person == 'you_males':
                english = "you are"
                result = decoded_manipulation(text, "62", "", "ት", "")
        
        elif situation == 'past':
            if person == 'i':
                english = "I"
                result = decoded_manipulation(text, "31", "", "", "")
            elif person == 'he':
                english = "he"
                result = decoded_manipulation(text, "32", "", "", "")
            elif person == 'it':
                english = "it"
                result = decoded_manipulation(text, "32", "", "", "")
            elif person == 'she':
                english = "she"
                result = decoded_manipulation(text, "34", "", "", "")
            elif person == 'they':
                english = "they"
                result = decoded_manipulation(text, "37", "", "", "ም")
            elif person == 'they_females':
                english = "they"
                result = decoded_manipulation(text, "31", "", "", "ን")
            elif person == 'we':
                english = "we"
                result = decoded_manipulation(text, "36", "", "", "ና")
            elif person == 'you':
                english = "you"
                result = decoded_manipulation(text, "36", "", "", "ካ")
            elif person == 'you_female':
                english = "you"
                result = decoded_manipulation(text, "36", "", "", "ኪ")
            elif person == 'you_females':
                english = "you"
                result = decoded_manipulation(text, "36", "", "", "ክን")
            elif person == 'you_males':
                english = "you"
                result = decoded_manipulation(text, "36", "", "", "ኩም")
        
        elif situation == 'future':
            if person in ['i', 'he', 'it']:
                if person == 'i':
                    english = "I will"
                elif person == 'he':
                    english = "he will"
                elif person == 'it':
                    english = "it will"
                result = decoded_manipulation(text, "66", "", "", "")
            elif person == 'she':
                result = decoded_manipulation(text, "66", "", "ት", "")
            elif person == 'they':
                result = decoded_manipulation(text, "62", "", "ክ", "")
            elif person == 'they_females':
                result = decoded_manipulation(text, "64", "", "ክ", "")
            elif person == 'we':
                result = decoded_manipulation(text, "66", "", "ክን", "")
            elif person == 'you':
                result = decoded_manipulation(text, "66", "", "ክት", "")
            elif person == 'you_females':
                result = decoded_manipulation(text, "63", "", "ክት", "")
            elif person == 'you_males':
                result = decoded_manipulation(text, "62", "", "ክት", "")

    # Handle negativities or front additions
    if negativities_or_front_additions:
        if negativities_or_front_additions in alphabet_info['negatives']:
            result_info["is_negative"] = "yes"
        else:
            result_info["is_negative"] = "no"
        result = negativities_or_front_additions + result
    else:
        result_info["is_negative"] = "no"

    result_info["result_text_tigrina"] = result
    result_info["result_text_english"] = english
    return result_info
class VerbInfo:
    @staticmethod
    def make_stem_verb(text):
        # try:
            result = assembler(text)
            return result
        # except Exception as error:
        #     return f"There is something wrong!, {error}"

    @staticmethod
    def make_verb_from_stem(text, situation, person, third_person=None, negativities_or_front_additions=None, using_ley_letter=None):
        # try:
            result = make_verb(text, situation, person, third_person, negativities_or_front_additions, using_ley_letter)
            info = {
                "text": text,
                "situation": situation,
                "first_person": person,
                "third_person": third_person,
                "negativitiesOrFrontAdditions": negativities_or_front_additions,
                "usingLeyLetter": using_ley_letter,
                "result_text_tigrina": result["result_text_tigrina"],
                "result_text_english": result["result_text_english"],
                "is_negative": result["is_negative"]
            }
            return info
        # except Exception as error:
        #     return f"There is something wrong!, {error}"

# Usage example:
# VerbInfo.make_stem_verb("some text")
# VerbInfo.make_verb_from_stem("some text", "present", "i", "he", "", "")

verb_info = VerbInfo()
