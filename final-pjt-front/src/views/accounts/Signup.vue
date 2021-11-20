<template>
  <div>
    <h1>Signup</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password">
    </div>
    <div>
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input 
        type="password" 
        id="passwordConfirmation" 
        v-model="credentials.passwordConfirmation"
        @keypress.enter="signup(credentials)"
      >
    </div> 
    <div>
      <label for="birthdate">생년월일: </label>
      <input type="date" id="birthdate" v-model="credentials.birthdate">
    </div>
    <div>
      <label for="gender">성별: </label>
      <div>
        <input type="radio" id="male" name="gender" value="남">
        <label for="male">남</label>
      </div>
      <div>
        <input type="radio" id="female" name="gender" value="여">
        <label for="female">여</label>
      </div>
    </div>
    <button @click="signup(credentials)">가입하기</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        passwordConfirmation: '',
        birthdate: '',
        gender: '',
      }
    }
  },
  methods: {
    ...mapActions([
      'signup',
    ])
  }
}
</script>