import SERVER from '@/api/drf.js'
import router from '@/router/index.js'
import axios from 'axios'
// import _ from 'lodash'


const movieStore = {
  namespaced: true,
  state: () => ({
    userId: '',
    authToken: localStorage.getItem('jwt'),
    // 리스트 검색, 추천
    searchedMovies: [],
    recommendedMovies: [],
    // 디테일, 좋아요
    selectedMovieDetail: '',
    likeButtonName: '',
    likeCnt: '',
  }),
  getters: {
    isLoggedIn: function (state) {
      return state.authToken ? true: false
    },
    config: function (state) {
      return {
        Authorization: `JWT ${state.authToken}`
      }
    },
  },
  mutations: {
    // 프로필
    SET_MOVIE_USER_ID: function (state, userId) {
      state.userId = userId
    },
    // 초기화
    RESET_MOVIES: function (state, type) {
      if (type === 'recommended') {
        state.recommendedMovies = []
      } if (type === 'searched') {
        state.searchedMovies = []
      }
    },
    // 리스트 검색, 추천
    SET_SEARCHED_MOVIE_LIST: function (state, movies) {
      state.searchedMovies = movies
      state.recommendedMovies = []
    },
    SET_RECOMMENDED_MOVIE_LIST: function (state, recommendedData) {
      state.recommendedMovies.push({
        recommended_name: recommendedData.pop(6).recommended_name,
        movies: recommendedData
      })
      state.searchedMovies = []
      // console.log(state.recommendedMovies)
    },
    // 디테일, 좋아요
    SET_MOVIE_DETAIL: function (state, MovieDetail) {
      state.selectedMovieDetail = MovieDetail
    },
    GET_LIKE_INFO: function (state, likeButtonName) {
      state.likeButtonName = likeButtonName
    },
    GET_LIKE_CNT: function (state, likeCnt) {
      state.likeCnt = likeCnt
    },
  },
  actions: {
    // 프로필
    getMovieUserId: function ({ commit, getters }) {
      axios({
        url: SERVER.URL + '/api/v1/accounts/login/',
        method: 'get',
        headers: getters.config
      })
      .then((res) => {
        commit('SET_MOVIE_USER_ID', res.data.userId)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // 초기화
    resetMovies: function ({ commit }, type) {
      commit('RESET_MOVIES', type)
    },
    // 리스트 검색, 추천
    getMovieSearchResult: function ({ commit, getters }, event) {
      const headers = getters.config
      const query = event.target.value
      axios({
        method: 'get',
        url: `${SERVER.URL}/api/v1/movies/search/${query}/`,
        headers,
      })
      .then((res) => {
        commit('SET_SEARCHED_MOVIE_LIST', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getMovieRecommendation: function ({ commit, getters }) {
      const headers = getters.config
      // const recommend_method = _.sample(['myinfo', 'genre', 'baskets', 'friends'])
      const recommend_method = 'genre'
      // 중복방지 처리 하기
      axios({
        method: 'get',
        url: `${SERVER.URL}/api/v1/movies/recommend/${recommend_method}`,
        headers,
      })
      .then((res) => {
        console.log(recommend_method)
        commit('SET_RECOMMENDED_MOVIE_LIST', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // 디테일, 좋아요
    getMovieDetail: function ({ commit, getters }, selectedMovie) {
      console.log(selectedMovie.id)
      const headers = getters.config
      const movie_pk = selectedMovie.id
      axios({
        method: 'get',
        url: `${SERVER.URL}/api/v1/movies/${movie_pk}/`,
        headers,
      })
      .then((res) => {
        commit('SET_MOVIE_DETAIL', res.data)
        router.push({ name: 'MovieDetail' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getLikeButtonName: function ({ state, commit }) {
      if (this.userId in state.selectedMovieDetail.like_users) {
        commit('GET_LIKE_INFO', 'unlike')
      } else {
        commit('GET_LIKE_INFO', 'like')
      }
    },
    likeUnlike: function ({ state, commit, dispatch, getters }, movieId) {
      axios({
        method: 'post',
        url: `${SERVER.URL}/api/v1/movies/${movieId}/like/`,
        headers: getters.config
      })
      .then((res) => {
        console.log(res)
        dispatch('getMovieDetail', state.selectedMovieDetail)
        if (res.data.liked) {
          commit('GET_LIKE_INFO', 'unlike')
        } else {
          commit('GET_LIKE_INFO', 'like')
        }
        commit('GET_LIKE_CNT', res.data.cnt_likes)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // unlike: function ({ state, commit, dispatch, getters }, movieId) {
    //   axios({
    //     method: 'delete',
    //     url: `${SERVER.URL}/api/v1/accounts/relationship/star/${movieId}/`,
    //     headers: getters.config
    //   })
    //   .then(() => {
    //     dispatch('getMovieDetail', state.selectedMovie)
    //     commit('GET_LIKE_INFO', 'like')
    //   })
    //   .catch((err) => {
    //     console.log(err)
    //   })
    // },
  },
}
export default movieStore