import Vue from 'vue'
import Vuex from 'vuex'
import SERVER from '@/api/drf.js'
import router from '@/router/index.js'
import axios from 'axios'

Vue.use(Vuex)

import accountStore from '@/store/modules/accountStore.js'
import basketStore from '@/store/modules/basketStore.js'
import movieStore from '@/store/modules/movieStore.js'

const store = new Vuex.Store({
  modules: {
    accountStore: accountStore,
    basketStore: basketStore,
    movieStore: movieStore,
  },
  state: {
    authToken: localStorage.getItem('jwt'),
  },
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
    SET_TOKEN: function (state, token) {
      state.authToken = token
      localStorage.setItem('jwt', token)
    },
    REMOVE_TOKEN: function (state) {
      localStorage.removeItem('jwt')
      state.authToken = ''
    },
  },
  actions: {
    login: function ({ commit }, credentials) {
      axios({
        url: SERVER.URL + SERVER.ROUTES.login,
        method: 'post',
        data: credentials,
      })
      .then((res) => {
        commit('SET_TOKEN', res.data.token)
        router.push({ name: 'Main' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    logout: function ({ commit }) {
      commit('REMOVE_TOKEN')
      router.push({ name: 'Login' })
    },
    signup: function (context, credentials) {
      axios({
        url: SERVER.URL + SERVER.ROUTES.signup,
        method: 'post',
        data: credentials,
      })
      .then(() => {
        console.log(SERVER.URL + SERVER.ROUTES.signup)
        router.push({ name: 'Login' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
  }
})

export default store

// import SERVER from '@/api/drf.js'
// import router from '@/router/index.js'
// import axios from 'axios'
// import _ from 'lodash'


// export default new Vuex.Store({
//   state: {
//     authToken: localStorage.getItem('jwt'),
//     userInfo: {},
//     movies: [],
//     selectedMovieDetail: '',
//     baskets: [],
//     userInput: '',
//     // isModalViewed:false,
//   },
//   getters: {
//     isLoggedIn: function (state) {
//       return state.authToken ? true: false
//     },
//     config: function (state) {
//       return {
//         Authorization: `JWT ${state.authToken}`
//       }
//     },
//   },
//   mutations: {
//     SET_TOKEN: function (state, token) {
//       state.authToken = token
//       localStorage.setItem('jwt', token)
//     },
//     REMOVE_TOKEN: function (state) {
//       localStorage.removeItem('jwt')
//       state.authToken = ''
//     },
//     GET_PROFILE: function (state, userData) {
//       state.userInfo = userData
//       // console.log(state.userInfo)
//     },
//     SET_MOVIELIST: function (state, movies) {
//       state.movies = movies
//     },
//     SET_INPUT_VALUE: function (state, inputData) {
//       state.userInput = inputData
//     },
//     SET_MOVIE_DETAIL: function (state, MovieDetail) {
//       state.selectedMovieDetail = MovieDetail
//     },
//   },
//   actions: {
//     login: function ({ commit }, credentials) {
//       axios({
//         url: SERVER.URL + SERVER.ROUTES.login,
//         method: 'post',
//         data: credentials,
//       })
//       .then((res) => {
//         commit('SET_TOKEN', res.data.token)
//         router.push({ name: 'Main' })
//       })
//       .catch((err) => {
//         console.log(err)
//       })
//     },
//     logout: function ({ commit }) {
//       commit('REMOVE_TOKEN')
//       router.push({ name: 'Login' })
//     },
//     signup: function (context, credentials) {
//       axios({
//         url: SERVER.URL + SERVER.ROUTES.signup,
//         method: 'post',
//         data: credentials,
//       })
//       .then(() => {
//         console.log(SERVER.URL + SERVER.ROUTES.signup)
//         router.push({ name: 'Login' })
//       })
//       .catch((err) => {
//         console.log(err)
//       })
//     },
//     getProfile: function ({ commit, getters }) {
//       axios({
//         method: 'get',
//         url: `${SERVER.URL}/api/v1/accounts/profile/`,
//         headers: getters.config
//       })
//       .then((res) => {
//         const userData = res.data
//         commit('GET_PROFILE', userData)
//       })
//       .catch((err) => {
//         console.log(err)
//       })
//     },
//     // getMovieData: function () { // 생각해보니까 최종 db에 미리 다 받아둘 거면 이 함수 필요없을지도?
//     //   axios({
//     //     method: 'post',
//     //     url: SERVER.URL + SERVER.ROUTES.getMovieData,
//     //   })
//     //   .then((res) => {
//     //     console.log(res)
//     //   })
//     //   .catch((err) => {
//     //     console.log(err)
//     //   })
//     // },
//     getMovieSearchResult: function ({ commit, state, getters }, event) {
//       commit('SET_INPUT_VALUE', event.target.value)
//       const headers = getters.config
//       const query = state.userInput
//       axios({
//         method: 'get',
//         url: `${SERVER.URL}/api/v1/movies/search/${query}/`,
//         headers,
//       })
//       .then((res) => {
//         commit('SET_MOVIELIST', res.data)
//       })
//       .catch((err) => {
//         console.log(err)
//       })
//     },
//     getMovieListRecommendation: function ({ commit, getters }) {
//       const headers = getters.config
//       const recommend_method = _.sample(['myinfo', 'genre', 'baskets', 'friends']) // 여기서 랜덤으로 골라서 넘겨주도록
//       axios({
//         method: 'get',
//         url: `${SERVER.URL}/api/v1/movies/recommend/${recommend_method}`,
//         headers,
//       })
//       .then((res) => {
//         commit('SET_MOVIELIST', res.data)
//       })
//       .catch((err) => {
//         console.log(err)
//       })
//     },
//     getMovieDetail: function ({ commit, getters }, selectedMovie) {
//       const headers = getters.config
//       const movie_pk = selectedMovie.id
//       axios({
//         method: 'get',
//         url: `${SERVER.URL}/api/v1/movies/${movie_pk}/`,
//         headers,
//       })
//       .then((res) => {
//         commit('SET_MOVIE_DETAIL', res.data)
//         router.push({ name: 'MovieDetail' })
//       })
//       .catch((err) => {
//         console.log(err)
//       })
//     },
//   },
//   modules: {
//   }
// })
