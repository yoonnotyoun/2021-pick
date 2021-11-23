import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"
// import axios from 'axios'
// import SERVER from '@/api/drf.js'


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
  },
  actions: {
  },
  plugins: [createPersistedState()]
})

export default store