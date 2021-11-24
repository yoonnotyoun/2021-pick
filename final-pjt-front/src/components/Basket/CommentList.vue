<template>
  <div>
    <comment-form></comment-form>
    <div v-if="showSpoilerOption">
      <ul v-for="(comment, idx) in comments" :comment="comment" :key="'spoilered' + idx">
        <span class="d-flex justify-content-between">
          <div class="d-flex">
            <p class="me-4 strong-text" @click="getProfile(comment.author)" style="cursor:pointer">{{ userInfo[comment.author].nickname }}</p>
            <p>{{ comment.content }}</p>
          </div>
          <div class="d-flex align-items-center">
            <p class="me-4">작성일 : {{ comment.created_at.split('T')[0] }}</p>
            <button @click="deleteComment(comment)" v-show="comment.author === userId" class="mb-3">X</button>
          </div>
        </span>
      </ul>
    </div>
    <div v-else>
      <ul v-for="(comment, idx) in comments" :comment="comment" :key="'notSpoilered' + idx">
        <div v-if="comment.spoiler === true && comment.author !== userId"> <!--  && comment.author !== userId -->
          <span class="d-flex justify-content-between">
            <div class="d-flex">
              <p class="me-4 strong-text" @click="getProfile(comment.author)" style="cursor:pointer">{{ userInfo[comment.author].nickname }}</p>
              <p>이 댓글은 스포일러가 포함된 댓글입니다.</p>
            </div>
            <p>작성일 : {{ comment.created_at.split('T')[0] }}</p>
          </span>
        </div>
        <div v-else>
          <span class="d-flex justify-content-between">
            <div class="d-flex">
              <p class="me-4 strong-text" @click="getProfile(comment.author)" style="cursor:pointer">{{ userInfo[comment.author].nickname }}</p>
              <p>{{ comment.content }}</p>
            </div>
            <div class="d-flex align-items-center">
              <p class="me-4">작성일 : {{ comment.created_at.split('T')[0] }}</p>
              <button @click="deleteComment(comment)" v-show="comment.author === userId" class="mb-3">X</button>
            </div>
          </span>
        </div>
      </ul>
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
    ]),
    ...mapActions('accountStore', [
      'getProfile',
    ])
  },
  computed: {
    ...mapState('basketStore', {
      comments: state => state.comments,
      noSpoilerComments: state => state.noSpoilerComments,
      showSpoilerOption: state => state.showSpoilerOption,
    }),
    ...mapState({
      userInfo: state => state.userInfo,
      userId: state => state.userId,
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