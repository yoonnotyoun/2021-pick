<template>
  <div>
    <h1>Login</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input 
        type="password" 
        id="password" 
        v-model="credentials.password"
        @keypress.enter="startLogin"
      >
    </div>
    <button @click="startLogin">로그인</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    ...mapActions('accountStore', [
      'login',
    ]),
    ...mapActions('movieStore', [
      'getMovieUserId',
    ]),
    startLogin: function() {
      this.login(this.credentials)
      this.getMovieUserId()
    }
  }
}
</script>