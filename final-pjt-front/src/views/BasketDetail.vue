<template>
  <div class="container my-5">
    <!-- 바스켓 소개 -->
    <div class="card p-3 border-light">
      <div class="row">
        <div class="card col-6 border-light" style="max-width: 400px;">
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
        <div class="card col border-light">
          <p v-if="selectedBasketDetail.public === true">공개</p>
          <p v-else>비공개</p>
          <p>제목 : {{ selectedBasketDetail.title }}</p>
          <p @click="getProfile(selectedBasketDetail.author)" class="" style="cursor:pointer">닉네임: {{ userInfo[selectedBasketDetail.author].nickname }}</p>
          <p class="">팔로워 {{ userInfo[selectedBasketDetail.author].fans.length }}명</p>
          <!-- 태그 -->
          <span v-for="(basket_tag, idx) in selectedBasketDetail.baskets_tags" :key="'basket' + idx">{{ basket_tag.name }} </span>
          <p>설명 : {{ selectedBasketDetail.explanation }}</p>
          <p>좋아요 개수: {{ likeCnt }}</p>
          <div v-if="selectedBasketDetail.public === true">
            <p>이 바스켓을 좋아하는 {{ selectedBasketDetail.like_users.length }}명</p>
            <span v-for="(like_user, idx) in selectedBasketDetail.like_users" :key="'like_user' + idx">{{ userInfo[like_user.id].nickname }} </span>
          </div>
          <div v-else>
            <p>이 바스켓에 참여중인 {{ selectedBasketDetail.participants.length }}명</p>
            <div>
              <span v-for="(participant, idx) in selectedBasketDetail.participants" :key="'participant' + idx">{{ userInfo[participant.id].nickname }} </span>
            </div>
          </div>
          <button @click="likeUnlike(selectedBasketDetail.id)">{{ likeButtonName }}</button>
          <button @click="updateBasket(selectedBasketDetail)" v-if="userId === selectedBasketDetail.author">수정</button>
          <button @click="deleteBasket(selectedBasketDetail)" v-if="userId === selectedBasketDetail.author">삭제</button>
        </div>
      </div>
    </div>
    <!-- 영화 -->
      <div class="d-flex align-items-end">
        <h5 class="d-inline-block me-2">이 바스켓의</h5>
        <h4 class="strong-text mb-2">영화 리스트</h4>
      </div>
    <div class="container">
      <b-card-group class="row row-cols-3 row-cols-lg-6">
        <movie-list-item v-for="(movie, idx) in selectedBasketDetail.movies"
          :movie="movie"
          :key="'movie' + idx"
        ></movie-list-item>
      </b-card-group>
    </div>
    <!-- 테이스팅 홀 -->
    <div class="d-flex justify-content-between align-items-center">
      <div class="d-flex align-items-end">
        <h5 class="d-inline-block me-2">영화에 대해 이야기 나누는</h5>
        <h4 class="strong-text mb-2">테이스팅 홀</h4>
      </div>
      <b-form-checkbox @change="setSpoilerFilter(showSpoiler)" v-model="showSpoiler" name="spoiler-button" switch class="d-inline-block">
      스포일러 보기
      </b-form-checkbox>
    </div>
    <span class="card p-4 border-light">
      <comment-list></comment-list>
    </span>
  </div>
</template>

<script>
import CommentList from '@/components/Basket/CommentList.vue'

import { mapState, mapActions } from 'vuex'
import MovieListItem from '../components/Movie/MovieListItem.vue'

export default {
  name: 'BasketDetail',
  data: function () {
    return {
      showSpoiler: false,
    }
  },
  components: {
    CommentList,
    MovieListItem,
  },
  methods: {
    ...mapActions('basketStore', [
      'setSpoilerFilter',
      'likeUnlike',
      'getLikeButtonName',
      'updateBasket',
      'deleteBasket',
    ]),
    ...mapActions('accountStore', [
      'getProfile',
    ]),
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
      userInfo: state => state.userInfo
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