<template>
  <div>
    <h2>영화</h2>
    <h3>영화검색창 / 추천기준 5줄</h3>
    <movie-search-bar></movie-search-bar>
    <movie-search-result></movie-search-result>
  </div>
</template>

<script>
// import MovieList from '@/components/Movie/MovieList.vue'
import MovieSearchBar from '@/components/Movie/MovieSearchBar.vue'
import MovieSearchResult from '@/components/Movie/MovieSearchResult.vue'

export default {
  name: 'Movie',
  components: {
    MovieSearchBar,
    MovieSearchResult,
  },
}
</script>

<style>

</style>