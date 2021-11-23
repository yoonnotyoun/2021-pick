<template>
  <div>
    <h3>코멘트 폼</h3>
    <p>스포일러 포함하기</p>
    <input type="checkbox" name="spoiler" v-model="spoiler">
    <input type="text" v-model.trim="content">
    <button @click="createAndErase({ content, spoiler })">등록하기</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'CommentForm',
  data: function () {
    return {
      content: '',
      spoiler: false,
    }
  },
  methods: {
    createAndErase: function ({ content, spoiler }) {
      this.createComment({ content, spoiler })
      this.content = ''
      this.spoiler = false
    },
    ...mapActions('basketStore', [
      'createComment',
    ]),
  },
}
</script>

<style>

</style>