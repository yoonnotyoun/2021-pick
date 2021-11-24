<template>
  <div class="container">
    <div class="card p-3">
      <div class="row">
        <div class="card col-6 border-light" style="max-width: 230px;" @click="getBasketDetail(basket)">
          <div v-if="basket.movies.length > 3">
            <div class="container">
              <div class="row row-cols-2 m-0 p-0">
                <div class="imgContainer col m-0 p-0" v-for="(movie, idx) in basket.movies.slice(0,4)" :key="idx">
                  <img :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path" alt="poster" class="image">
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="card col me-3 border-light">
          <p @click="getBasketDetail(basket)" style="cursor:pointer">제목: {{ basket.title }}</p>
          <p @click="getProfile(basket.author)" style="cursor:pointer">닉네임: {{ userInfo[basket.author].nickname }}</p>
          <span>태그: </span>
          <span v-for="(basket_tag, idx) in basket.baskets_tags" :key="'basket' + idx">{{ basket_tag.name }}</span>
          <p>좋아요개수: {{ basket.like_users.length }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'BasketListItem',
  props: {
    basket: {
      type: Object,
    },
  },
  methods: {
    ...mapActions('basketStore', [
      'getBasketDetail',
    ]),
    ...mapActions('accountStore', [
      'getProfile',
    ]),
  },
  computed: {
    ...mapState({
      userInfo: state => state.userInfo
    })
  }
}
</script>

<style>
/* * {
  background: grey;
} */

.imgContainer {
  width: 100px;
  height: 100px;
  overflow: hidden;
}
.imgContainer > img {
  width: 100%;
  object-fit: fill;
  /* height: 200px; */
}
</style>