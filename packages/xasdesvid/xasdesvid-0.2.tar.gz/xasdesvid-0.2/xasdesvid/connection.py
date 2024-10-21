import pymorphy2

morph = pymorphy2.MorphAnalyzer()

def determine_connection(main_word, dependent_word):
    main_word_parse = morph.parse(main_word)[0]
    dependent_word_parse = morph.parse(dependent_word)[0]

    # Согласование
    if dependent_word_parse.tag.POS == 'ADJF' and main_word_parse.tag.POS == 'NOUN':
        question = f"Какой {main_word}?"
        return f"{main_word} ({question}) {dependent_word}"

    # Управление
    if dependent_word_parse.tag.case == 'gen' and main_word_parse.tag.POS == 'NOUN':
        question = f"Чего {main_word}?"
        return f"{main_word} ({question}) {dependent_word}"

    # Примыкание
    if dependent_word_parse.tag.POS in {'INFN', 'ADVB'}:
        if main_word_parse.tag.POS in {'ADVB', 'VERB'}:
            question = f"Как {main_word}?"
            return f"{main_word} ({question}) {dependent_word}"

    return f"{main_word} (Не удалось определить вид связи) {dependent_word}"

def extract_main_and_dependent(phrase):
    words = phrase.split()
    if len(words) != 2:
        return None, None
    return words[0], words[1]
