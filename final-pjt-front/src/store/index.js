import Vue from 'vue'
import Vuex from 'vuex'

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
})

export default store