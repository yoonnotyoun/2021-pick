<template>
  <div>
    <header>
      <!-- <img :src="userInfo.image" alt="profile"> -->
      <p>{{ profileInfo.username }}</p>
      <p>{{ profileInfo.nickname }}</p>
      <span v-for="(tag, idx) in tags" :key="idx">{{ tag }} </span>
      <br>
      <span>팔로워: {{ profileInfo.fans.length }} / </span>
      <span>팔로잉: {{ profileInfo.stars.length }}</span>
      <button @click="followUnfollow" v-if="userId !== profileInfo.id">{{ followButtonName }}</button>

      <div>{{ profileInfo.nickname }}님이 작성한 바스켓</div>
      <ul v-for="(author_basket, idx) in profileInfo.author_baskets" :key="'author_baskets' + idx">{{ author_basket }}</ul>
      <div>{{ profileInfo.nickname }}님이 좋아하는 바스켓</div>
      <ul v-for="(like_basktet, idx) in profileInfo.like_basktets" :key="'like_basktet' + idx">{{ like_basktet }}</ul>
      <div>{{ profileInfo.nickname }}님이 좋아하는 영화</div>
      <ul v-for="(like_movie, idx) in profileInfo.like_movies" :key="'like_movie' + idx">{{ like_movie }}</ul>
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
      'getProfile',
      'follow',
      'unfollow',
      'getFollowButtonName',
    ]),
    followUnfollow: function() {
      if (this.followButtonName === '팔로우') {
        this.follow(this.profileInfo.id)
      } else {
        this.unfollow(this.profileInfo.id)
      }
      this.getFollowButtonName(this.profileInfo.id)
    }
  },
  computed: {
    ...mapState('accountStore', {
      profileInfo: state => state.profileInfo,
      tags: state => state.tags,
      followButtonName: state => state.followButtonName,
    }),
    ...mapState({
      userId: state => state.userId,
    })
  },
  created: function () {
    this.getProfile(this.userId) // 나중에 다른 회원 정보랑 분리해야됨
    this.getFollowButtonName(this.profileInfo)
  }
}
</script>

<style>

</style>