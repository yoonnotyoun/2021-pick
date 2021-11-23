import SERVER from '@/api/drf.js'
import router from '@/router/index.js'
import axios from 'axios'
// import _ from 'lodash'


const basketStore = {
  namespaced: true,
  state: () => ({
    authToken: localStorage.getItem('jwt'),
    searchedBaskets: [],
    recommendedBaskets: [],
    selectedBasketDetail: '',
    // COMMENT
    comments: [],
    noSpoilerComments: [],
    showSpoilerOption: false,
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
    SET_SEARCHED_BASKET_LIST: function (state, baskets) {
      state.searchedBaskets = baskets
      state.recommendedBaskets = []
    },
    SET_RECOMMENDED_BASKET_LIST: function (state, recommendedData) {
      console.log(recommendedData)
      state.recommendedBaskets.push({
        recommended_name: recommendedData.pop(3).recommended_name,
        baskets: recommendedData
      })
      state.searchedBaskets = []
    },
    SET_BASKET_DETAIL: function (state, basketDetail) {
      state.selectedBasketDetail = basketDetail
    },
    // COMMENT
    SET_COMMENTS: function (state, comments) {
      state.comments = comments
      const noSpoilerCommentList = []
      for (let comment of comments) {
        if (!comment.spoiler) {
          noSpoilerCommentList.push(comment)
        }
      }
      state.noSpoilerComments = noSpoilerCommentList
    },
    SET_SPOILER_FILTER: function (state, showSpoiler) {
      state.showSpoilerOption = showSpoiler
    },
  },
  actions: {
    getBasketSearchResult: function ({ commit, getters }, event) {
      const headers = getters.config
      const query = event.target.value
      axios({
        method: 'get',
        url: `${SERVER.URL}/api/v1/baskets/search/${query}/`,
        headers,
      })
      .then((res) => {
        commit('SET_SEARCHED_BASKET_LIST', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getBasketDetail: function ({ commit, getters }, selectedBasket) {
      const headers = getters.config
      const basket_pk = selectedBasket.id
      axios({
        method: 'get',
        url: `${SERVER.URL}/api/v1/baskets/${basket_pk}/`,
        headers,
      })
      .then((res) => {
        commit('SET_BASKET_DETAIL', res.data)
        router.push({ name: 'BasketDetail' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getBasketRecommendation: function ({ commit, getters }) {
      const headers = getters.config
      // const recommend_method = _.sample(['myinfo', 'movies', 'tags', 'friends'])
      const recommend_method = 'movies'
      // 중복방지 처리 하기
      axios({
        method: 'get',
        url: `${SERVER.URL}/api/v1/baskets/recommend/${recommend_method}`,
        headers,
      })
      .then((res) => {
        console.log(recommend_method)
        commit('SET_RECOMMENDED_BASKET_LIST', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // COMMENT
    getCommentList: function ({ state, commit, getters }) {
      const headers = getters.config
      const basket_id = state.selectedBasketDetail.id
      // console.log(basket_id)
      axios({
        url: `${SERVER.URL}/api/v1/baskets/${basket_id}/comment/`,
        method: 'get',
        headers,
      })
      .then((res) => {
        commit('SET_COMMENTS', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    createComment: function ({ state, getters, dispatch }, { content, spoiler }) {
      const headers = getters.config
      const basket_id = state.selectedBasketDetail.id
      const commentItem = {
        content,
        spoiler,
      }

      if (commentItem.content) {
        axios({
          url: `${SERVER.URL}/api/v1/baskets/${basket_id}/comment/`,
          method: 'post',
          data: commentItem,
          headers,
        })
        .then(() => {
          dispatch('getCommentList')
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
    deleteComment: function ({ getters, dispatch }, comment) {
      const headers = getters.config
      const comment_pk = comment.id
      axios({
        url: `${SERVER.URL}/api/v1/baskets/comment/${comment_pk}/`,
        method: 'delete',
        headers,
      })
      .then(() => {
        dispatch('getCommentList')
      })
      .catch((err) => {
        console.log(err)
      })
    },
    setSpoilerFilter: function ({ commit }, showSpoiler) {
      commit('SET_SPOILER_FILTER', showSpoiler)
    },
  },
}
export default basketStore