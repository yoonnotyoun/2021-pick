const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  URL: SERVER_URL,
  ROUTES: {
    signup: '/api/v1/accounts/signup/',
    login: '/api/v1/accounts/api-token-auth/',
    // createTodo: '/todos/',
    // todoList: '/todos/',
    movies: '/api/v1/movies/db/movies/', //created 시점에 실행?
  }
}