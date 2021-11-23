<template>
  <div>
    <h2>메인페이지</h2>
    <h3>바스켓 추천기준 2 / 영화 1줄</h3>
    <basket-list></basket-list>
    <movie-list></movie-list>
  </div>
</template>

<script>
import MovieList from '@/components/Movie/MovieList.vue'
import BasketList from '@/components/Basket/BasketList.vue'

import { mapState, mapActions } from 'vuex'

export default {
  name: 'Main',
  components: {
    MovieList,
    BasketList,
  },
  methods: {
    ...mapActions('movieStore', [
      'getMovieRecommendation',
      'resetMovies',
    ]),
    ...mapActions('basketStore', [
      'getBasketRecommendation',
      'resetBaskets',
    ]),
  },
  computed: {
    ...mapState('MovieStore', {
      recommendedMovies: state => state.recommendedMovies,
    }),
    ...mapState('basketStore', {
      recommendedBaskets: state => state.recommendedBaskets,
    }),
  },
  created: function () {
    if (this.$store.getters.isLoggedIn) {
      this.resetBaskets('recommended')
      this.resetMovies('recommended')
      this.getBasketRecommendation()
      this.getBasketRecommendation()
      this.getMovieRecommendation()
    }
  }
}
</script>

<style>

</style>