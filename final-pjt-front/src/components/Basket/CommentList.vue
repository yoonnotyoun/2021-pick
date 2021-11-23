<template>
  <div>
    <h3>코멘트리스트 올 자리</h3>
    <comment-form></comment-form>
    <div v-if="showSpoilerOption">
      <li v-for="(comment, idx) in comments" :comment="comment" :key="idx">
        <span>
          <p>스포일러여부: {{ comment.spoiler }}</p>
          <p>작성자 : {{ comment.author }}</p>
          <p>내용: {{ comment.content }}</p>
          <p>시간 : {{ comment.created_at }}</p>
        </span>
        <button @click="deleteComment(comment)">X</button>
      </li>
    </div>
    <div v-else>
      <li v-for="(comment, idx) in noSpoilerComments" :comment="comment" :key="idx">
        <span>
          <p>스포일러여부: {{ comment.spoiler }}</p>
          <p>작성자 : {{ comment.author }}</p>
          <p>내용: {{ comment.content }}</p>
          <p>시간 : {{ comment.created_at }}</p>
        </span>
        <button @click="deleteComment(comment)">X</button>
      </li>
    </div>
  </div>
</template>

<script>
import CommentForm from '@/components/Basket/CommentForm.vue'

import { mapState, mapActions } from 'vuex'

export default {
  name: 'CommentList',
  components: {
    CommentForm,
  },
  methods: {
    ...mapActions('basketStore', [
      'getCommentList',
      'deleteComment'
    ])
  },
  computed: {
    ...mapState('basketStore', {
      comments: state => state.comments,
      noSpoilerComments: state => state.noSpoilerComments,
      showSpoilerOption: state => state.showSpoilerOption,
    }),
  },
  created: function () {
    this.getCommentList()
  },
  // updated: function () {
  //   this.getCommentList()
  // },
}
</script>

<style>

</style>