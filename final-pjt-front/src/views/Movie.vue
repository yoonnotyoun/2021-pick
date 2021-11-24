<template>
  <div>
    <!-- <movie-detail-modal v-if="isModalViewed" @close-modal="isModalViewed=false"></movie-detail-modal> -->
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
      'resetMovies',
      'getMovieRecommendation',
      'resetMovies',
    ])
  },
  computed: {
    ...mapState('movieStore', {
      recommendedMovies: state => state.recommendedMovies,
      searchedMovies: state => state.searchedMovies,
    })
  },
  created: function () {
  // console.log(this.recommendedMovies)
    if (this.$store.getters.isLoggedIn) {
      this.resetMovies('recommended')
      this.resetMovies('method')
      this.resetMovies('tail')
      this.getMovieRecommendation()
      this.getMovieRecommendation()
      this.getMovieRecommendation()
      this.getMovieRecommendation()
      this.getMovieRecommendation()
    }
  }
}
</script>

<style>

</style>