<template>
  <div class="col" @click="getBasketDetail(basket)">
    <div class="card row">
      <div class="card" style="max-width: 230px;">
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
      <div class="card">
        <p>{{ basket.title }}</p>
        <p>{{ basket.like_users }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

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
    ])
  },
}
</script>

<style>
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