<template>
  <div class="mt-5"><br>
    <b-row>
      <b-col md="3">
        <b-avatar src="@/assets/profile-image.png"></b-avatar>
      </b-col>
      <b-col md="9">
        
      </b-col>
    </b-row>
    <div>
      <!-- <img :src="userInfo.image" alt="profile"> -->
      <p>{{ profileInfo.nickname }}</p>
      <span v-for="(tag, idx) in tags" :key="idx">{{ tag }} </span>
      <br>
      <span>팔로워: {{ profileInfo.fans.length }} / </span>
      <span>팔로잉: {{ profileInfo.stars.length }}</span>
      <button @click="followUnfollow" v-if="userId !== profileInfo.id">{{ followButtonName }}</button>
      <div class="container">
        <div class="d-flex align-items-end">
          <h4 class="strong-text mb-2">{{ profileInfo.nickname }}</h4>
          <h5 class="d-inline-block ms-2">님이 작성한 바스켓</h5>
        </div>
        <div class="basket-search-result row row-cols-1 row-cols-md-2 row-cols-xl-3">
          <basket-list-item v-for="(basket, idx) in authorBaskets"       
            :key="'author_baskets' + idx"
            :basket="basket"
          ></basket-list-item>
        </div>
      </div>
      <!-- <ul v-for="(author_basket, idx) in profileInfo.author_baskets" :key="'author_baskets2' + idx">{{ author_basket }}</ul> -->
      <div class="container">
        <div class="d-flex align-items-end">
          <h4 class="strong-text mb-2">{{ profileInfo.nickname }}</h4>
          <h5 class="d-inline-block ms-2">님이 좋아하는 바스켓</h5>
        </div>
        <div class="basket-search-result row row-cols-1 row-cols-md-2 row-cols-xl-3">
          <basket-list-item v-for="(basket, idx) in likeBaskets"       
            :key="'like_baskets' + idx"
            :basket="basket"
          ></basket-list-item>
        </div>
      </div>
      <!-- <ul v-for="(like_basktet, idx) in profileInfo.like_basktets" :key="'like_basktet' + idx">{{ like_basktet }}</ul> -->
      <div class="container">
        <div class="d-flex align-items-end">
          <h4 class="strong-text mb-2">{{ profileInfo.nickname }}</h4>
          <h5 class="d-inline-block ms-2">님이 좋아하는 영화</h5>
        </div>
        <b-card-group class="row row-cols-3 row-cols-lg-6">
          <movie-list-item v-for="(movie, idx) in likeMovies"
            :movie="movie"
            :key="'movie' + idx"
          ></movie-list-item>
        </b-card-group>
      </div>
      <!-- <ul v-for="(like_movie, idx) in profileInfo.like_movies" :key="'like_movie' + idx">{{ like_movie }}</ul> -->
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import BasketListItem from '../../components/Basket/BasketListItem.vue'
import MovieListItem from '../../components/Movie/MovieListItem.vue'
// import axios from 'axios'
// import SERVER from '@/api/drf.js'
// import SERVER from '@/api/drf.js'

export default {
  components: { BasketListItem, MovieListItem },
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
    // ...mapGetters([
    //   'config'
    // ]),
    followUnfollow: function() {
      if (this.followButtonName === '팔로우') {
        this.follow(this.profileInfo.id)
      } else {
        this.unfollow(this.profileInfo.id)
      }
      console.log('getFollowButtonName', this.profileInfo)
      this.getFollowButtonName(this.profileInfo)
    },
  },
  computed: {
    ...mapState('accountStore', {
      profileInfo: state => state.profileInfo,
      tags: state => state.tags,
      followButtonName: state => state.followButtonName,
      authorBaskets: state => state.authorBaskets,
      likeBaskets: state => state.likeBaskets,
      likeMovies: state => state.likeMovies,
    }),
    ...mapState({
      userId: state => state.userId,
    })
  },
  created: function () {
    // this.getProfile(this.userId) // 나중에 다른 회원 정보랑 분리해야됨
    // this.getFollowButtonName(this.profileInfo)
    console.log(this.$route.params.userId)
    console.log(this.userId)
    if (this.$route.params.userId === this.userId) {
      this.getProfile(this.$route.params.userId)
    }
    this.profileId = this.$route.userId
    // this.getAuthorBaskets(this.$route.userId)
  }
}
</script>

<style>

</style>