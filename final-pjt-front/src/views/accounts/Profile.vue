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
      <!-- <button @click="followUnfollow" v-if="userId !== profileInfo.id">{{ followButtonName }}</button> -->
      <button @click="followUnfollow">{{ followButtonName }}</button>
      <!-- <button @click="follow(profileInfo.id)" v-show="!isFollowed">팔로우</button>
      <button @click="Unfollow(profileInfo.id)" v-show="isFollowed">언팔로우</button> -->

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
      // 'isFollowed'
      
    ]),
    followUnfollow: function() {
      if (this.followButtonName === '팔로우') {
        console.log(this.profileInfo.id)
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
      userId: state => state.userId,
      followButtonName: state => state.followButtonName,
      getFollowButtonName: state => state.getFollowButtonName
    }),
  },
  created: function () {
    this.getProfile(this.userId) // 나중에 다른 회원 정보랑 분리해야됨
    this.getFollowButtonName(this.profileInfo)
    // this.followButtonName = '팔로우'
    console.log(this.followButtonName)
  }
}
</script>

<style>

</style>