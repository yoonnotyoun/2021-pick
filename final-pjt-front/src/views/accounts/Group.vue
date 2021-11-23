<template>
  <div>
    <h2>그룹관리</h2>
    <create-group></create-group>
    <group-list></group-list>
    <relationship-list></relationship-list>
  </div>
</template>

<script>
import CreateGroup from '../../components/Account/CreateGroup.vue'
import { mapState, mapActions } from 'vuex'
import GroupList from '../../components/Account/GroupList.vue'
import RelationshipList from '../../components/Account/RelationshipList.vue'

export default {
  name: 'Group',
  components: { GroupList, RelationshipList, CreateGroup },
  methods: {
    ...mapActions('accountStore', [
    ])
  },
  computed: {
    ...mapState('accountStore', [
    ])
  },
  created: function () {
  }
}
</script>

<style>

</style>