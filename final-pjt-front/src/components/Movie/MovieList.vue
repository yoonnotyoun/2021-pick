<template>
  <div class="container-fluid m-5">
    <div v-for="(movieListData, idx) in recommendedMovies"
      :movieListData="movieListData"
      :key="idx">{{ movieListData.recommended_name }}{{ recommendedTail[idx] }}
      <div class="movie-search-result row row-cols-3 row-cols-sm-6">
        <movie-list-item v-for="(movie, idx) in movieListData.movies"
          :movie="movie"
          :key="idx"
        ></movie-list-item>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import MovieListItem from './MovieListItem.vue'

export default {
  components: { MovieListItem },
  name: 'MovieList',
  computed: {
    ...mapState('movieStore', {
      recommendedMovies: state => state.recommendedMovies,
      recommendedMethod: state => state.recommendedMethod,
      recommendedTail: state => state.recommendedTail,
    })
  }
}
</script>

<style>

</style>