import SERVER from '@/api/drf.js'
import router from '@/router/index.js'
import axios from 'axios'

const accountStore = {
  namespaced: true,

  state: () => ({
    // 로그인
    authToken: localStorage.getItem('jwt'),
    // 프로필
    userId: '',
    profileInfo: '',
    tags: [],
    followButtonName: '',
    // 그룹
    groups: [],
    // relationship (그룹관리)
    relationshipList: [],
    groupFilterId: '전체',
  }),

  getters: {
    // 로그인
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
    // 로그인
    SET_TOKEN: function (state, token) {
      state.authToken = token
      localStorage.setItem('jwt', token)
    },
    REMOVE_TOKEN: function (state) {
      localStorage.removeItem('jwt')
      state.authToken = ''
    },
    // 프로필
    SET_USER_ID: function (state, userId) {
      state.userId = userId
      console.log(state.userId)
    },
    GET_PROFILE: function (state, userData) {
      state.profileInfo = userData
    },
    GET_TAGS: function (state, userData) {
      state.tags = userData.liked_baskets_tags
    },
    // 팔로우
    GET_FOLLOW_INFO: function (state, followButtonName) {
      state.followButtonName = followButtonName
    },
    // 그룹
    SET_GROUPS: function (state, groups) {
      state.groups = groups
    },
    // Relationship
    SET_RELATIONSHIP_LIST: function (state, relationshipList) {
      state.relationshipList = relationshipList
    },
    SET_GROUP_FILTER_ID: function (state, groupFilterId) {
      state.groupFilterId = groupFilterId
    },
  },

  actions: {
    // 로그인
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
    getProfile: function ({ commit, getters }, userId) {
      axios({
        method: 'get',
        url: `${SERVER.URL}/api/v1/accounts/profile/${userId}/`,
        headers: getters.config
      })
      .then((res) => {
        const userData = res.data
        commit('GET_PROFILE', userData)
      })
      .catch((err) => {
        console.log(err)
      })
      axios({
        method: 'get',
        url: `${SERVER.URL}/api/v1/accounts/liked_baskets_tags/${userId}/`,
        headers: getters.config
      })
      .then((res) => {
        const userData = res.data
        commit('GET_TAGS', userData)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    //팔로우
    getFollowButtonName: function ({ commit }, profileInfo) {
      if (this.userId in profileInfo.fans) {
        commit('GET_FOLLOW_INFO', '언팔로우')
      } else {
        commit('GET_FOLLOW_INFO', '팔로우')
      }
    },
    follow: function ({ commit, dispatch, getters }, starId) {
      axios({
        method: 'post',
        url: `${SERVER.URL}/api/v1/accounts/relationship/star/${starId}/`,
        headers: getters.config
      })
      .then(() => {
        dispatch('getProfile', starId)
        commit('GET_FOLLOW_INFO', '언팔로우')
      })
      .catch((err) => {
        console.log(err)
      })
    },
    unfollow: function ({ commit, dispatch, getters }, starId) {
      axios({
        method: 'delete',
        url: `${SERVER.URL}/api/v1/accounts/relationship/star/${starId}/`,
        headers: getters.config
      })
      .then(() => {
        dispatch('getProfile', starId)
        commit('GET_FOLLOW_INFO', '팔로우')
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // 그룹
    getGroups: function ({ commit, getters }) {
      const headers = getters.config
      axios({
        url: `${SERVER.URL}/api/v1/accounts/group/`,
        method: 'get',
        headers,
      })
      .then((res) => {
        commit('SET_GROUPS', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    createGroup: function ({ dispatch, getters }, name) {
      const headers = getters.config

      const group = {
        name,
      }
      if (group.name) {
        axios({
          url: `${SERVER.URL}/api/v1/accounts/group/`,
          method: 'post',
          data: group,
          headers,
        })
        .then(() => {
          dispatch('getGroups')
          this.$router.push({ name: 'Group' })
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
    deleteGroup: function ({ dispatch, getters }, groupId) {
      const headers = getters.config

      axios({
        url: `${SERVER.URL}/api/v1/accounts/group/${groupId}/`,
        method: 'delete',
        headers,
      })
      .then(() => {
        dispatch('getGroups')
        dispatch('getGroupRelationshipList')
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // Relationship (그룹관리)
    getGroupRelationshipList: function ({ commit, getters }) {
      const headers = getters.config
      axios({
        url: `${SERVER.URL}/api/v1/accounts/relationship/`,
        method: 'get',
        headers,
      })
      .then((res) => {
        commit('SET_RELATIONSHIP_LIST', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    setGroupFilterId: function ({ commit }, groupFilterId) {
      commit('SET_GROUP_FILTER_ID', groupFilterId)
    },
    changeRelationshipGroup: function ({ dispatch, getters }, { selectedRelationships, selectedGroup }) {
      const headers = getters.config
      console.log(selectedGroup)
      for (let selectedRelationship of selectedRelationships) {
        axios({
          url: `${SERVER.URL}/api/v1/accounts/relationship/${selectedRelationship}/group/${selectedGroup}/`,
          method: 'put',
          headers,
        })
        .then(() => {
          dispatch('getGroupRelationshipList')
          this.$router.push({ name: 'Group' })
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
  }
}
export default accountStore