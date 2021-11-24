<template>
  <div>
    <header>
      <!-- <img :src="userInfo.image" alt="profile"> -->
      <p>{{ profileInfo.nickname }}</p>
      <span v-for="(tag, idx) in tags" :key="idx">{{ tag }} </span>
      <br>
      <span>팔로워: {{ profileInfo.fans.length }} / </span>
      <span>팔로잉: {{ profileInfo.stars.length }}</span>
      <button @click="followUnfollow" v-if="userId !== profileInfo.id">{{ followButtonName }}</button>

      <div class="d-flex align-items-end">
        <h4 class="strong-text mb-2">{{ profileInfo.nickname }}</h4>
        <h5 class="d-inline-block ms-2">님이 작성한 바스켓</h5>
      </div>
      <div class="basket-search-result row row-cols-3">
        <basket-list-item v-for="(basket, idx) in authorBaskets"       
          :key="'author_baskets' + idx"
          :basket="basket"
        ></basket-list-item>
      </div>
      <!-- <ul v-for="(author_basket, idx) in profileInfo.author_baskets" :key="'author_baskets2' + idx">{{ author_basket }}</ul> -->
      <div class="d-flex align-items-end">
        <h4 class="strong-text mb-2">{{ profileInfo.nickname }}</h4>
        <h5 class="d-inline-block ms-2">님이 좋아하는 바스켓</h5>
      </div>
      <ul v-for="(like_basktet, idx) in profileInfo.like_basktets" :key="'like_basktet' + idx">{{ like_basktet }}</ul>
      <div class="d-flex align-items-end">
        <h4 class="strong-text mb-2">{{ profileInfo.nickname }}</h4>
        <h5 class="d-inline-block ms-2">님이 좋아하는 영화</h5>
      </div>
      <ul v-for="(like_movie, idx) in profileInfo.like_movies" :key="'like_movie' + idx">{{ like_movie }}</ul>
    </header>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import BasketListItem from '../../components/Basket/BasketListItem.vue'
// import axios from 'axios'
// import SERVER from '@/api/drf.js'
// import SERVER from '@/api/drf.js'

export default {
  components: { BasketListItem },
  name: 'Profile',
  data: function() {
    return {
      profileId: '',
    }
  },
  methods: {
    ...mapActions('accountStore', [
      'getProfile',
      'follow',
      'unfollow',
      'getFollowButtonName',
    ]),
    ...mapActions('basketStore', [
      'getAuthorBaskets',
    ]),
    // ...mapGetters([
    //   'config'
    // ]),
    followUnfollow: function() {
      if (this.followButtonName === '팔로우') {
        this.follow(this.profileInfo.id)
      } else {
        this.unfollow(this.profileInfo.id)
      }
      console.log(this.profileInfo.id)
      this.getFollowButtonName(this.profileInfo.id)
    },
  },
  computed: {
    ...mapState('accountStore', {
      profileInfo: state => state.profileInfo,
      tags: state => state.tags,
      followButtonName: state => state.followButtonName,
    }),
    ...mapState('basketStore', {
      authorBaskets: state => state.authorBaskets,
    }),
    ...mapState({
      userId: state => state.userId,
    })
  },
  created: function () {
    // this.getProfile(this.userId) // 나중에 다른 회원 정보랑 분리해야됨
    // this.getFollowButtonName(this.profileInfo)
    this.getProfile(this.$route.userId)
    this.profileId = this.$route.userId
    this.getAuthorBaskets(this.$route.userId)
  }
}
</script>

<style>

</style>