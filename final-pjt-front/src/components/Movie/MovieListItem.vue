<template>
  <div class="col" @click="getMovieDetail(movie)">
    <div class="card">
      <img :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path" alt="poster">
      <!-- <h3 v-show="checked">p!cked</h3> -->
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
  // data: function () {
  //   return {
  //     checked: this.checkPickedMovies(this.movie),
  //   } 
  // },
  methods: {
    ...mapActions('movieStore', [
      'getMovieDetail',
      // 'checkPickedMovies',
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