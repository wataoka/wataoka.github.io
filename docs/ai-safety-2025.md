# 2025年、AI Safetyで起きた重要な動き

この一年間、SB IntuitionsのResponsible AIチームのリーダーとして、AI安全性の研究開発に広く携わることができました。
ここでは、私の目線で、2025年に起きた重要な出来事を順を追ってまとめていきます。

## 安全性対策が複雑化

かつてのSafety Alignmentは、モデルの全般的な能力向上と同様に、人間によるアノテーションデータを用いたSFTやRLHFが中心的でした。しかし、今日では、このパラダイムは完全に転換したと言えるでしょう。

特に **RLVF (Reinforcement Learning from Verifiable Feedback)** [https://arxiv.org/abs/2411.15124](https://arxiv.org/abs/2411.15124), [https://arxiv.org/abs/2501.12948](https://arxiv.org/abs/2501.12948) の潮流以降、事後学習における合成データの利用が支配的となり、全体のデータ量は爆発的に増加しました。安全性対策においても、単にSFTデータとPreferenceデータを人手で準備すれば終わりという時代は終焉を迎えました。
しかし、安全性の問題は数学やパズルのように、一律に検証可能な領域ではありません。そのため、体系的に自然言語で記述された安全性ルールである **OpenAI Model Spec** [https://model-spec.openai.com/2025-12-18.html](https://model-spec.openai.com/2025-12-18.html) 等に対し、どれほど忠実にアラインメントできているかを検証する**Collective Alignment** [https://openai.com/index/collective-alignment-aug-2025-updates/](https://openai.com/index/collective-alignment-aug-2025-updates/)のようなアプローチが加速しています。

また、LLMの情報処理能力と正確性が向上したことで、懸念されるリスクも質的に変化しています。単なる不適切な発言の防止を超え、深刻な犯罪行為への悪用リスクが最大の懸念事項となりました。
GPT-5のシステムカード [https://cdn.openai.com/gpt-5-system-card.pdf](https://cdn.openai.com/gpt-5-system-card.pdf) によれば、400人以上の専門家による5,000時間以上のレッドチーミングが実施され、高度な推論能力に伴う悪用リスクへの対策に莫大なリソースが投じられました。
同時に、AutoDAN-Turbo [https://arxiv.org/abs/2410.05295](https://arxiv.org/abs/2410.05295) のような自動レッドチーミング手法の発達を続けています。

2025年は、AIがブラウザやツールを操作する実行権限を本格的に持ち始めた年でもあります。これに伴い、ユーザーの介入なしに機密情報の漏洩などが成立する初のゼロクリック攻撃 **EchoLeak** [https://www.varonis.com/blog/echoleak](https://www.varonis.com/blog/echoleak) が報告されるなど、防御側にはより実務的なセキュリティ対策が求められるようになりました。

こうした状況下で、安全性の確保はもはや単なる機械学習の技術的課題に留まりません。Google DeepMindが提唱する **Frontier Safety Framework** [https://deepmind.google/blog/strengthening-our-frontier-safety-framework/](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/) のように、インシデントへの即応体制やガバナンスを含めた、組織全体としての課題解決が不可欠なフェーズに突入しています。


## ガードレールモデルが飛躍的発展

2025年は、メインのLLMを保護するガードレールモデルが、単なる補助的なフィルターから、それ自体が巨大な計算資源とデータを投じられた高度な推論モデルへと進化した年でした。

これまでガードレールモデルの課題は、学習データに含まれない新しい攻撃手法や、複雑な文脈に潜む有害性を検知できないこと（汎化性能の不足）にありました。しかし、2025年は合成データの戦略的活用により、この壁が突破されました。以下に、主要なガードレールに関する研究を紹介します。

* **Constitutional Classifier [https://arxiv.org/abs/2501.18837](https://arxiv.org/abs/2501.18837):**
  行動規範に基づき、AI自身が多様な攻撃シナリオとそれに対する判定根拠を生成・学習することで、人手では網羅不可能な複雑なタスクへの適応を実現しました。
* **BingoGuard [https://arxiv.org/abs/2503.06550](https://arxiv.org/abs/2503.06550):**
  モデルがどのリスクにどの程度の深刻さで違反しているかを出力するラベルデータを生成し、検知精度と説明可能性の向上を実現しました。
* **DynaGuard [https://arxiv.org/abs/2509.02563](https://arxiv.org/abs/2509.02563):**
  自由なポリシーから学習データを自動生成し、柔軟な判断を可能にする学習フレームワークを確立しました。

研究レベルの進化に留まらず、商用レベルで即戦力となる強力なモデルが相次いで公開され、安全性対策の民主化が進みました。

| モデル名 | 特徴とURL |
| :--- | :--- |
| **LlamaGuard 4** | Metaが公開した、エージェントの行動ログや多言語での安全性判定に特化した最高峰のOSSモデル。[https://www.llama.com/docs/model-cards-and-prompt-formats/llama-guard-4/](https://www.llama.com/docs/model-cards-and-prompt-formats/llama-guard-4/) |
| **gpt-oss-safeguard** | OpenAIがModeration APIの知見をOSSとして提供。商用APIと同等の基準をローカル環境で実現可能に。[https://openai.com/index/introducing-gpt-oss-safeguard/](https://openai.com/index/introducing-gpt-oss-safeguard/) |
| **Qwen3Guard** | 特に東アジア圏の言語や文化特有の有害表現において、極めて高い検知性能を誇る強力なガードレール。[https://github.com/QwenLM/Qwen3Guard](https://github.com/QwenLM/Qwen3Guard) |


## LLMの挙動解明に繋がるいくつかの研究

安全性を高めるためには、単に対策を講じるだけでなく、モデルの内部で何が起きているのかという根本的なメカニズムの解明が不可欠です。2025年は、いくつかの挙動に対し、重要な知見が示されました。

### ハルシネーションが起きる理由
モデルがもっともらしい嘘をつくハルシネーションは、長らくLLM最大の課題でした。OpenAIが公開した分析報告では、これが単なるデータ不足ではなく、学習プロセスにおける不確実性のキャリブレーション不足に起因することが示唆されました。
* **[Why Language Models Hallucinate]** (https://openai.com/index/why-language-models-hallucinate/)
例えば、未知の人物の誕生日を聞かれた場合、1/365の確率で正解し、Rewardが与えられてしまいます。
そのため、モデルにとっては、適当に回答するという選択が最善となることが問題であると指摘されています。

### 自由回答の均質化（Homogenization）への警鐘
RLHF（人間からのフィードバックによる強化学習）の副作用として、モデルの回答が「当たり障りのない、似通ったもの」になってしまう問題が深刻化しています。
* **[The Homogenization of Free-form Responses in LLMs]** (https://arxiv.org/abs/2510.22954)
この研究では、過度なアラインメントがモデルの創造性や多様な視点を奪い、結果として平均的な回答に収束してしまうリスクを指摘しています。

### AIの内省能力（Introspection）の検証
Anthropicによる、モデルの内省能力（自身の思考やバイアスを客観的に認識できるか）についての研究です。
* **[Evaluating Introspection in Large Language Models]** (https://www.anthropic.com/research/introspection)
モデルが回答を生成する前に、自身の論理的な不整合や潜在的な有害性を自己検出し、修正するプロセスの可視化が進んでいます。この「メタ認知」能力の向上は、外部からのガードレールに頼り切らない、モデル内部での「自律的な安全性」の確保に向けた大きな一歩となります。

## まとめ
AI Safetyの分野は、基盤モデルの飛躍的な能力向上と権限の獲得により、急激な進化が要求されている苦境の時代と言えるかもしれません。
しかし、これほど社会に必要とされた時代もなかったかと感じています。
また、2026年はより多くの課題が解決され、新たな挑戦ができるかと思うとワクワクしますね。

また、言語処理学会にて、「チュートリアル1：AI Safety: Bridging Academic Research and Industrial Application(https://anlp.jp/nlp2026/)」という講演をします。
ご興味がある方はぜひご聴講してください。
講演後、本記事を見ていただいた方はぜひ教えてください。
