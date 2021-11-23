<template>
  <div>
    <header>
      <!-- <img :src="userInfo.image" alt="profile"> -->
      <p>{{ profileInfo.username }}</p>
      <p>{{ profileInfo.birthdate }}</p>
      <p>{{ profileInfo.gender }}</p>
      <p>팔로워: {{ profileInfo.fans }}</p>
      <p>팔로잉: {{ profileInfo.stars }}</p>
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
    ...mapState('accountStore', [
      'profileInfo',
    ])
  },
  created: function () {
    this.getProfile()
  }
}
</script>

<style>

</style>