<template>
  <div>
    <div class="movie-search-result row row-cols-md-6">
      <movie-list-item
        v-for="(movie, idx) in movies"
        :movie="movie"
        :key="idx"
      ></movie-list-item>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import MovieListItem from '@/components/Movie/MovieListItem.vue'

export default {
  name: 'MovieSearchResult',
  components: {
    MovieListItem,
  },
  computed: {
    ...mapState([
      'movies',
    ])
  },
}
</script>

<style>

</style>