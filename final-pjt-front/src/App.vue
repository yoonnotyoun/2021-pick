<template>
  <div id="app">
    <div id="nav">
      <router-link :to="{ name: 'Main' }">P!ck</router-link> |
      <router-link :to="{ name: 'Movie' }">Movie</router-link> |
      <router-link :to="{ name: 'Basket' }">Basket</router-link> |
      <span v-if="isLoggedIn">
        <router-link :to="{ name: 'Profile' }">Profile</router-link> |
        <router-link :to="{ name: 'Group' }">Group</router-link> |
        <router-link @click.native="logout" to="#">Logout</router-link>
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
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
    ...mapActions('accountStore', [
      'logout',
      'getUserId',
      // 'getMovieData'
      ])
  },
  computed: {
    ...mapGetters('accountStore', [
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
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
