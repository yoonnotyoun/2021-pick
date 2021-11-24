<template>
  <div class="container">
    <div class="card border-light" style="max-width: 400px;">
      <div v-if="selectedBasketDetail.movies.length > 3">
        <div class="container">
          <div class="row row-cols-2 m-0 p-0">
            <div class="imgContainer2 col m-0 p-0" v-for="(movie, idx) in selectedBasketDetail.movies.slice(0,4)" :key="idx">
              <img :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path" alt="poster" class="image">
            </div>
          </div>
        </div>
      </div>
    </div>
    <p>{{ selectedBasketDetail }}</p>
    <p>좋아요 개수: {{ likeCnt }}</p>
    <button @click="likeUnlike(selectedBasketDetail.id)">{{ likeButtonName }}</button>
    <button @click="updateBasket(selectedBasketDetail)" v-if="userId === selectedBasketDetail.author">수정</button>
    <button @click="deleteBasket(selectedBasketDetail)" v-if="userId === selectedBasketDetail.author">삭제</button>
    <h2>이 바스켓에서 이야기 나누는 공간</h2>
    <b-form-checkbox @change="setSpoilerFilter(showSpoiler)" v-model="showSpoiler" name="spoiler-button" switch>
      스포일러 보기
    </b-form-checkbox>
    <comment-list></comment-list>
  </div>
</template>

<script>
import CommentList from '@/components/Basket/CommentList.vue'

import { mapState, mapActions } from 'vuex'

export default {
  name: 'BasketDetail',
  data: function () {
    return {
      showSpoiler: false,
    }
  },
  components: {
    CommentList,
  },
  methods: {
    ...mapActions('basketStore', [
      'setSpoilerFilter',
      'likeUnlike',
      'getLikeButtonName',
      'updateBasket',
      'deleteBasket',
    ])
  },
  computed: {
    ...mapState('basketStore', {
      selectedBasketDetail: state => state.selectedBasketDetail,
      showSpoilerOption: state => state.showSpoilerOption,
      likeButtonName: state => state.likeButtonName,
      likeCnt: state => state.likeCnt,
    }),
    ...mapState({
      userId: state => state.userId,
    })
  },
  created: function () {
    this.getLikeButtonName(this.selectedBasketDetail)
  },
}
</script>

<style>
.imgContainer2 {
  width: 200px;
  height: 200px;
  overflow: hidden;
}
.imgContainer2 > img {
  width: 100%;
  object-fit: fill;
  /* height: 200px; */
}
</style>