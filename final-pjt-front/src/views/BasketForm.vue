<template>
  <div class="container mt-5">
    <div><br>
      <p class="d-inline-block"
      style="font-family: 'Hahmlet', serif; font-weight: 600; font-size: 1.6rem; color: #222222;"
      >바스켓</p>
      <p class="d-inline-block ms-1">생성하기</p>
    </div>
    
    <!-- form start -->
    <div class="input-signup">
      <label for="title" class="d-flex">바스켓 이름</label>
      <b-form-input
        id="title"
        type="text"
        v-model="info.title"
        placeholder="바스켓 이름을 입력해주세요."></b-form-input>
    </div>
    <!-- <div>
      <label for="title">바스켓 이름: </label>
      <input type="text" id="title" v-model="info.title">
    </div> -->
    <div class="input-signup">
      <div class="d-flex" align="left">
        <label for="explanation" class="d-inline-block">바스켓 설명</label>
        <p class="d-inline-block ms-2 mt-1 mb-0" style="font-size:0.8rem;">(선택)</p>
      </div>
      <b-form-textarea
        id="explanation"
        v-model="info.explanation"
        placeholder="바스켓 설명을 입력해주세요."
        rows="3"
      ></b-form-textarea>
    </div>
    <!-- <div>
      <label for="explanation">바스켓 설명: </label>
      <input type="text" id="explanation" v-model="info.explanation">
    </div> -->
    <div class="input-signup">
      <div class="d-flex" align="left">
        <label for="explanation" class="d-inline-block">바스켓 태그</label>
        <p class="d-inline-block ms-2 mt-1 mb-0" style="font-size:0.8rem;">(선택)</p>
      </div>
      <b-form-tags
        input-id="basket_tags_names"
        v-model="info.basket_tags_names"
        placeholder="바스켓을 대표할 태그를 등록해주세요."
      ></b-form-tags>
    </div>
    <div class="input-signup pb-0">
      <b-form-group label="공개 설정" align="left" style="font-weight:600;">
        <b-form-radio-group
          v-model="info.public"
          buttons
          button-variant="outline-secondary"
          size="sm"
          class="mx-n1"
          align="left"
        ><template v-for="publicOption in publicOptions">
            <b-form-radio :value="publicOption.value" :key="publicOption.text" class="rounded-pill mx-1">
              {{ publicOption.text }}
            </b-form-radio>
          </template>
        </b-form-radio-group>
      </b-form-group>
    </div>
    <!-- public 비공개 선택 시 친구 선택 창 나타내기 -->
    <div class="input-signup">
      <b-card v-if="info.public === 'False'" align="left">
        <p style="font-weight: 600;">친구 그룹 초대</p>
        <ul>
          <span v-for="(group, idx) in groups" :key="idx">
            <input type="checkbox" :value="group.id" v-model="info.groups_ids">
            <span class="ms-2" @click="setGroupFilterId(group.id)">{{ group.name }}</span><br>
          </span>
        </ul>
      </b-card>
    <!-- </b-collapse> -->
    </div>
    <!-- 영화 선택 -->
    <div>
      <div class="input-signup">
        <div class="d-flex" align="left">
          <label for="pickedMovies" class="d-inline-block">선택 영화 목록</label>
          <p class="d-inline-block ms-2 mt-1 mb-0" style="font-size:0.8rem; color:#999999;">아래 검색창을 통해 4개 이상의 영화를 추가해주세요.</p>
        </div>
        <b-form-tags
          input-id="pickedMovies"
          v-model="pickedMovieTitleList"
          tag-variant="secondary"
          tag-pills
          size="md"
          separator=" "
          :disabled="true"
          placeholder=""
          style="background-color:#ffffff;"
        ></b-form-tags>
      </div>
      <div align="right" class="input-signup" >
        <p class="d-inline-block">{{ pickedMovieList.length }}개의 영화로 바스켓</p>
        <b-button class="action-button d-inline-block ms-2" @click="beforeCreate">생성하기</b-button>
      </div>
      <movie-search-bar></movie-search-bar>
      <movie-search-result class="input-signup"></movie-search-result>
    </div>
  </div>
</template>

<script>
import MovieSearchBar from '@/components/Movie/MovieSearchBar'
import MovieSearchResult from '@/components/Movie/MovieSearchResult'

import { mapState, mapActions } from 'vuex'


export default {
  name: 'BasketForm',
  data: function () {
    return {
      publicOptions: [
        { text: '공개', value: 'True' },
        { text: '비공개', value: 'False' },
      ],
      info: {
        title: '',
        explanation: '',
        basket_tags_names: [],
        public: '',
        groups_ids: [],
        movies_ids: [],
      }
    }
  },
  components: {
    MovieSearchBar,
    MovieSearchResult,
  },
  methods: {
    beforeCreate: function () {
      this.info.movies_ids = this.pickedMovieIdList
      this.createBasket(this.info)
      this.resetMovies('picked')
      this.resetMovies('pickedId')
      this.resetMovies('pickedTitle')
    },
    ...mapActions('movieStore', [
      'resetMovies',
    ]),
    ...mapActions('accountStore', [
      'getGroups',
    ]),
    ...mapActions('basketStore', [
      'createBasket',
    ]),
  },
  computed: {
    ...mapState('movieStore', {
      pickedMovie: state => state.pickedMovie,
      pickedMovieList: state => state.pickedMovieList,
      pickedMovieIdList: state => state.pickedMovieIdList,
      pickedMovieTitleList: state => state.pickedMovieTitleList,
    }),
    ...mapState('accountStore', {
      groups: state => state.groups,
    }),
  },
  created: function () {
    this.getGroups()
  }
}
</script>

<style>

</style>