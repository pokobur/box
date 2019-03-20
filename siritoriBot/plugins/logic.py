import jaconv
import random
import re
from plugins import yasaidata

'''
def inspe(message):

    re_hira = re.compile(r'[\u3041-\u3093]')
    if re_hira == message:
        m_kana = jaconv.hira2kana(message)
        pass
    else:
        print("ひらがなを入力してください")

    if re.search('ン\Z', m_kana):
        print("末尾に「ん」がついた")

    if (m_kana in yasaidata.basket):
        print(message, 'ですね')
    else:
        print('存在しない野菜です')

    tone_list = ['ｱ','ｲ','ｳ','ｴ','ｵ','ｬ','ｭ','ｮ','ﾜ','ｰ','ﾞ','ﾟ']

    jaconv.hira2hkana(message)
    for tone in tone_list:
        if m_kana[-1:] == tone:
            m_kana.replace(tone , ' ')
            break

    result = ''
    for word in yasaidata.basket:
        if word.startwith(m_kana[-1:]):
            result = word
            break


    m_hira = jaconv.hkana2hira(result)

'''


def convert_hira_to_kana(user_message_hira):
    re_hira = re.compile(r'[\u3041-\u3093]+')
    remove_bar = user_message_hira.replace('ー', '')

    if re_hira.fullmatch(remove_bar):
        converted_kana = jaconv.hira2kata(user_message_hira)
        print(converted_kana)
        return converted_kana
    else:
        print("ひらがなを入力してください")
        return None


def check_n(converted_kana):
    print(converted_kana)
    if re.search('ン\Z', converted_kana):
        print("末尾に「ん」がついた")
        return False
    return True


def exist_list(converted_kana):
    for yasai in yasaidata.basket:
        if (converted_kana in yasai):
            print(converted_kana, 'ですね')
            return True

    print('存在しない野菜です')
    return False


tone_list = ['ｧ', 'ｨ', 'ｩ', 'ｪ', 'ｫ', 'ｬ', 'ｭ', 'ｮ', 'ﾜ', 'ｰ', 'ﾞ', 'ﾟ']


def tone_reject(converted_kana):
    converted_half_kana = jaconv.zenkaku2hankaku(converted_kana)
    replaced_half_kana = converted_half_kana
    print(converted_half_kana)
    for tone in tone_list:
        if converted_half_kana[-1:] == tone:
            replaced_half_kana = converted_half_kana.replace(tone, '')
            break
    print(replaced_half_kana)
    replaced_full_kana = jaconv.hankaku2zenkaku(replaced_half_kana)
    print(replaced_full_kana)
    return replaced_full_kana


# 入力したワードが全角カタカナで入ってくるべき
def word_search(zenkaku_kana):
    replaced_full_kana = tone_reject(zenkaku_kana)
    applicant_list = []
    for word in yasaidata.basket:
        if word.startswith(replaced_full_kana[-1:]):
            if word in rireki_list:
                continue
            else:
                applicant_list.append(word)
    print(applicant_list)
    if len(applicant_list) == 0:
        return None
    return random_get(applicant_list)


def random_get(ans_list):

    bot_ans_word = random.choice(ans_list)
    print(bot_ans_word)
    words_storage(bot_ans_word.strip())
    global last_bot_word
    last_bot_word = tone_reject(bot_ans_word)
    return bot_ans_word


rireki_list = []


def words_storage(ans_word):
    rireki_list.append(ans_word)
    print(rireki_list)


def already_used_words(used_words):
    for rireki_word in rireki_list:
        if rireki_word == used_words:
            print('すでに使用されたワードです')
            return False
            continue
    return True


last_bot_word = None


def word_end_check(user_word):
    if user_word.startswith(last_bot_word[-1:]):
        return True
    else:
        return False




"""
if __name__ == '__main__':
    yasaidata.master_data()
    words_storage('スイカ')
"""
