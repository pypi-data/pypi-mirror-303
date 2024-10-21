# xasdesvid/connection.py
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

def determine_connection(main_word, dependent_word):
    main_word_parse = morph.parse(main_word)[0]
    dependent_word_parse = morph.parse(dependent_word)[0]
    
    if dependent_word_parse.tag.POS == 'ADJF' and main_word_parse.tag.POS == 'NOUN':
        return 'Согласование', f"Какой {main_word}?"
    
    if dependent_word_parse.tag.case == 'gen' and main_word_parse.tag.POS == 'NOUN':
        return 'Управление', f"Чего {main_word}?"
    
    if dependent_word_parse.tag.POS == 'INFN' and main_word_parse.tag.POS == 'ADVB':
        return 'Примыкание', f"Как {main_word}?"
    
    if dependent_word_parse.tag.POS == 'ADVB' and main_word_parse.tag.POS == 'VERB':
        return 'Примыкание', f"Как {main_word}?"

    return 'Не удалось определить вид связи', None

def extract_main_and_dependent(phrase):
    words = phrase.split()
    if len(words) != 2:
        return None, None
    return words[0], words[1]
