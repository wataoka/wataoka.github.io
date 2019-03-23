from work import Work

def get_work(work_name):
    for work in all_works:
        if work.name == work_name:
            return work
    return None

def get_all_works():
    return all_works


work01 = Work(id=1,
             name="ホームページ",
             image="banner.jpg",
             description="このサイトのことです。flaskの静的サイトジェネレータのfrozen flaskと言うライブラリを使用しました。")

work02 = Work(id=2,
             name="GUIで設計できるAI",
             image="guiai01.png",
             description="GUIでディープラーニングの設計ができるアプリ。タスクは手書き文字認識のみ。自作したモデルを学習させた結果をランキングで表示する機能もある。")

work03 = Work(id=3,
             name="upCamera",
             image="upcamera.png",
             description="カメラで撮った写真を0タップでtwitterにアップロードするiOSアプリ。Twitterにサーバーにバックアップする目的で作ったが、今は全く使っていない。",
             github="")

work04 = Work(id=4,
             name="OWALIVE",
             image="owalive.png",
             description="2018年3月8-9日に開催されたTrunk Hachathonで制作したWebアプリ。お笑い芸人が路上ライブを行なっている場所をマップ上に表示させる。ハッカソンの成績は準優勝であった。綿岡はデザイン, iOS版のフロントエンド, プレゼンターを担当した。")

work05 = Work(id=5,
             name="月文字エンジン",
             image="tsuki.png",
             description="画像を月の絵文字に変換するエンジン。記事がQiitaのトレンドランキングで3期連続1位を記録した。また、このエンジンを使用したサイトがYoutubeのコメント欄でめちゃくちゃバズった。",
             qiita="https://qiita.com/wataoka/items/261fc12c956a517049d8",
             github="https://github.com/wataoka/tsuki")

work06 = Work(id=6,
             name="台風偏差値計算機",
             image="typhoon.png",
             description="任意の台風が過去の台風の中でどれほどの強さを持っているのかを偏差値で出力してくれるエンジン。Wikipediaにある過去20年間の台風のデータをスクレイピングしている。スクレイピングの練習目的で制作した。",
             qiita="https://qiita.com/wataoka/items/61613f1ab259025cdb2b",
             github="https://github.com/wataoka/typhoon")

work07 = Work(id=7,
             name="歌詞生成AI",
             image="kashi.png",
             description="ほぼ任意の歌手に似た歌詞を生成してくれるAI。複数歌手を入力すると歌手通しの足し合わせもしてくれる。モデルはLSTMを使用している",
             github="https://github.com/wataoka/kashi")

work08 = Work(id=8,
             name="Todo API",
             image="todo.png",
             description="フロントエンドとバックエンドを切り分けたアプリを練習したかったので作りました。",
             qiita="https://qiita.com/wataoka/items/98e2ca53091b629ec165#-indexhtml",
             github="https://github.com/wataoka/todo-api")

all_works = [work01, work02, work03, work04, work05, work06, work07, work08]