<template>
  <div>
    <ul>
      <li v-for="(relationship, idx) in relationshipList" :key="idx">
        <input type="checkbox">
        <span>{{ relationship.star.username }}</span>
        <span>{{ relationship.star.nickname }}</span>
        <span>{{ relationship.group.name }}</span>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'groupList',
  methods: {
    ...mapActions('accountStore', [
    ]),
  },
  computed: {
    ...mapState('accountStore', {
      relationshipList: state => state.relationshipList,
    })
  },
  // created: function () {
  //   if (this.$store.getters.isLoggedIn) {
  //     this.getGroups()
  //   } else {
  //     this.$router.push({ name: 'Login' })
  //   }
  // },
}
</script>

<style scoped>
  .group-btn {
    margin-left: 10px;
  }
</style>