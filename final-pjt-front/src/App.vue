<template>
  <div id="app" class="container-fluid">
    <img id="line" src="@/assets/navbar.png" width="vw" alt="line">
    <div>
      <router-link :to="{ name: 'Main' }">
        <img src="@/assets/logo.png" alt="p!ck logo" width="75px" class="d-inline-block"/>your taste
      </router-link>
    </div>
    <div id="nav">
        <router-link :to="{ name: 'Movie' }">Movie</router-link>
        <router-link :to="{ name: 'Basket' }">Basket</router-link>
        <b-avatar variant="info" src="https://placekitten.com/300/300"></b-avatar>
      <!-- <router-link :to="{ name: 'SetMovieTaste' }">SetMovieTaste</router-link> | -->
      <span v-if="isLoggedIn">
        <router-link :to="{ name: 'Profile' }">Profile</router-link>
        <router-link :to="{ name: 'Group' }">Group</router-link>
        <router-link @click.native="logout" to="#">Logout</router-link>
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">Signup</router-link>
        <router-link :to="{ name: 'Login' }">Login</router-link>
      </span>
    </div>
    <router-view/>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'App',
  methods: {
    ...mapActions([
      'logout',
      'getUserId',
      // 'getMovieData'
      ])
  },
  computed: {
    ...mapGetters([
      'isLoggedIn',
    ])
  },
  created: function () {
    this.getUserId()
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
  top: 90px; left: 0px;
  width: 100%;
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
