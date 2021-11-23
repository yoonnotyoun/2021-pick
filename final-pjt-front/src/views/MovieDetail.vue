<template>
  <div>
    <p>{{ selectedMovieDetail }}</p>
    <p>좋아요 개수: {{ likeCnt }}</p>
    <button @click="likeUnlike(selectedMovieDetail.id)">{{ likeButtonName }}</button>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'MovieDetail',
  methods: {
    ...mapActions('movieStore', [
      'likeUnlike',
      'getLikeButtonName',
    ]),
  },
  computed: {
    ...mapState('movieStore', [
      'selectedMovieDetail',
      'likeButtonName',
      'likeCnt',
    ])
  },
  created: function () {
    this.getLikeButtonName(this.selectedMovieDetail)
  }
}
</script>

<style>

</style>