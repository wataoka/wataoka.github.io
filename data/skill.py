from .data_manager import Dataset

class Skill:
    def __init__(self, label:str, title:str, stars:int, text:str):
        self.label = label
        self.title = title
        self.stars = stars
        self.text = text

skills_dataset = Dataset()
skills_dataset.set_data_list([
    
    Skill(label="language",
          title="python",
          stars=5,
          text="5年間継続的に使い続けた言語です。機械学習にもWeb開発にも使用し、ほぼ毎日使っているので、文句無しに使えます。"),

    Skill(label="language",
          title="HTML/CSS",
          stars=5,
          text="適切にレスポンシブ対応したサイトを作れます。当サイト(wataoka.info)もレスポンシブ対応しています。"),

    Skill(label="language",
          title="JavaScript",
          stars=4,
          text="趣味でWebアプリを作り続けてきましたので、否が応でも十分に使用できるようになりました。"),

    Skill(label="language",
          title="Typescript",
          stars=3,
          text="クックパッドインターンの際に本腰を入れて勉強しました。async/awaitをしっかりと理解しています。"),

    Skill(label="language",
          title="C/C++",
          stars=4,
          text="大学の授業で4年間習ってきましたので、ポインタ, 名前空間, STLなど必須事項は抑えています。授業でリードソロモン符号の設計をCで行いました。"),

    Skill(label="language",
          title="Java/Scala",
          stars=4,
          text="制約充足問題のソルバーのための構文解析器とパーサーと処理系をscalaで書いたことがあります。Sprint bootをちょっとだけ触ったことあります。"),

    Skill(label="language",
          title="R",
          stars=4,
          text="他人が書いたコードを頻繁に読むことがあります。もちろんデータセットの用意からモデルの評価までを適切に書くこともできます。"),

    Skill(label="language",
          title="Ruby",
          stars=3,
          text="クックパッドインターンの際に頻繁に触りました。railsで簡単なブログサイトを作ったことがあります。"),

    Skill(label="language",
          title="PHP",
          stars=3,
          text="Laravelを用いたバックエンドAPIを作ったことがあります。"),

    Skill(label="language",
          title="Swift",
          stars=4,
          text="大学2回生までiOSアプリ開発をしていました。また、クックパッドインターンの際にcookpad liveというアプリのプロジェクトに配属され、swiftを使用しました。"),

    Skill(label="language",
          title="Go",
          stars=1,
          text="3年前にTour of Goをしました。"),

    Skill(label="framework",
          title="Django",
          stars=4,
          text="最も使用頻度の高いフレームワークです。個人的な全体の開発経験もバックエンド側の開発経験もあります。個人レベルですが、友人との共同開発のため、しっかりとしたプロジェクト管理もできていると思います"),

    Skill(label="framework",
          title="Flask",
          stars=4,
          text="使用頻度が高いわけでは無いですが、疎な結合が好きなので、flaskは好きなwebフレームワークの一つです。このサイトもflaskを使用しています。"),

    Skill(label="framework",
          title="Laravel",
          stars=3,
          text="友人との共同開発でバックエンドを担当することになった時に、APIを設計するために使用しました。"),

    Skill(label="framework",
          title="Ruby on rails",
          stars=2,
          text="練習のために簡単なブログサイトを作っただけで、慣れているとは言えません。"),

    Skill(label="framework",
          title="Spring boot",
          stars=2,
          text="練習のために簡単なTODOアプリを作ったことがあるだけで、慣れているとは言えません。"),

    Skill(label="framework",
          title="RxSwift",
          stars=4,
          text="クックパッドインターンの際に使用しました。Observableあたりをきっちり理解しています。"),

    Skill(label="framework",
          title="その他 bootstrapやjQueryなどのよくあるライブラリ",
          stars=4,
          text="フロントエンドは勉強が泥臭いのであまり好きではありませんが、何度も使ってきているので、嫌でも適切に使えるようになりました。特にbootstrapはほとんど全ての開発に使用しているので、とても慣れ親しんでいます"),

    Skill(label="machine_learning",
          title="Pytorch",
          stars=5,
          text="現在使用しているフレームワークです。研究で使用しているので当たり前のように使用できます。当然, 自作活性化関数, 自作損失関数, 自作モデルなども適切に設計できます。pytorch 1.1.0から標準装備されたtensorboardも使用していますし、実験に関する情報も自動でgoogleスプレッドシートに書き込むようにしていますので、プロジェクト管理もきちんと行えていると思います。"),

    Skill(label="machine_learning",
          title="Tensorflow",
          stars=3,
          text="学部3~4回生の2年間使用してきたフレームワークです。Kerasの限界が見えた時にTensorflowを使用してきました。モデルは必ずKerasで設計してきました。Tensorflowで書かれた他人のコードを読むのが苦手なので星3つとしましたが、Tensorflowがそもそも読みにくいのだと信じています。"),

    Skill(label="machine_learning",
          title="Keras",
          stars=5,
          text="学部3~4回生の2年間使用してきたフレームワークです。Kerasの限界が見えるほど自分で設計してきました。"),

    Skill(label="machine_learning",
          title="sklearn",
          stars=4,
          text="機械学習の基礎的で有名なモデルは3回生の時に全て実験しました。(dicision tree, random forest, svm, etc..."),

    Skill(label="machine_learning",
          title="Chainer",
          stars=1,
          text="Udemyの現場で使えるChainerによるディープラーニング入門を受講したことがあるだけです"),
          
    Skill(label="machine_learning",
          title="Optuna",
          stars=4,
          text="ハイパーパラメータ探索はほとんどOptunaで行います。一時期、hyperasというハイパーパラメータ探索ライブラリを使用していましたが、現在は完全にOptunaに移行しています。"),

    Skill(label="machine_learning",
          title="その他Numpy, Pandasなどの必須ライブラリ",
          stars=5,
          text="呼吸をするように使用してきました。"),

    Skill(label="other",
          title="Git",
          stars=4,
          text="ブランチを切ったり、プルリクエストを送ったりと、適切に共同プロジェクトを進めることができます。研究でもWeb開発でも必ず使用しています。"),

    Skill(label="other",
          title="Docker/Vagrant",
          stars=3,
          text="何度も必要にかられ使用してきていますので基本的なシステムや使用方法は理解していますが、若干苦手意識があります。dockerベースのCI/CD環境を自分で作れと言われればキツイです。"),

    Skill(label="other",
          title="SQL",
          stars=4,
          text="MySQL, SQLite, PostgreSQLを使用したことがあります。ISUCONに出場したことがあり、最適化の知識もありますが、胸を張って得意だとは言えません。"),

    Skill(label="other",
          title="英語",
          stars=4,
          text="機械学習の論文を毎日読んでいますので、リーディングは全く問題ありません。リスニングやスピーキングはDMM英会話を半年ほど受けたので、日常会話なら支障なくできます。TOEICは735点です。(2018年5月)"),

    Skill(label="other",
          title="数学",
          stars=4,
          text="この世で最も好きなものは数学です。数3, 線形代数, 解析, 複素関数, 確率統計, 集合論, 情報数学など高校数学と情報系の大学数学の基本はしっかりと抑えています。他には数論, 情報幾何学, 代数幾何学, 多様体, グレブナ基底などを勉強していますが, どれも何度も挫折しながらの勉強ですので、しっかりと抑えているとは言いたくありません。数学検定は準1級です。(2014年10月くらい"),
        

    
])