<template>
  <div>
    <ul>
      <b-row>
        <b-col md="7"></b-col>
        <b-col md="3" class="px-0">
          <b-form-select v-model="selected" :options="options">
            <option disabled value="">선택</option>
            <option v-for="(group, idx) in groups" :key="idx" :value="group.id">{{ group.name }}</option>
          </b-form-select>
        </b-col>
        <b-col md="2" class="px-0">
          <b-button pill class="mini-button" @click="changeRelationshipGroup({ selectedRelationships, selectedGroup })">그룹 이동</b-button>
        </b-col>
      </b-row>
      <!-- <select v-model="selectedGroup" class="d-inline">
        <option disabled value="">선택</option>
        <option v-for="(group, idx) in groups" :key="idx"
        :value="group.id">{{ group.name }}</option>
      </select> -->
      <li v-for="(relationship, idx) in filterRelationshipList(relationshipList, groupFilterId)" :key="idx">
        <input type="checkbox" :value="relationship.id" v-model="selectedRelationships">
        <span> {{ relationship.star.username }} </span>
        <span>{{ relationship.star.nickname }} </span>
        <span>{{ relationship.group.name }}</span>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'RelationshipList',
  data: function () {
    return {
      selectedRelationships: [],
      selectedGroup: '',
    }
  },
  methods: {
    ...mapActions('accountStore', [
      'changeRelationshipGroup',
    ]),
    filterRelationshipList: function (relationshipList, groupFilterId) {
      return relationshipList.filter(relationship => {
        console.log(relationship.id)
        console.log(relationship.id === this.groupFilterId)
        if (groupFilterId === '전체') {
          return relationship
        } else {
          return relationship.group.id === this.groupFilterId
        }
      })
    }
  },
  computed: {
    ...mapState('accountStore', {
      relationshipList: state => state.relationshipList,
      groupFilterId: state => state.groupFilterId,
      groups: state => state.groups,
    })
  },
}
</script>

<style scoped>
  .group-btn {
    margin-left: 10px;
  }
</style>