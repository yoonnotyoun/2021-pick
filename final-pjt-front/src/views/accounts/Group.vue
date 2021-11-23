<template>
  <div>
    <h2>그룹관리</h2>
    <group-list></group-list>
    <relationship-list></relationship-list>
  </div>
</template>

<script>
// import { mapState, mapActions } from 'vuex'
import GroupList from '../../components/Account/GroupList.vue'
import RelationshipList from '../../components/Account/RelationshipList.vue'

export default {
  name: 'Group',
  components: { GroupList, RelationshipList },
  // methods: {
  //   ...mapActions('accountStore', [
  //     'getProfile'
  //   ])
  // },
  // computed: {
  //   ...mapState('accountStore', [
  //     'profileInfo',
  //   ])
  // },
  // created: function () {
  //   this.getProfile()
  // }
}
</script>

<style>

</style>