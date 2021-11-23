<template>
  <div>
    <input type="text" v-model.trim="name" @keypress.enter="createGroup(name)">
    <button @click="callCreateGroup">그룹 생성</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'CreateGroup',
  data: function () {
    return {
      name: '',
    }
  },
  methods: {
    ...mapActions('accountStore', [
      'createGroup',
    ]),
    callCreateGroup: function() {
      this.createGroup(this.name)
      this.name = ''
    }
  }
}
</script>