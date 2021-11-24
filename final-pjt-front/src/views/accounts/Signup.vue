<template>
  <div class="container">
    <h1>Signup</h1>
    <div class="input-signup">
      <label for="username">아이디</label>
      <b-form-input
        id="username"
        type="text"
        v-model="credentials.username"
        placeholder="아이디를 입력해주세요."></b-form-input>
    </div>
    <!-- <div>
      <label for="username">아이디: </label>
      <input type="text" id="username" v-model="credentials.username">
    </div> -->
    <div class="input-signup">
      <label for="password">비밀번호</label>
      <b-form-input
        id="password"
        type="password"
        v-model="credentials.password"
        placeholder="비밀번호를 입력해주세요."></b-form-input>
    </div>
    <!-- <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password">
    </div> -->
    <div class="input-signup">
      <label for="passwordConfirmation">비밀번호 확인</label>
      <b-form-input
        id="passwordConfirmation"
        type="password"
        v-model="credentials.passwordConfirmation"
        placeholder="비밀번호를 다시 입력해주세요."></b-form-input>
    </div>
    <!-- <div>
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input 
        type="password"
        id="passwordConfirmation" 
        v-model="credentials.passwordConfirmation"
        @keypress.enter="signup(credentials)"
      >
    </div> -->
    <div class="input-signup">
      <label for="nickname">닉네임</label>
      <b-form-input
        id="nickname"
        type="text"
        v-model="credentials.nickname"
        placeholder="서비스 내에서 사용할 닉네임을 입력해주세요."></b-form-input>
    </div>
    <!-- <div>
      <label for="nickname">닉네임: </label>
      <input type="text" id="nickname" v-model="credentials.nickname">
    </div> -->
    <!-- <div>
      <label for="birthdate">생년월일: </label>
      <input type="date" id="birthdate" v-model="credentials.birthdate">
    </div> -->
    <div class="input-signup">
      <label for="birthdate">생년월일</label>
      <b-form-datepicker id="birthdate" v-model="credentials.birthdate" class="mb-2"></b-form-datepicker>
    </div>
    <!--  -->
    <b-form-group label="성별" style="font-weight:600;">
      <b-form-radio-group
        v-model="credentials.gender"
        buttons
        button-variant="outline-secondary"
        class="mx-n1"
      ><template v-for="genderOption in genderOptions">
          <b-form-radio :value="genderOption.value" :key="genderOption.text" class="rounded-pill mx-1">
            {{ genderOption.text }}
          </b-form-radio>
        </template>
      </b-form-radio-group>
    </b-form-group>
    <!-- <div>
      <label for="gender">성별: </label>
      <div>
        <label for="male">남</label>
        <input type="radio" id="male" name="gender" v-model="credentials.gender" value=1>
      </div>
      <div>
        <label for="female">여</label>
        <input type="radio" id="female" name="gender" v-model="credentials.gender" value=2>
      </div>
    </div> -->
    <b-button class="action-button mt-4" @click="signup(credentials)">가입하기</b-button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'Signup',
  data: function () {
    return {
      genderOptions: [
        { text: '남', value: 1 },
        { text: '여', value: 2 },
      ],
      credentials: {
        username: '',
        password: '',
        passwordConfirmation: '',
        nickname: '',
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

<style>

.input-signup {
  display: block;
  padding: 35px;
}

.input-signup label {
  font-weight: 600;
}

</style>