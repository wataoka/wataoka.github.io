<template>
  <a :href="url" class="block p-6 bg-white shadow-md rounded-md hover:bg-gray-100">
    <h3 class="tracking-tight ">{{ title }}</h3>
    <p class="mt-2 text-gray-400 text-sm">投稿日 : {{ date }}</p>
    <p class="mt-2">{{ description }}</p>
  </a>
</template>

<script>
export default {
  name: "PostCard",
  props: [
    "url",
    "title",
    "date",
    "description"
  ]
};
</script>
