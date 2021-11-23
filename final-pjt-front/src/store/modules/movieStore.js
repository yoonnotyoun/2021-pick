import SERVER from '@/api/drf.js'
import router from '@/router/index.js'
import axios from 'axios'
// import _ from 'lodash'


const movieStore = {
  namespaced: true,
  state: () => ({
    authToken: localStorage.getItem('jwt'),
    searchedMovies: [],
    recommendedMovies: [],
    selectedMovieDetail: '',
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
    SET_MOVIE_DETAIL: function (state, MovieDetail) {
      state.selectedMovieDetail = MovieDetail
    },
  },
  actions: {
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
    getMovieRecommendation: function ({ commit, getters }) {
      const headers = getters.config
      // const recommend_method = _.sample(['myinfo', 'genre', 'baskets', 'friends'])
      const recommend_method = 'genre'
      // 리스트 하나 만들어서 중복방지 체크용으로 쓰기 (for문)
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
  },
}
export default movieStore