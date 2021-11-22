const basketStore = {
  namespaced: true,
  state: {
    authToken: localStorage.getItem('jwt'),
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
  },
  actions: {
  },
}
export default basketStore