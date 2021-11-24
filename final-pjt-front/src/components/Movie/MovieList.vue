<template>
  <div class="container">
    <div v-for="(movieListData, idx) in recommendedMovies"
      :movieListData="movieListData"
      :key="idx">
      <div align="left" class="mt-2">
        <p class="d-inline-block strong-text">'{{ movieListData.recommended_name }}'</p>
        <p class="d-inline-block mx-1">{{ recommendedTail[idx] }}</p>
      </div>
      <b-card-group class="row row-cols-3 row-cols-lg-6">
        <movie-list-item v-for="(movie, idx) in movieListData.movies"
          :movie="movie"
          :key="idx"
        ></movie-list-item>
      </b-card-group>
      <!-- <div class="movie-search-result row row-cols-3 row-cols-sm-6">
        <movie-list-item v-for="(movie, idx) in movieListData.movies"
          :movie="movie"
          :key="idx"
        ></movie-list-item>
      </div> -->
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

.strong-text {
  font-family: 'Hahmlet', serif;
  font-weight: 600;
  color: #5a89cf;
}

</style>