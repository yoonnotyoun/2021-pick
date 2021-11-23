<template>
  <div>
    <h3>코멘트리스트 올 자리</h3>
    <comment-form></comment-form>
    <p>{{ selectedBasketDetail }}</p>
    <li v-for="(comment, idx) in comments" :comment="comment" :key="idx">
      <span>
        <p>{{ comment.author }}</p>
        <p>{{ comment.content }}</p>
        <p>{{ comment.created_at }}</p>
      </span>
      <button>X</button>
    </li>
  </div>
</template>

<script>
import CommentForm from '@/components/Basket/CommentForm.vue'

import { mapState } from 'vuex'

export default {
  name: 'CommentList',
  components: {
    CommentForm,
  },
  methods: {
  },
  computed: {
    ...mapState('basketStore', {
      comments: state => state.comments,
      selectedBasketDetail: state => state.selectedBasketDetail
    })
  }
}
</script>

<style>

</style>