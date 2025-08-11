<template>
  <div class="post mt-10 px-10">
    <h1>Post</h1>
    <div class="mt-1 space-y-6">
        <PostCard
          url="https://engineering.linecorp.com/ja/blog/css2022-report/"
          title="CSS2022参加報告 - LINE Engineering Blog"
          date="2022年11月25日"
          description="2022年10月に開催されたコンピュータセキュリティシンポジウム2022に参加しました。"
        />
        <PostCard
          url="https://tech-verse.me/ja/sessions/239"
          title="AIの信頼性を可視化するストレステスト技術 - Tech-Verse 2022"
          date="2022年11月17日"
          description="2022年11月17,18日に開催されたTech-Verse 2022に登壇しました。"
        />
        <PostCard
          url="https://engineering.linecorp.com/ja/blog/challenge-the-jigsaw-rate-severity-of-toxic-comments/"
          title="文章有害性評価コンペティションへの挑戦 - LINE Engineering Blog"
          date="2022年03月25日"
          description="2021年11月-2022年2月に開催されたKaggleコンペティションJigsaw Rate Severity of Toxic Commentsの体験記です。最終結果は上位6.4%で銅メダルを獲得しました。"
        />
        <PostCard
          url="https://qiita.com/wataoka/items/85a92ec66fb2432a9b4b"
          title="2020年に読んだAI論文100本全部解説 - Qiita"
          date="2020年12月31日"
          description="2020年に読んだ論文を解説した記事です。2021年1月のQiitaトレンド1位を獲得し、2022年現在32,000 views以上閲覧されています。"
        />
        <PostCard
          url="https://qiita.com/wataoka/items/ae782defabc3706b5c93"
          title="2019年、俺の読んだ論文50本全部解説 - Qiita"
          date="2019年12月30日"
          description="2019年に読んだ論文を解説した記事です。2020年1月のQiitaトレンド1位を獲得し、2022年現在35,000 views以上閲覧されています。"
        />
        <PostCard
          url="https://ai-scholar.tech/articles/others/fairness-ai-229"
          title="Fairness入門 - AI-SCHOLAR"
          date="2019年10月10日"
          description="機械学習の公平性について体系的に解説した記事です。この記事はAI-SCHOLARのライターアルバイトして書いたもので編集長賞を受賞しました。"
        />
        <PostCard
          url="https://ai-scholar.tech/articles/treatise/gamo-ai-215"
          title="データ増強をするためのGANモデルGAMO - AI-SCHOLAR"
          date="2019年08月14日"
          description="GANをデータ増強として応用した手法GAMOを解説した記事です。この記事はAI-SCHOLARのライターアルバイトして書いたもので月間TOP PVを記録しました。"
        />
    </div>
  </div>
</template>

<script>
import PostCard from "./elements/PostCard.vue";
export default {
    name: "Post",
    components: {
        PostCard
    },
};
</script>
