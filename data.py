work_list = [
    {
        "name": "ホームページ",
        "image": "images/banner.jpg",
        "description": "このサイトのことです。flaskの静的サイトジェネレータのfrozen flaskと言うライブラリを使用しました。",
        "qiita": "",
        "github": ""
    },
    {
        "name": "AIをGUIで設計できるアプリ",
        "image": "images/guiai01.png",
        "description": "GUIでディープラーニングの設計ができるアプリ。タスクは手書き文字認識のみ。自作したモデルを学習させた結果をランキングで表示する機能もある。",
        "qiita": "",
        "github": ""
    },
    {
        "name": "upCamera",
        "image": "images/upcamera.png",
        "description": "カメラで撮った写真を0タップでtwitterにアップロードするiOSアプリ。Twitterにサーバーにバックアップする目的で作ったが、今は全く使っていない。",
        "qiita": "",
        "github": "https://github.com/wataoka/upcamera"
    },
    {
        "name": "OWALIVE",
        "image": "images/owalive.png",
        "description": "2018年3月8-9日に開催されたTrunk Hachathonで制作したWebアプリ。お笑い芸人が路上ライブを行なっている場所をマップ上に表示させる。ハッカソンの成績は準優勝であった。綿岡はデザイン, iOS版のフロントエンド, プレゼンターを担当した。",
        "qiita": "",
        "github": ""
    },
    {
        "name": "月文字エンジン",
        "image": "images/tsuki.png",
        "description": "画像を月の絵文字に変換するエンジン。記事がQiitaのトレンドランキングで3期連続1位を記録した。また、このエンジンを使用したサイトがYoutubeのコメント欄でめちゃくちゃバズった。",
        "qiita": "https://qiita.com/wataoka/items/261fc12c956a517049d8",
        "github": "https://github.com/wataoka/tsuki"
    },
    {
        "name": "台風偏差値計算機",
        "image": "images/typhoon.png",
        "description": "任意の台風が過去の台風の中でどれほどの強さを持っているのかを偏差値で出力してくれるエンジン。Wikipediaにある過去20年間の台風のデータをスクレイピングしている。スクレイピングの練習目的で制作した。",
        "qiita": "https://qiita.com/wataoka/items/61613f1ab259025cdb2b",
        "github": "https://github.com/wataoka/typhoon"
    },
    {
        "name": "歌詞生成AI",
        "image": "images/kashi.png",
        "description": "ほぼ任意の歌手に似た歌詞を生成してくれるAI。複数歌手を入力すると歌手通しの足し合わせもしてくれる。モデルはLSTMを使用している。",
        "qiita": "",
        "github": "https://github.com/wataoka/kashi"
    },
    {
        "name": "Todo API",
        "image": "images/todo.png",
        "description": "フロントエンドとバックエンドを切り分けたアプリを練習したかったので作りました。",
        "qiita": "https://qiita.com/wataoka/items/98e2ca53091b629ec165#-indexhtml",
        "github": "https://github.com/wataoka/todo-api"
    },
    ]

def get_work_data(work_name):
    for work in work_list:
        if work['name'] == work_name:
            return work
    return None

def get_work_list():
    return work_list