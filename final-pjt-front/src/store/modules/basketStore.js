import SERVER from '@/api/drf.js'
import router from '@/router/index.js'
import axios from 'axios'
// import _ from 'lodash'


const basketStore = {
  namespaced: true,
  state: () => ({
    userId: '',
    authToken: localStorage.getItem('jwt'),
    searchedBaskets: [],
    recommendedBaskets: [],
    // 디테일
    selectedBasketDetail: '',
    // 좋아요
    likeButtonName: '',
    likeCnt: '',
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
    // 프로필
    SET_USER_ID: function (state, userId) {
      console.log('basket userId', userId)
      state.userId = userId
    },
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
    // 디테일
    SET_BASKET_DETAIL: function (state, basketDetail) {
      state.selectedBasketDetail = basketDetail
    },
    // 좋아요
    GET_LIKE_INFO: function (state, likeButtonName) {
      state.likeButtonName = likeButtonName
    },
    GET_LIKE_CNT: function (state, likeCnt) {
      state.likeCnt = likeCnt
    },
    RESET_BASKETS: function (state, type) {
      if (type === 'recommended') {
        state.recommendedBaskets = []
      } if (type === 'searched') {
        state.searchedBaskets = []
      }
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
    // 프로필
    getBasketUserId: function ({ commit }, userId) {
      commit('SET_USER_ID', userId)
    },
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
    // 디테일
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
        commit('GET_LIKE_CNT', res.data.like_users.length)
        router.push({ name: 'BasketDetail' })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // 좋아요
    getLikeButtonName: function ({ state, commit }) {
      if (this.userId in state.selectedBasketDetail.like_users) {
        commit('GET_LIKE_INFO', 'unlike')
      } else {
        commit('GET_LIKE_INFO', 'like')
      }
    },
    likeUnlike: function ({ state, commit, dispatch, getters }, basketId) {
      axios({
        method: 'post',
        url: `${SERVER.URL}/api/v1/baskets/${basketId}/like/`,
        headers: getters.config
      })
      .then((res) => {
        console.log('likeUnlike', res)
        dispatch('getBasketDetail', state.selectedBasketDetail)
        if (res.data.liked) {
          commit('GET_LIKE_INFO', 'unlike')
        } else {
          commit('GET_LIKE_INFO', 'like')
        }
        commit('GET_LIKE_CNT', res.data.cnt_likes)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // 초기화
    resetBaskets: function ({ commit }, type) {
      commit('RESET_BASKETS', type)
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