import SERVER from '@/api/drf.js'
import axios from 'axios'

const accountStore = {
  state: {
    // authToken: localStorage.getItem('jwt'),
    userInfo: {},
  },
  // getters: {
  //   isLoggedIn: function (state) {
  //     return state.authToken ? true: false
  //   },
  //   config: function (state) {
  //     return {
  //       Authorization: `JWT ${state.authToken}`
  //     }
  //   },
  // },
  mutations: {
    // SET_TOKEN: function (state, token) {
    //   state.authToken = token
    //   localStorage.setItem('jwt', token)
    // },
    // REMOVE_TOKEN: function (state) {
    //   localStorage.removeItem('jwt')
    //   state.authToken = ''
    // },
    GET_PROFILE: function (state, userData) {
      state.userInfo = userData
    },
  },
  actions: {
    // login: function ({ commit }, credentials) {
    //   axios({
    //     url: SERVER.URL + SERVER.ROUTES.login,
    //     method: 'post',
    //     data: credentials,
    //   })
    //   .then((res) => {
    //     commit('SET_TOKEN', res.data.token)
    //     router.push({ name: 'Main' })
    //   })
    //   .catch((err) => {
    //     console.log(err)
    //   })
    // },
    // logout: function ({ commit }) {
    //   commit('REMOVE_TOKEN')
    //   router.push({ name: 'Login' })
    // },
    // signup: function (context, credentials) {
    //   axios({
    //     url: SERVER.URL + SERVER.ROUTES.signup,
    //     method: 'post',
    //     data: credentials,
    //   })
    //   .then(() => {
    //     console.log(SERVER.URL + SERVER.ROUTES.signup)
    //     router.push({ name: 'Login' })
    //   })
    //   .catch((err) => {
    //     console.log(err)
    //   })
    // },
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
  },
}
export default accountStore