<template>
  <div>
    <!-- <movie-detail-modal v-if="isModalViewed" @close-modal="isModalViewed=false"></movie-detail-modal> -->
    <h2>영화</h2>
    <h3>영화검색창 / 추천기준 5줄</h3>
    <movie-search-bar></movie-search-bar>
    <movie-search-result v-if="searchedMovies"></movie-search-result>
    <movie-list v-if="recommendedMovies"></movie-list>
  </div>
</template>

<script>
import MovieSearchBar from '@/components/Movie/MovieSearchBar.vue'
import MovieList from '@/components/Movie/MovieList.vue'
import MovieSearchResult from '@/components/Movie/MovieSearchResult.vue'
// import MovieDetailModal from '@/components/Movie/MovieDetailModal.vue'

import { mapState, mapActions } from 'vuex'

export default {
  name: 'Movie',
  components: {
    MovieList,
    MovieSearchBar,
    MovieSearchResult,
    // MovieDetailModal,
  },
  methods: {
    ...mapActions('movieStore', [
      'getMovieRecommendation'
    ])
  },
  computed: {
    ...mapState('movieStore', {
      searchedMovies: state => state.searchedMovies,
      recommendedMovies: state => state.recommendedMovies,
      // 'searchedMovies',
      // 'recommendedMovies',
      // 'selectedMovie',
      // 'isModalViewed',
    })
  },
  created: 
  function () {
    console.log(this.recommendedMovies)
    // if (this.$store.getters.isLoggedIn) {
    //   while (this.recommendedMovies.length < 5) {
    //     this.getMovieRecommendation()
    //   }
    // }
  }
}
</script>

<style>

</style>