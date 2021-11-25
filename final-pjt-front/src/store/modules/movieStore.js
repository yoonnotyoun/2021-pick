import SERVER from '@/api/drf.js'
// import router from '@/router/index.js'
import axios from 'axios'
import _ from 'lodash'


const movieStore = {
  namespaced: true,
  state: () => ({
    // userId: '',
    authToken: localStorage.getItem('jwt'),
    pickedMovie: '',
    pickedMovieList: [],
    pickedMovieIdList: [],
    pickedMovieTitleList: [],
    // 리스트 검색, 추천
    searchedMovies: [],
    query: '',
    recommendedMovies: [],
    recommendedMethod: [],
    recommendedTail: [],
    // 디테일, 좋아요
    selectedMovieDetail: '',
    movieBaskets: '',
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
        state.pickedMovieList = []
      } if (type === 'pickedId') {
        state.pickedMovieIdList = []
      } if (type === 'pickedTitle') {
        state.pickedMovieTitleList = []
      } if (type === 'method') {
        state.recommendedMethod = []
      } if (type === 'tail') {
        state.recommendedTail = []
      }
      state.query = ''
    },
    // 리스트 검색, 추천
    SET_SEARCHED_MOVIE_LIST: function (state, movies) {
      state.searchedMovies = movies
      state.recommendedMovies = []
    },
    SET_SEARCHED_QUERY: function (state, query) {
      state.query = query
    },
    SET_RECOMMENDED_MOVIE_LIST: function (state, recommendedData) {
      if (recommendedData.length === 7) {
        state.recommendedMovies.push({
          recommended_name: recommendedData.pop(6).recommended_name,
          movies: recommendedData
        })
      } else {
        state.recommendedMovies.push({
          recommended_name: '당신 또래의 같은 성별',
          movies: recommendedData
        })
      }
      state.searchedMovies = []
      // console.log(state.recommendedMovies)
    },
    SET_RECOMMENDED_METHOD_TAIL: function (state, methodTail) {
      state.recommendedMethod.push(methodTail.method)
      state.recommendedTail.push(methodTail.tail)
    },
    ADD_TO_PICK: function (state) {
      const movie = state.selectedMovieDetail
      // let checkDuplication = state.pickedMovieList.findIndex(item => item.id === movie.id)
      let checkDuplication = state.pickedMovieIdList.findIndex(item => item === movie.id)
      // if (!(movie.id in state.pickedMovies)) {
      console.log(checkDuplication)
      if (checkDuplication === -1) {
        // console.log(movie)
        state.pickedMovie = movie
        state.pickedMovieList.push(movie)
        state.pickedMovieIdList.push(movie.id)
        state.pickedMovieTitleList.push(movie.title)
        // console.log(state.pickedMovies)
      } else {
        state.pickedMovieList.pop(movie)
        state.pickedMovieIdList.pop(movie.id)
        state.pickedMovieTitleList.pop(movie.title)
      }
      state.selectedMovieDetail = ''
    },
    // 디테일, 좋아요
    SET_MOVIE_DETAIL: function (state, MovieDetail) {
      state.selectedMovieDetail = MovieDetail
    },
    // 유저, 영화별 바스켓
    GET_MOVIE_BASKETS: function (state, movieBaskets) {
      state.movieBaskets = movieBaskets
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
        commit('SET_SEARCHED_QUERY', query)
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
        'myinfo': '사용자들이 p!ck한 영화',
        'genre': '장르의 영화',
        'baskets': '바스켓에 들어있는 영화',
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
    getMovieDetail: function ({ commit, getters, dispatch }, selectedMovie) {
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
        dispatch('addMovieInfo', movie_pk)
        console.log(location)
        if (location === 'basketform') {
          commit('ADD_TO_PICK')
        }
      })
      .catch((err) => {
        console.log(err)
      })
    },
    addMovieInfo: function ({ commit, getters }, movieId) {
      const headers = getters.config
      axios({
        url: `${SERVER.URL}/api/v1/movies/add_movie_info/${movieId}`,
        method: 'get',
        headers,
      })
      .then((res) => {
        commit('GET_MOVIE_BASKETS', res.data)
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
    // getMovieBaskets: function ({ commit, getters }, movieId) {
    //   const headers = getters.config
    //   axios({
    //     url: `${SERVER.URL}/api/v1/baskets/movie/${movieId}/`,
    //     method: 'get',
    //     headers,
    //   })
    //   .then((res) => {
    //     commit('GET_MOVIE_BASKETS', res.data)
    //   })
    //   .catch((err) => {
    //     console.log(err)
    //   })
    // },
  },
}
export default movieStore