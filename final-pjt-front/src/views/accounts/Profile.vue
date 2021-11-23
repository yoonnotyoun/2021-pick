<template>
  <div>
    <header>
      <!-- <img :src="userInfo.image" alt="profile"> -->
      <p>{{ profileInfo.username }}</p>
      <p>{{ profileInfo.nickname }}</p>
      <span v-for="(tag, idx) in tags" :key="idx">{{ tag }} </span>
      <p>팔로워: {{ profileInfo.fans.length }}</p>
      <p>팔로잉: {{ profileInfo.stars.length }}</p>
      <p>{{ profileInfo.nickname }}님이 작성한 바스켓: {{ profileInfo.author_baskets }}</p>
      <p>{{ profileInfo.nickname }}님이 좋아하는 바스켓: {{ profileInfo.like_basktets }}</p>
      <p>{{ profileInfo.nickname }}님이 좋아하는 영화: {{ profileInfo.like_movies }}</p>
    </header>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
// import SERVER from '@/api/drf.js'

export default {
  name: 'Profile',
  methods: {
    ...mapActions('accountStore', [
      'getProfile'
    ])
  },
  computed: {
    ...mapState('accountStore', [
      'profileInfo',
      'tags',
    ])
  },
  created: function () {
    this.getProfile()
  }
}
</script>

<style>

</style>