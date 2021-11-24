<template>
  <div id="app" class="container-fluid">
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
          <router-link :to="{ name: 'Main' }">
            <img src="@/assets/logo.png" alt="p!ck logo" width="75px" class="d-inline-block"/> your taste
          </router-link>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
              <li class="nav-item mx-2 mt-2">
                <router-link class="nav-link" :to="{ name: 'Movie' }">영화</router-link>
              </li>
              <li class="nav-item mx-2 mt-2">
                <router-link class="nav-link" :to="{ name: 'Basket' }">바스켓</router-link>
              </li>
              <li class="nav-item mx-2 mt-3" v-if="isLoggedIn">
                <router-link :to="{ name: 'Profile', userId: userId }">{{ userInfo[userId].nickname }}</router-link> 님, 환영합니다!
              </li>
              <li class="nav-item mx-2 mt-3" v-else>
                [로그인 후 이용 부탁 드립니다.]
              </li>
              <li class="nav-item dropdown mx-2">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  <b-avatar variant="info" src="https://placekitten.com/300/300"></b-avatar>
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink" v-if="isLoggedIn">
                  <li class="nav-item mx-3 my-2"><router-link :to="{ name: 'Profile', userId: userId }">내 프로필</router-link></li>
                  <li class="nav-item mx-3 my-2"><router-link :to="{ name: 'Group' }">그룹 관리</router-link></li>
                  <li class="nav-item mx-3 my-2"><router-link @click.native="logout" to="#">로그아웃</router-link></li>
                </ul>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink" v-else>
                  <li class="nav-item mx-3 my-2"><router-link :to="{ name: 'Signup' }">회원가입</router-link></li>
                  <li class="nav-item mx-3 my-2"><router-link :to="{ name: 'Login' }">로그인</router-link></li>
                </ul>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      <!-- <img id="line" src="@/assets/navbar.png" width="vw" alt="line" class="wave-line m-0 p-0"> -->
    <router-view/>
  </div>
</template>

<script>
import { mapGetters, mapActions, mapState } from 'vuex'

export default {
  name: 'App',
  methods: {
    ...mapActions([
      'logout',
      'getUserId',
      'setUserInfo',
      // 'getMovieData'
      ]),
    ...mapActions('accountStore', [
      'getProfile',
    ]),
  },
  computed: {
    ...mapGetters([
      'isLoggedIn',
    ]),
   ...mapState({
      userId: state => state.userId,
      userInfo: state => state.userInfo,
    })
  },
  created: function () {
    this.getUserId()
    this.setUserInfo()
  }
}
</script>


<style>

#app {
  font-family: 'Gothic A1', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #222222;
  background-color: #f9f9f9;
}

#nav {
  padding: 35px;
}

#nav a {
  font-size: 95%;
  font-weight: 600;
  color: #222222;
  margin: 30px;
}

#line {
  position: absolute;
  top: 35px; left: 0px;
  width: 100%;
  z-index: 10;
}

#nav a.router-link-exact-active {
  color: #5a89cf;
}

.action-button {
  font-family: 'Hahmlet', serif;
  font-weight: 500;
  color: #ffffff;
  background-color: #5a89cf !important;
  border-color: #5a89cf !important;
}

</style>
