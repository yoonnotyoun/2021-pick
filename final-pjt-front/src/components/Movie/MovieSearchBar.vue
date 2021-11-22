<template>
  <div>
    <input @keypress.enter="getMovieSearchResult" type="text" placeholder="Movie Search">
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'MovieSearchBar',
  methods: {
    ...mapActions([
      // 'setInputValue',
      'getMovieSearchResult',
    ])
  },
  computed: {
    ...mapState([
      'userInput',
      'movies',
    ])
  },
}
</script>

<style>

</style>