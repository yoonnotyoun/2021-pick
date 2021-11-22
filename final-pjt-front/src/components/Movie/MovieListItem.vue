<template>
  <div class="col" @click="SET_SELECTED_MOVIE(movie)">
    <movie-detail-modal :visible="visible"></movie-detail-modal>
    <div class="card" @click="handleClickButton">
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
import { mapMutations, mapState } from 'vuex'
import MovieDetailModal from '@/components/Movie/MovieDetailModal.vue'

export default {
  name: 'MovieListItem',
  data: function () {
    return {
      visible: false
    }
  },
  props: {
    movie: {
      type: Object,
    }
  },
  components: {
    MovieDetailModal
  },
  methods: {
    ...mapMutations([
      'SET_SELECTED_MOVIE',
    ]),
    handleClickButton(){
      this.visible = !this.visible
    }
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