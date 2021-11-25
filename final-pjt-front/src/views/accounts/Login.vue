<template>
  <div>
    <div class="container mt-5">
      <div><br>
        <p class="d-inline-block"
        style="font-family: 'Hahmlet', serif; font-weight: 600; font-size: 1.6rem; color: #222222;"
        >로그인</p>
      </div>
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
    </div>
    <div class="">
      <b-button class="action-button-transparent mx-1">
        <router-link class="text-decoration-none" style="color:#c4c4c4;" :to="{ name: 'Signup' }">회원가입</router-link>
      </b-button>
      <b-button class="action-button mx-1" @click="login(credentials)">로그인</b-button>
    </div>
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