import requests
import json
import numpy as np
import datetime

text_list = ['@mizume 音ゲーなんてやってる場合じゃないんでーすか？',
             '@mizume 音ゲーなんてやめてスーパーマリオオデッセイとかモンハン，スプラトゥーンやりませんか？',
             '@mizume ロックマンエグゼの実況はどうなったんですか？はやく全シリーズの実況完結させてくださいよ．もちろんまた縛りプレイするんですよね？',
             '@mizume キミを見てるといつもハートDOKI☆DOKI　揺れる思いはマシュマロみたいにふわ☆ふわ　いつもがんばるキミの横顔　ずっと見てても気づかないよね　夢の中なら二人の距離　縮められるのにな　あぁ カミサマお願い二人だけのDream Timeください☆　お気に入りのうさちゃん 抱いて今夜も オヤスミ♪',
             '@mizume Please dont say "You are lazy"　だって本当はcrazy　白鳥たちはそう見えないとこでバタ足するんです　本能に従順忠実 翻弄も重々承知　前途洋々だし…　だからたまに休憩しちゃうんです,'
             '@mizume Welcome to ようこそジャパリパーク　今日もドッタンバッタン大騒ぎ　姿かたちも十人十色　だから魅かれ合うの　夕暮れ空に指をそっと重ねたら　はじめまして　君をもっと知りたいな♪']

def attention():
    # setting
    URL = 'https://hooks.slack.com/services/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'
    TEXT = np.random.choice(text_list)
    USERNAME = 'お邪魔します'

    # post
    post_json = {
        'text': TEXT,
        'username': USERNAME,
        'link_names': 1
    }
    requests.post(URL, data=json.dumps(post_json))

if __name__ == '__main__':
    add_flg = True
    while 1:
        now = datetime.datetime.now()
        interval = np.random.randint(3,20)
        td = datetime.timedelta(seconds=interval)
        if add_flg:
            next_time = now + td
            add_flg = False
        if next_time.second == now.second:
            attention()
            add_flg = True