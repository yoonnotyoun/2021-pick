<template>
  <div>
    <div>
      <label for="title">바스켓 이름: </label>
      <input type="text" id="title" v-model="info.title">
    </div>
    <div>
      <label for="explanation">바스켓 설명: </label>
      <input type="text" id="explanation" v-model="info.explanation">
    </div>
    <div>
      <label for="basket_tags_names">바스켓 태그: </label>
      <b-form-tags input-id="basket_tags_names" v-model="info.basket_tags_names"></b-form-tags>
    </div>
    <div>
      <b-form-group label="public" v-slot="{ ariaDescribedby }">
        <b-form-radio v-model="info.public" :aria-describedby="ariaDescribedby" name="public" value="True">공개</b-form-radio>
        <b-form-radio v-model="info.public" :aria-describedby="ariaDescribedby" name="public" value="False">비공개</b-form-radio>
      </b-form-group>
    </div>
    <!-- public 비공개 선택 시 친구 선택 창 나타내기 -->
    <div>{{ participants_ids }}</div>
    <div>
    <b-button v-b-toggle.collapse-1 variant="primary">친구 초대</b-button>
    <b-collapse id="collapse-1" class="mt-2">
      <b-card>
        <p class="card-text">친구선택창</p>
        <relationship-list></relationship-list>
      </b-card>
    </b-collapse>
    </div>
    <!-- 영화 선택 -->
    <div>
      <p>총 {{ info.movies_ids.length }}개의 영화를 p!ck했습니다.</p>
      <div>
        <label for="tags-pills">선택 영화 목록</label>
        <b-form-tags
          input-id="tags-pills"
          v-model="info.movies_ids"
          tag-variant="primary"
          tag-pills
          size="lg"
          separator=" "
          disabled="true"
        ></b-form-tags>
      </div>
      <movie-search-bar></movie-search-bar>
      <b-button variant="outline-primary" @click="addToData">추가하기</b-button>
      <movie-search-result></movie-search-result>
    </div>
  </div>
</template>

<script>
import RelationshipList from '@/components/Account/RelationshipList'
import MovieSearchBar from '@/components/Movie/MovieSearchBar'
import MovieSearchResult from '@/components/Movie/MovieSearchResult'

import { mapState, mapActions } from 'vuex'


export default {
  name: 'BasketForm',
  data: function () {
    return {
      info: {
        title: '',
        explanation: '',
        basket_tags_names: [],
        public: false,
        participants_ids: [],
        image: '',
        movies_ids: [],
      }
    }
  },
  components: {
    RelationshipList,
    MovieSearchBar,
    MovieSearchResult,
  },
  methods: {
    addToData: function () {
      for (let pickedMovie of this.pickedMovies) {
        this.info.movies_ids.push(pickedMovie.id)
      }
      this.resetMovies('picked')
    },
    ...mapActions('movieStore', [
      'resetMovies',
    ])
  },
  computed: {
    ...mapState('movieStore', {
      pickedMovies: state => state.pickedMovies,
    })
  }
}
</script>

<style>

</style>