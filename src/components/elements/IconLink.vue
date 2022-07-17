<template>
  <div class="icon-link px-1">
    <a :href="url">
        <img :src="svg" class="w-8">
    </a>
  </div>
</template>

<script>
export default {
  name: "IconLink",
  props: [
    "svg",
    "url"
  ],
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
