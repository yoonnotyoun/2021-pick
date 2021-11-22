<template>
  <div>
    <!-- <movie-detail-modal v-if="isModalViewed" @close-modal="isModalViewed=false"></movie-detail-modal> -->
    <h2>영화</h2>
    <h3>영화검색창 / 추천기준 5줄</h3>
    <movie-search-bar></movie-search-bar>
    <movie-search-result></movie-search-result>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import MovieSearchBar from '@/components/Movie/MovieSearchBar.vue'
import MovieSearchResult from '@/components/Movie/MovieSearchResult.vue'
// import MovieDetailModal from '@/components/Movie/MovieDetailModal.vue'

export default {
  name: 'Movie',
  components: {
    MovieSearchBar,
    MovieSearchResult,
    // MovieDetailModal,
  },
  computed: {
    ...mapState('movieStore', [
      'selectedMovie',
      // 'isModalViewed',
    ])
  }
}
</script>

<style>

</style>