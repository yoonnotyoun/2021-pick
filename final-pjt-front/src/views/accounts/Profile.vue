<template>
  <div>
    <header>
      <!-- <img :src="userInfo.image" alt="profile"> -->
      <p>{{ userInfo.username }}</p>
      <p>{{ userInfo.birthdate }}</p>
      <p>{{ userInfo.gender }}</p>
      <p>팔로워: {{ userInfo.fans }}</p>
      <p>팔로잉: {{ userInfo.stars }}</p>
    </header>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
// import SERVER from '@/api/drf.js'

export default {
  name: 'Profile',
  methods: {
    ...mapActions([
      'getProfile'
    ])
  },
  computed: {
    ...mapState([
      'userInfo',
    ])
  },
  created: function () {
    this.getProfile()
  }
}
</script>

<style>

</style>