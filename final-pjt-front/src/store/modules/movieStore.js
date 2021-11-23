import SERVER from '@/api/drf.js'
import router from '@/router/index.js'
import axios from 'axios'
// import _ from 'lodash'


const movieStore = {
  namespaced: true,
  state: () => ({
    // 로그인
    authToken: localStorage.getItem('jwt'),
    // 검색
    searchedMovies: [],
    // 추천
    recommendedMovies: [],
    recommendedNameList: [],
    // 디테일
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
      const recommendedName = recommendedData.pop(6).recommended_name
      state.recommendedNameList.push(recommendedName)
      state.recommendedMovies.push({
        recommendedName: recommendedName,
        movies: recommendedData
      })
      // state.recommendedMovies = recommendedMovies
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

      axios({
        method: 'get',
        url: `${SERVER.URL}/api/v1/movies/recommend/${recommend_method}`,
        headers,
      })
      .then((res) => {
        // console.log(recommend_method)
        // const recommended_name = res.data.pop(6).recommended_name
        // console.log(res.data[6].recommended_name)
        if (!(res.data[6].recommended_name in state.recommendedNameList)) {
          commit('SET_RECOMMENDED_MOVIE_LIST', res.data)
        }
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
}
export default movieStore