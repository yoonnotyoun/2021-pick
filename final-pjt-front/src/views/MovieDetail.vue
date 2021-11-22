<template>
  <div>
    <p>{{ selectedMovieDetail }}</p>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'MovieDetail',
  methods: {
  },
  computed: {
    ...mapState('movieStore', [
      'selectedMovieDetail'
    ])
  }
}
</script>

<style>

</style>