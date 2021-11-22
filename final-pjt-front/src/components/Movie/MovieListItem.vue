<template>
  <div class="col">
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
export default {
  name: 'MovieListItem',
  props: {
    movie: {
      type: Object,
    }
  },
  // computed: {
  //   moviePosterSrc: function () {
  //     return this.movie.poster_path
  //   }
  // },
}
</script>

<style>

</style>