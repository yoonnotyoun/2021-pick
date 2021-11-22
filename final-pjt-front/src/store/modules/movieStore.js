import SERVER from '@/api/drf.js'
import router from '@/router/index.js'
import axios from 'axios'
import _ from 'lodash'


const movieStore = {
  state: {
    authToken: localStorage.getItem('jwt'),
    movies: [],
    selectedMovieDetail: '',
    userInput: '',
  },
  getters: {
    isLoggedIn: function (state) {
      console.log(state.authToken ? true: false)
      return state.authToken ? true: false
    },
    config: function (state) {
      console.log(state.authToken ? true: false)
      return {
        Authorization: `JWT ${state.authToken}`
      }
    },
  },
  mutations: {
    SET_MOVIE_LIST: function (state, movies) {
      state.movies = movies
    },
    SET_INPUT_VALUE: function (state, inputData) {
      state.userInput = inputData
    },
    SET_MOVIE_DETAIL: function (state, MovieDetail) {
      state.selectedMovieDetail = MovieDetail
    },
  },
  actions: {
    getMovieSearchResult: function ({ commit, state, getters }, event) {
      commit('SET_INPUT_VALUE', event.target.value)
      const headers = getters.config
      const query = state.userInput
      axios({
        method: 'get',
        url: `${SERVER.URL}/api/v1/movies/search/${query}/`,
        headers,
      })
      .then((res) => {
        commit('SET_MOVIE_LIST', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getMovieListRecommendation: function ({ commit, getters }) {
      const headers = getters.config
      const recommend_method = _.sample(['myinfo', 'genre', 'baskets', 'friends']) // 여기서 랜덤으로 골라서 넘겨주도록
      axios({
        method: 'get',
        url: `${SERVER.URL}/api/v1/movies/recommend/${recommend_method}`,
        headers,
      })
      .then((res) => {
        commit('SET_MOVIE_LIST', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getMovieDetail: function ({ commit, getters }, selectedMovie) {
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
  },
}
export default movieStore