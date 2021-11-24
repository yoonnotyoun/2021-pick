<template>
  <div>
    <div class="container">
      <h1>Login</h1>
      <div class="input-signup">
        <label for="username" class="d-flex">아이디</label>
        <b-form-input
          id="username"
          type="text"
          v-model="credentials.username"
          placeholder="아이디를 입력해주세요."></b-form-input>
      </div>
      <div class="input-signup">
        <label for="password" class="d-flex">비밀번호</label>
        <b-form-input
          id="password"
          type="password"
          v-model="credentials.password"
          placeholder="비밀번호를 입력해주세요."
          @keypress.enter="login(credentials)">
          </b-form-input>
      </div>
      <b-button class="action-button" @click="login(credentials)">로그인</b-button>
    </div>
    <b-button class="action-button-gray mt-2 mb-4">
      <router-link class="text-decoration-none" style="color:#c4c4c4;" :to="{ name: 'Signup' }">회원가입</router-link>
    </b-button>
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
    ...mapActions([
      'login',
    ]),
  },
}
</script>