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
    ...mapState('movieStore', {
      selectedMovieDetail: state => state.selectedMovieDetail,
      likeButtonName: state => state.likeButtonName,
      likeCnt: state => state.likeCnt,
    })
  },
  created: function () {
    console.log('Movie getLikeButtonName')
    this.getLikeButtonName(this.selectedMovieDetail)
  }
}
</script>

<style>

</style>