import SERVER from '@/api/drf.js'
import router from '@/router/index.js'
import axios from 'axios'

const accountStore = {
  namespaced: true,
  state: {
    authToken: localStorage.getItem('jwt'),
    userId: '',
    profileInfo: '',
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
    SET_TOKEN: function (state, token) {
      state.authToken = token
      localStorage.setItem('jwt', token)
    },
    REMOVE_TOKEN: function (state) {
      localStorage.removeItem('jwt')
      state.authToken = ''
    },
    SET_USER_ID: function (state, userId) {
      state.userId = userId
      console.log(state.userId)
    },
    GET_PROFILE: function (state, userData) {
      state.profileInfo = userData
    },
  },
  actions: {
    login: function ({ commit, dispatch }, credentials) {
      axios({
        url: SERVER.URL + SERVER.ROUTES.login,
        method: 'post',
        data: credentials,
      })
      .then((res) => {
        commit('SET_TOKEN', res.data.token)
        router.push({ name: 'Main' })
        dispatch('getUserId')
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getUserId: function ({ commit, getters }) {
      axios({
        url: SERVER.URL + '/api/v1/accounts/login/',
        method: 'get',
        headers: getters.config
      })
      .then((res) => {
        console.log(res, '유저아이디')
        commit('SET_USER_ID', res.data.userId)
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
    getProfile: function ({ state, commit, getters }) {
      axios({
        method: 'get',
        url: `${SERVER.URL}/api/v1/accounts/profile/${state.userId}/`,
        headers: getters.config
      })
      .then((res) => {
        console.log(res.data)
        const userData = res.data
        commit('GET_PROFILE', userData)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  }
}
export default accountStore