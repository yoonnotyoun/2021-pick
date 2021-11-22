<template>
  <div>
    <p>{{movies}}</p>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'MovieList',
  methods: {
    ...mapActions([
      'getMovieListRecommendation',
    ])
  },
  computed: {
    ...mapState([
      'movies',
    ])
  },
  created: function () {
    if (this.$store.getters.isLoggedIn) {
      this.getMovieListRecommendation()
    } else {
      // 여기 random 으로 영화 가져오는거 필요한가
    }
  }
}
</script>

<style>

</style>