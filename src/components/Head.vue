<template>
  <div class="head">
    <div class="mt-20 flex w-full justify-center">
      <img src="/wataoka2018.jpeg" class="icon drop-shadow-2xl" />
    </div>
    <h2 class="mt-4 w-full text-center">綿岡 晃輝</h2>
    <div class="w-full text-center">LINE株式会社 Trustworthy AIチーム</div>
    <div class="flex justify-center mt-1">
        <IconLink svg="/github.svg" url="https://github.com/wataoka" />
        <IconLink svg="/twitter.svg" url="https://twitter.com/wataoka_koki" />
        <IconLink svg="/youtube.svg" url="https://www.youtube.com/channel/UClZfnIaWYR_WgrWLVu4muvw" />
    </div>
  </div>
</template>

<script>
import IconLink from "./elements/IconLink.vue";
export default {
  name: "Head",
  components: {
    IconLink
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.icon {
  width: 150px;
  border-radius: 100px;
}
</style>
