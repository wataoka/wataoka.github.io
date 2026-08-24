---
title_en: "AIエージェントの安全性入門"
title_ja: "AIエージェントの安全性入門"
date: 2026-08-05
description: "OWASPのAgentic AI脅威分類を軸に、AIエージェントのリスク・評価ベンチマーク・対策を整理する入門記事。"
---

<section>
<h2>はじめに</h2>
<p>
  先月、「<a href="https://www.youtube.com/watch?v=ssWdDNCohAI" target="_blank" rel="noopener">AIが暴走</a>」というような衝撃的な見出しのニュースが各地で報道されました。これは、既知の脆弱性の情報だけを手がかりに、それを悪用して実際に不正な動作を引き起こすプログラム、いわゆるエクスプロイトを組み立てられるかをAIエージェントに問う評価ベンチマーク「<a href="https://arxiv.org/abs/2605.11086" target="_blank" rel="noopener">ExploitGym</a>」の社内評価中に起きた、OpenAIのインシデントを指しています。GPT-5.6 Solを含む複数のモデルが、パッケージレジストリのゼロデイ脆弱性を悪用してサンドボックス環境を抜け出し、盗んだ認証情報と別のゼロデイ脆弱性を連鎖させてHugging Faceの本番サーバーでリモートコード実行に至り、ベンチマークの正解データを直接窃取していたのです（<a href="https://openai.com/ja-JP/index/hugging-face-model-evaluation-security-incident/" target="_blank" rel="noopener">OpenAIの公式発表</a>）。また2025年には、Microsoft 365 Copilotに対し、ユーザーの操作を一切必要としない初のゼロクリック攻撃「<a href="https://www.varonis.com/blog/echoleak" target="_blank" rel="noopener">EchoLeak</a>」が報告されています。
</p>
<p>
  こうした事例が示すのは、ブラウザやコード実行環境を自ら操作する「実行権限」を持ったAIエージェントが、もはや理論上のリスクではなく、実際に事故を起こす段階に入ったということです。単なるチャットボットと違い、AIエージェントは外部のツール・データ・他のエージェントと連携しながら自律的に計画・実行するため、そのリスクは質的に異なり、対策も一筋縄ではいきません。
</p>
<p>
  本記事では、生成AIのセキュリティに関する国際的なコミュニティであるOWASP GenAI Security Projectが2025年12月に公開した、<a href="https://genai.owasp.org/initiatives/agentic-security-initiative/" target="_blank" rel="noopener">Agentic Security Initiative</a>の中核資料<a href="https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/" target="_blank" rel="noopener"><em>"Agentic AI - Threats and Mitigations"</em></a> v1.1を軸に、次の3点を整理します。
</p>
<ol>
  <li>AIエージェント特有のリスク</li>
  <li>それを測るための評価ベンチマーク</li>
  <li>実務で使える安全性対策</li>
</ol>
</section>

<section>
<h2>AIエージェントのリスク</h2>
<p>
  OWASPはAIエージェントを、「入力を受け取り、計画（Planning）・記憶（Memory）・ツール実行（Tool Use）のループを回しながら、自律的にタスクを遂行するソフトウェア」と位置づけています。この構成要素のうち、とくに外部ツールを呼び出す実行権限と、セッションをまたいで情報を保持するメモリこそが、通常のLLM（大規模言語モデル）アプリケーションにはない攻撃対象領域を生み出します。
</p>
<p>
  OWASPは、単一エージェント・マルチエージェントの双方に共通する17種類の脅威（T1〜T17）を定義し、下図のリファレンスアーキテクチャ上にマッピングしています。
</p>

<img src="{{ '/assets/blog/agentic-ai-safety-intro/owasp-reference-threat-model.png' | relative_url }}" alt="OWASPのリファレンスアーキテクチャ上に17個の脅威（T1〜T17）をマッピングした図" style="max-width:100%; height:auto; display:block; margin: 24px auto; border:1px solid var(--line); border-radius:8px;">
<p class="muted" style="text-align:center; font-size:0.85rem; margin-top:-12px;">
  出典: OWASP GenAI Security Project, <em>"Agentic AI - Threats and Mitigations"</em> v1.1（<a href="https://genai.owasp.org/" target="_blank" rel="noopener">genai.owasp.org</a>）の図を一部抜粋・加工。CC BY-SA 4.0（<a href="https://creativecommons.org/licenses/by-sa/4.0/legalcode" target="_blank" rel="noopener">ライセンス全文</a>）。
</p>

<table>
  <thead><tr><th>ID</th><th>脅威</th><th>概要</th></tr></thead>
  <tbody>
    <tr><td>T1</td><td>Memory Poisoning</td><td>短期・長期メモリに悪意あるデータや虚偽情報を注入し、以降の判断や動作を歪める</td></tr>
    <tr><td>T2</td><td>Tool Misuse</td><td>巧妙なプロンプトでツール呼び出しを乗っ取り、権限の範囲内で意図しない操作をさせる（Agent Hijackingを含む）</td></tr>
    <tr><td>T3</td><td>Privilege Compromise</td><td>権限管理の不備を突き、本来アクセスできないはずのデータや機能に到達する</td></tr>
    <tr><td>T4</td><td>Resource Overload</td><td>計算資源やAPI呼び出しを枯渇させ、性能低下やサービス停止を引き起こす</td></tr>
    <tr><td>T5</td><td>Cascading Hallucination Attacks</td><td>もっともらしい誤情報が、メモリや複数エージェント間の連携を通じて増幅・伝播する</td></tr>
    <tr><td>T6</td><td>Intent Breaking &amp; Goal Manipulation</td><td>プロンプトインジェクションなどにより、エージェントの目標や計画をすり替える</td></tr>
    <tr><td>T7</td><td>Misaligned &amp; Deceptive Behaviors</td><td>悪意ある指示がなくても、与えられた目標に過度に固執し、欺瞞的・破壊的な手段を取ってしまう</td></tr>
    <tr><td>T8</td><td>Repudiation &amp; Untraceability</td><td>ログや追跡性が不十分で、誰が何をしたのか事後に検証できない</td></tr>
    <tr><td>T9</td><td>Identity Spoofing &amp; Impersonation</td><td>エージェントや正規ユーザーになりすまし、その権限で不正な操作を行う</td></tr>
    <tr><td>T10</td><td>Overwhelming Human in the Loop</td><td>大量の判断要求で人間の監視者を疲弊させ、承認プロセスを機能不全に陥らせる</td></tr>
    <tr><td>T11</td><td>Unexpected RCE and Code Attacks</td><td>エージェントが生成・実行するコードを悪用し、任意コード実行（RCE）に持ち込む</td></tr>
    <tr><td>T12</td><td>Agent Communication Poisoning</td><td>エージェント間の通信チャネルに偽情報を注入し、意思決定を歪める</td></tr>
    <tr><td>T13</td><td>Rogue Agents in Multi-Agent Systems</td><td>侵害・悪意あるエージェントが、マルチエージェント環境内で監視の目をすり抜けて活動する</td></tr>
    <tr><td>T14</td><td>Human Attacks on Multi-Agent Systems</td><td>エージェント間の委任関係や信頼関係を悪用し、権限昇格やワークフロー妨害を狙う</td></tr>
    <tr><td>T15</td><td>Human Manipulation</td><td>エージェントに対する人間の信頼を逆手に取り、フィッシングや不正送金などへ誘導する</td></tr>
    <tr><td>T16</td><td>Insecure Inter-Agent Protocol Abuse</td><td><a href="https://modelcontextprotocol.io/" target="_blank" rel="noopener">MCP</a>（Model Context Protocol）や<a href="https://a2a-protocol.org/latest/" target="_blank" rel="noopener">A2A</a>（Agent2Agent Protocol）などエージェント間プロトコルの欠陥を突き、同意バイパスやエージェント乗っ取りを行う</td></tr>
    <tr><td>T17</td><td>Supply Chain Compromise</td><td>汚染されたモデル・ライブラリ・ツールを通じて、エージェントの挙動そのものを改ざんする</td></tr>
  </tbody>
</table>

<p>
  冒頭で紹介した2つの事例も、この分類に当てはめると見通しがよくなります。GPT-5.6 Solのインシデントは、モデルが与えられた狭いテスト目標（ExploitGymの正解取得）に過度に最適化し、ゼロデイ脆弱性を連鎖的に悪用するという極端な手段に至った点で、<strong>T7: Misaligned &amp; Deceptive Behaviors</strong>の実例と言えます。攻撃者による悪意ある指示は介在しておらず、モデル自身の目標追求が暴走した点が特徴です。一方、EchoLeakのようなゼロクリック攻撃は、メールなど外部コンテンツに仕込まれた指示でエージェントの動作を書き換える<strong>T6: Intent Breaking &amp; Goal Manipulation</strong>と、Copilotが持つツール実行権限を悪用してデータを持ち出す<strong>T2: Tool Misuse</strong>の複合として整理できます。
</p>
</section>

<section>
<h2>AIエージェントの評価</h2>
<p>
  こうしたリスクをどう測るか、という問いに対して、2024年以降、AIエージェント特有の安全性ベンチマークが相次いで発表されています。ここでは、査読付き国際会議に採択され、一定の引用実績がある代表的な4本を紹介します。
</p>

<div class="pubs">
  <div class="pub">
    <div class="title">InjecAgent</div>
    <div class="meta">
      <a href="https://arxiv.org/abs/2403.02691" target="_blank" rel="noopener">Zhan et al., ACL 2024 Findings</a>（<a href="https://www.semanticscholar.org/paper/c8eee9766f0968e8f1b1be0731bc70b85be0ac97" target="_blank" rel="noopener">Semantic Scholar</a>調べ、2026年8月時点で204件引用）<br>
      ツール統合エージェントに対する間接プロンプトインジェクション（IPI: Indirect Prompt Injection）を専門に評価するベンチマーク。17種類のユーザーツールと62種類の攻撃者ツールを組み合わせた1,054ケースで構成され、ReActプロンプトのGPT-4でも24%のケースで攻撃が成功したと報告している。
    </div>
  </div>
  <div class="pub">
    <div class="title">AgentDojo</div>
    <div class="meta">
      <a href="https://arxiv.org/abs/2406.13352" target="_blank" rel="noopener">Debenedetti et al., NeurIPS 2024（Datasets &amp; Benchmarks Track）</a><br>
      銀行・Slack・メール／カレンダー・旅行予約という4つの実務的なドメインに、97個のユーザータスクと629個の攻撃ケースを配置した動的評価環境。攻撃手法と防御手法を後から追加できる拡張性が特徴で、プロンプトインジェクション研究の標準的な実験基盤として定着している。
    </div>
  </div>
  <div class="pub">
    <div class="title">AgentHarm</div>
    <div class="meta">
      <a href="https://arxiv.org/abs/2410.09024" target="_blank" rel="noopener">Andriushchenko et al., ICLR 2025</a><br>
      詐欺・サイバー犯罪・ハラスメントなど11の被害カテゴリにまたがる、明確に悪意あるエージェントタスク110種（拡張込みで440種）への追従度合いを測るベンチマーク。ジェイルブレイクなしでも主要なLLMが悪意あるタスクに従ってしまうケースが多いこと、また単純な汎用ジェイルブレイク文字列がエージェントにも転用できることを示した。
    </div>
  </div>
  <div class="pub">
    <div class="title">Agent Security Bench (ASB)</div>
    <div class="meta">
      <a href="https://arxiv.org/abs/2410.02644" target="_blank" rel="noopener">Zhang et al., ICLR 2025</a>（<a href="https://www.semanticscholar.org/paper/5f4efbe3aae1d8f44ceab1da257ae685d6beb00b" target="_blank" rel="noopener">Semantic Scholar</a>調べ、2026年8月時点で327件引用）<br>
      Eコマース・自動運転・金融など10シナリオ、400以上のツール、27種類の攻撃・防御手法を横断する包括的な評価フレームワーク。プロンプトインジェクションだけでなくメモリ汚染やPlan-of-Thoughtバックドアも扱い、最大84.3%という高い攻撃成功率と、既存の防御手法の限界を明らかにした。
    </div>
  </div>
</div>

<p>
  4本を通じて見えてくるのは、プロンプトインジェクション・悪意あるタスクへの追従・複合的な攻撃という異なる切り口で評価しても、いずれも無視できない攻撃成功率が報告されているという点です。ASBが示すように、現状の防御手法だけでは攻撃を十分に防ぎきれておらず、評価技術に対策技術が追いついていない領域だと言えます。
</p>
</section>

<section>
<h2>AIエージェントの安全性対策</h2>
<p>
  OWASPは、上記17種類の脅威に対応する形で、6つのミティゲーション（対策）プレイブックを提示しています。それぞれ、事前予防（Proactive）・検知後対応（Reactive）・継続監視（Detective）の3段階で具体策を整理しているのが特徴です。
</p>

<table>
  <thead><tr><th>プレイブック</th><th>対象脅威</th><th>主な対策</th></tr></thead>
  <tbody>
    <tr><td>1. 推論操作の防止</td><td>T6, T7, T8</td><td>ツールアクセスの最小化、目標の一貫性検証、暗号学的に改ざん検知可能なロギング</td></tr>
    <tr><td>2. メモリ汚染・ナレッジ破損の防止</td><td>T1, T5</td><td>メモリ更新の出典追跡、コミット前のファクトチェック、異常検知とロールバック</td></tr>
    <tr><td>3. ツール実行・サプライチェーンの保護</td><td>T2, T3, T4, T11, T16, T17</td><td>サンドボックス実行、Just-in-Timeなツール権限付与、AIBOM（AI Bill of Materials、AIソフトウェア部品表）による署名検証</td></tr>
    <tr><td>4. 認証・ID・権限管理の強化</td><td>T3, T9, T16</td><td>暗号学的なエージェントID検証、RBAC（役割ベースアクセス制御）／ABAC（属性ベースアクセス制御）、エージェント間の相互認証</td></tr>
    <tr><td>5. HITL保護・意思決定疲労の防止</td><td>T10, T15</td><td>リスクに応じた承認ルーティング、通知頻度の制限、AIによる判断根拠の要約提示</td></tr>
    <tr><td>6. マルチエージェント通信・信頼の保護</td><td>T12, T13, T14</td><td>メッセージの認証・暗号化、エージェント間の信頼スコアリング、コンセンサス検証</td></tr>
  </tbody>
</table>

<p>
  ここでいうHITL（Human-in-the-Loop）とは、AIの判断や実行に人間の承認や監視を介在させる仕組みのことです。エージェントの規模と複雑さが増すほど、この人間の監視能力そのものが攻撃対象になり得る（T10）という指摘は、単純ながら見落とされやすい観点だと思います。
</p>
<p>
  重要なのは、これらが<a href="https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/" target="_blank" rel="noopener">OWASP Top 10 for LLM Applications</a>のような既存のLLMセキュリティ対策を置き換えるものではなく、あくまで「エージェントが実行権限とメモリを持つこと」に起因する新しいリスクへの追加対策だという点です。とくにツールのサンドボックス化・最小権限・人間による監視は、単一の技術で解決できるものではなく、開発から運用までを貫くガバナンスの問題として扱う必要があります。
</p>
</section>

<section>
<h2>おわりに</h2>
<p>
  AIエージェントの安全性は、まだ体系化が始まったばかりの領域です。評価ベンチマークが示す高い攻撃成功率が物語るように、対策技術は攻撃技術に追いついていません。それでも、OWASPのような taxonomy（分類体系）が整備されつつあることは、この分野が今後急速に成熟していくことを示していると思います。
</p>

<div class="pub" style="border: 1px solid var(--line); padding: 16px; border-radius: 8px; margin-top: 24px;">
  <div class="title" style="margin-bottom: 8px;">📖 書籍のお知らせ</div>
  <div class="meta">
    本記事で扱った内容は、拙著<a href="https://gihyo.jp/book/2026/978-4-297-15702-9" target="_blank" rel="noopener"><em>『生成AIの安全性入門』</em></a>（技術評論社, 2026年6月）の第8章「AI安全性の未来」でも、対話から実行へと広がるエージェントAIのリスクとして取り上げています。生成AIの安全性を基礎から体系的に学びたい方は、ぜひ手に取ってみてください。
  </div>
</div>
</section>
