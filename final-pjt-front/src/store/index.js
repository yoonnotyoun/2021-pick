import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"
import axios from 'axios'
import SERVER from '@/api/drf.js'


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
    userId: '',
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
    // 프로필
    SET_USER_ID: function (state, userId) {
      state.userId = userId
      console.log(state.userId)
    },
  },
  actions: {
    // 프로필
    getUserId: function ({ commit, getters }) {
      axios({
        url: SERVER.URL + '/api/v1/accounts/login/',
        method: 'get',
        headers: getters.config
      })
      .then((res) => {
        commit('SET_USER_ID', res.data.userId)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  plugins: [createPersistedState()]
})

export default store