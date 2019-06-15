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
             description="このサイトのことです。flaskの静的サイトジェネレータのfrozen flaskと言うライブラリを使用しました。",
             date="2019年3月15日")

work02 = Work(id=2,
             name="GUIで設計できるAI",
             image="guiai01.png",
             description="GUIでディープラーニングの設計ができるアプリ。タスクは手書き文字認識のみ。自作したモデルを学習させた結果をランキングで表示する機能もある。",
             date="2017年11月20日")

work03 = Work(id=3,
             name="upCamera",
             image="upcamera.png",
             description="カメラで撮った写真を0タップでtwitterにアップロードするiOSアプリ。Twitterにサーバーにバックアップする目的で作ったが、今は全く使っていない。",
             date="2018年2月15日",
             github="")

work04 = Work(id=4,
             name="OWALIVE",
             image="owalive.png",
             description="2018年3月8-9日に開催されたTrunk Hachathonで制作したWebアプリ。お笑い芸人が路上ライブを行なっている場所をマップ上に表示させる。ハッカソンの成績は準優勝であった。綿岡はデザイン, iOS版のフロントエンド, プレゼンターを担当した。",
             date="2018年3月9日")

work05 = Work(id=5,
             name="月文字エンジン",
             image="tsuki.png",
             description="画像を月の絵文字に変換するエンジン。記事がQiitaのトレンドランキングで3期連続1位を記録した。また、このエンジンを使用したサイトがYoutubeのコメント欄でめちゃくちゃバズった。",
             date="2018年6月14日",
             qiita="https://qiita.com/wataoka/items/261fc12c956a517049d8",
             github="https://github.com/wataoka/tsuki")

work06 = Work(id=6,
             name="台風偏差値計算機",
             image="typhoon.png",
             description="任意の台風が過去の台風の中でどれほどの強さを持っているのかを偏差値で出力してくれるエンジン。Wikipediaにある過去20年間の台風のデータをスクレイピングしている。スクレイピングの練習目的で制作した。",
             date="2018年9月4日",
             qiita="https://qiita.com/wataoka/items/61613f1ab259025cdb2b",
             github="https://github.com/wataoka/typhoon")

work07 = Work(id=7,
             name="歌詞生成AI",
             image="kashi.png",
             description="ほぼ任意の歌手に似た歌詞を生成してくれるAI。複数歌手を入力すると歌手通しの足し合わせもしてくれる。モデルはLSTMを使用している",
             date="2018年11月9日",
             github="https://github.com/wataoka/kashi")

work08 = Work(id=8,
             name="Todo API",
             image="todo.png",
             description="フロントエンドとバックエンドを切り分けたアプリを練習したかったので作りました。",
             date="2019年3月20日",
             qiita="https://qiita.com/wataoka/items/98e2ca53091b629ec165#-indexhtml",
             github="https://github.com/wataoka/todo-api")

work09 = Work(id=9,
             name="make10",
             image="make10.png",
             description="計算パズルゲーム。4つの数字と四則演算と括弧を使って10を作るゲームで、10問解くまでのタイムを競います。開発ではバックエンドを担当しました。フレームワークはDjangoです。",
             date="2019年5月18日",
             github="https://github.com/rokuyon/make10_project/")

all_works = [work01, work02, work03, work04, work05, work06, work07, work08]