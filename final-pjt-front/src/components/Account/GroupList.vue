<template>
  <div>
    <ul>
      <span @click="setGroupFilterId('전체')">전체</span><br>
      <span v-for="(group, idx) in groups" :key="idx">
        <span @click="setGroupFilterId(group.id)">{{ group.name }}</span>
        <button @click="deleteGroup(group.id)" v-if="group.name !== '기본'">삭제</button><br>
      </span>
    </ul>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'groupList',
  // data: function() {
  //   return {

  //   }
  // },
  methods: {
    ...mapActions('accountStore', [
      'getGroups',
      'deleteGroup',
      'getGroupRelationshipList',
      'setGroupFilterId',
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
  },
}
</script>

<style scoped>
  .group-btn {
    margin-left: 10px;
  }
</style>