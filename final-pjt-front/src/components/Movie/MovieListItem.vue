<template>
  <div class="col" @click="getMovieDetail(movie)">
    <div class="card">
      <img :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path" alt="poster">
      <div class="card-body">
        <p>{{ movie.title }}</p>
        <p>{{ movie.release_date }}</p>
        <p>{{ movie.like_users }}</p>
        <p>{{ movie.vote_average }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'MovieListItem',
  props: {
    movie: {
      type: Object,
    },
  },
  methods: {
    ...mapActions('movieStore', [
      'getMovieDetail',
    ])
  },
  computed: {
    ...mapState('movieStore', {
      pickedMovies: state => state.pickedMovies
    })
  }
}
</script>

<style>

</style>