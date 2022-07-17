<template>
  <div class="pb-20">
    <Head />
    <Abstract />
    <Career />
    <Research />
    <Love />
  </div>
</template>

<script>
import Head from "./components/Head.vue";
import Abstract from "./components/Abstract.vue";
import Career from "./components/Career.vue";
import Research from "./components/Research.vue";
import Love from "./components/Love.vue";

export default {
  name: "App",
  components: {
    Head,
    Abstract,
    Career,
    Research,
    Love
  },
};
</script>

<style>
#app {
  color: #2c3e50;
}
</style>
