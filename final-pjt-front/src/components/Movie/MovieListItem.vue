<template>
  <div class="col" @click="setSelectedMovie(movie)">
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
    }
  },
  methods: {
    // ...mapMutations([
    //   'SET_SELECTED_MOVIE',
    // ]),
    ...mapActions([
      'setSelectedMovie',
    ])
  },
  computed: {
    ...mapState([
      'selectedMovie',
    ])
  }
}
</script>

<style>

</style>