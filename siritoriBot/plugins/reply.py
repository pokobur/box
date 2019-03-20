# from pkg_resources import require
from slackbot.bot import respond_to
import re
from plugins import yasaidata
from plugins import logic
import random

siritori_act_flg = False


@respond_to('.+')
def siritori_func(message):
    global siritori_act_flg
    request = message.body['text']
    if request == 'しりとり':
        siritori_act_flg = True
        yasaidata.master_data()
        message.reply('野菜を読み込みました\n'
                      'ルール説明！\n'
                      '①同じワードは使用しないこと\n'
                      '②濁音や拗音は清音へ変換してもよい\n'
                      '③長音は前文字の母音にすること\n'
                      '④20秒以内に答えること\n'
                      '⑥二回以上の一字攻めはしないこと\n'
                      '⑦「ん」で終わると負け\n'
                      '⑧やめたい時は「まいった」という\n'
                      'スタート！\n'
                      '----------------------------------------\n')

        logic.rireki_list.clear()
        message.reply(logic.random_get(yasaidata.basket))
        return

    if request == 'まいった':
        if siritori_act_flg:
            message.reply('おつかれさまでした')
            siritori_act_flg = False
            return
        else:
            print('siritori_act_flgがONになっていない')
            message.reply('"しりとり"と言ってスタートしてね')
    else:
        if not siritori_act_flg:
            message.reply('"しりとり"と言ってスタートしてね')
            return

        request = logic.convert_hira_to_kana(request)
        if logic.check_n(request):
            print('ンがついてない')
        else:
            print('ンがついている')
            message.reply('"ん"' + 'がついたので終了です')
            return

        if logic.exist_list(request):
            print('野菜がある')
            message.reply(request + 'ですね')
        else:
            print('野菜がない')
            message.reply('たぶん存在しない野菜です')
            return

        if logic.already_used_words(request):
            pass
        else:
            print('すでに使用されたワード')
            message.reply('すでに使用されたワードです')
            return

        if logic.word_end_check(request):
            pass
        else:
            print('ワードの先頭が不正')
            message.reply('先頭に' + '"' + logic.last_bot_word[-1:] + '"' + 'のつく野菜で返してね')
            return

        logic.words_storage(request)

        result_word = logic.word_search(request)
        if result_word:
            message.reply(result_word)
        else:
            print('候補リストからワードが無くなった')
            message.replya('まいった！')
            siritori_act_flg = False



# yasaidata.master_data()


'''
@respond_to('しりとり')
def siritori_func(message):
    message.reply('今日はやりません')

@respond_to('こんにちは')
def siritori_func(message):
    message.reply('こんにちは！')


@respond_to('.*')
def siritori_func(message):
    message.reply('しりとりをしませんか？')



@respond_to('(.*)')
def refrection(message, something):
    message.reply(something)


@respond_to('good')
def good_func(message):
    message.reply('リアクションした！')
    message.react('+1')
    message.react('100')

'''
