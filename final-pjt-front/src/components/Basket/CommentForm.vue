<template>
  <div>
    <div class="text-start d-flex align-items-center mt-2">
      <span class="me-2">스포일러를 포함하기</span>
      <input type="checkbox" name="spoiler" v-model="spoiler"><br>
    </div>
    <div class="">
      <input type="text" @keypress.enter="createAndErase({ content, spoiler })" v-model.trim="content" class="form-control mt-2 mb-4" placeholder="댓글을 입력해주세요.">
      <!-- <button @click="createAndErase({ content, spoiler })" class="mb-3">등록하기</button> -->
    </div>
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