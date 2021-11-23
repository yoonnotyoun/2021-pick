<template>
  <div>
    <ul>
      <li v-for="(group, idx) in groups" :key="idx">
        <span @click="filterGroupRelationshipList(group.name)">{{ group.name }}</span>
        <button @click="deleteGroup(group)">X</button>
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
      'getGroups',
      'deleteGroup',
      'getGroupRelationshipList',
    ]),
  },
  computed: {
    ...mapState('accountStore', {
      groups: state => state.groups,
    })
  },
  created: function () {
    if (this.$store.getters.isLoggedIn) {
      this.getGroups()
      this.getGroupRelationshipList()
    } else {
      this.$router.push({ name: 'Login' })
    }
    // console.log(this.$store.state.accoutStore.groups)
    console.log(this.groups)
  },
}
</script>

<style scoped>
  .group-btn {
    margin-left: 10px;
  }
</style>