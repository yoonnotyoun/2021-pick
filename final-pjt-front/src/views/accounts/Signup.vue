<template>
  <div class="container mt-5">
    <div><br>
      <p class="d-inline-block"
      style="font-family: 'Hahmlet', serif; font-weight: 600; font-size: 1.6rem; color: #222222;"
      >회원가입</p>
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
        placeholder="비밀번호를 입력해주세요."></b-form-input>
    </div>
    <div class="input-signup">
      <label for="passwordConfirmation" class="d-flex">비밀번호 확인</label>
      <b-form-input
        id="passwordConfirmation"
        type="password"
        v-model="credentials.passwordConfirmation"
        placeholder="비밀번호를 다시 입력해주세요."></b-form-input>
      <b-alert show variant="warning" style="text-align:start;"
        v-if="credentials.passwordConfirmation && (credentials.password != credentials.passwordConfirmation)">
        비밀번호가 일치하지 않습니다. 다시 입력해주세요.</b-alert>
    </div>
    <div class="input-signup">
      <label for="nickname" class="d-flex">닉네임</label>
      <b-form-input
        id="nickname"
        type="text"
        v-model="credentials.nickname"
        placeholder="서비스 내에서 사용할 닉네임을 입력해주세요."></b-form-input>
    </div>
    <div class="input-signup">
      <label for="birthdate" class="d-flex">생년월일</label>
      <b-form-input id="birthdate" type="date" v-model="credentials.birthdate" class="mb-2"></b-form-input>
    </div>
    <div class="input-signup">
      <b-form-group label="성별" align="left" style="font-weight:600;">
        <b-form-radio-group
          v-model="credentials.gender"
          buttons
          button-variant="outline-secondary"
          class="mx-n1"
          align="left"
        ><template v-for="genderOption in genderOptions">
            <b-form-radio :value="genderOption.value" :key="genderOption.text" class="rounded-pill mx-1">
              {{ genderOption.text }}
            </b-form-radio>
          </template>
        </b-form-radio-group>
      </b-form-group>
    </div>
    <b-button class="action-button m-4" @click="signup(credentials)">가입하기</b-button>
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
      },
      isInvalid: false,
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