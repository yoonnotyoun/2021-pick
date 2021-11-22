import Vue from 'vue'
import Vuex from 'vuex'
import SERVER from '@/api/drf.js'
import router from '@/router/index.js'
import axios from 'axios'
import _ from 'lodash'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authToken: localStorage.getItem('jwt'),
    userInfo: {},
    movies: [],
    baskets: [],
    tastingrooms: [],
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
    GET_PROFILE: function (state, userData) {
      state.userInfo = userData
      // console.log(state.userInfo)
    },
    SET_MOVIELIST: function (state, movies) {
      state.movies = movies
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
    getProfile: function ({ commit, getters }) {
      axios({
        method: 'get',
        url: `${SERVER.URL}/api/v1/accounts/profile/`,
        headers: getters.config
      })
      .then((res) => {
        const userData = res.data
        commit('GET_PROFILE', userData)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getMovieListRecommendation: function ({ commit, getters }) {
      const headers = getters.config
      recommend_method = _.sample['myinfo', 'genre', 'baskets', 'friends'] // 여기서 랜덤으로 골라서 넘겨주도록
      axios({
        method: 'get',
        url: `${SERVER.URL}/api/v1/movies/tmdb/movies/${recommend_method}`,
        headers,
      })
      .then((res) => {
        commit('SET_MOVIELIST', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  modules: {
  }
})
