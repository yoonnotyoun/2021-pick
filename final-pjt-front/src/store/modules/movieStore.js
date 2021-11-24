import SERVER from '@/api/drf.js'
// import router from '@/router/index.js'
import axios from 'axios'
import _ from 'lodash'


const movieStore = {
  namespaced: true,
  state: () => ({
    // userId: '',
    authToken: localStorage.getItem('jwt'),
    pickedMovies: [],
    // 리스트 검색, 추천
    searchedMovies: [],
    recommendedMovies: [],
    recommendedMethod: [],
    recommendedTail: [],
    // 디테일, 좋아요
    selectedMovieDetail: '',
    likeButtonName: '',
    likeCnt: '',
  }),
  getters: {
    isLoggedIn: function (state, getters, rootState, rootGetters) {
      return rootGetters.isLoggedIn
    },
    config: function (state, getters, rootState, rootGetters) {
      return rootGetters.config
    },
  },
  mutations: {
    // 초기화
    RESET_MOVIES: function (state, type) {
      if (type === 'recommended') {
        state.recommendedMovies = []
      } if (type === 'searched') {
        state.searchedMovies = []
      } if (type === 'picked') {
        state.pickedMovies = []
      } if (type === 'method') {
        state.recommendedMethod = []
      } if (type === 'tail') {
        state.recommendedTail = []
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
    SET_RECOMMENDED_METHOD_TAIL: function (state, methodTail) {
      state.recommendedMethod.push(methodTail.method)
      state.recommendedTail.push(methodTail.tail)
      console.log(state.recommendedMethod)
      console.log(state.recommendedTail)
    },
    ADD_TO_PICK: function (state) {
      const movie = state.selectedMovieDetail
      let checkDuplication = state.pickedMovies.findIndex(item => item.id === movie.id)
      // if (!(movie.id in state.pickedMovies)) {
      console.log(checkDuplication)
      if (checkDuplication === -1) {
        // console.log(movie)
        state.pickedMovies.push(movie)
        // console.log(state.pickedMovies)
      }
      state.selectedMovieDetail = ''
      // state.pickedMovies = []
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
      const recommend_method = _.sample(['myinfo', 'genre', 'baskets', 'friends'])
      // const recommend_method = 'genre'
      const recommend_tail = {
        'myinfo': '당신과 연령, 성별이 비슷한 사용자들이 p!ck한 영화',
        'genre': '장르의 영화',
        'baskets': '바스켓을 포함해 당신이 p!ck한 바스켓의 영화',
        'friends': '님이 p!ck한 바스켓',
      }
      const methodTail = {
        method: recommend_method,
        tail: recommend_tail[recommend_method],
      }
      // 중복방지 처리 하기
      axios({
        method: 'get',
        url: `${SERVER.URL}/api/v1/movies/recommend/${recommend_method}`,
        headers,
      })
      .then((res) => {
        console.log(recommend_method)
        commit('SET_RECOMMENDED_MOVIE_LIST', res.data)
        commit('SET_RECOMMENDED_METHOD_TAIL', methodTail)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // 디테일, 좋아요
    getMovieDetail: function ({ commit, getters }, selectedMovie) {
      // console.log(document.location.href.split("0/"))
      const headers = getters.config
      const movie_pk = selectedMovie.id
      const location = document.location.href.split("0/")[1]
      axios({
        method: 'get',
        url: `${SERVER.URL}/api/v1/movies/${movie_pk}/`,
        headers,
      })
      .then((res) => {
        commit('SET_MOVIE_DETAIL', res.data)
        // if (location === 'accounts/setmovietaste') {
        //   commit('ADD_TO_PICK') // like 해버리기?
        // }
        console.log(location)
        if (location === 'basketform') {
          commit('ADD_TO_PICK') // like 해버리기?
        }
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getLikeButtonName: function ({ state, commit, rootState }) {
      let flag = false
      for (let like_user of state.selectedMovieDetail.like_users) {
        if (rootState.userId === like_user['id']) {
          commit('GET_LIKE_INFO', 'unlike')
          flag = true
        }
      }
      if (flag === false) {
        commit('GET_LIKE_INFO', 'like')
      }
    },
    // checkPickedMovies: function ({ state }, selectedMovie) {
    //   let checkDuplication = state.pickedMovies.findIndex(item => item.id === selectedMovie.id)
    //   console.log(checkDuplication)
    //   if (checkDuplication === -1) {
    //     return false
    //   } else {
    //     return true
    //   }
    // },
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
  },
}
export default movieStore