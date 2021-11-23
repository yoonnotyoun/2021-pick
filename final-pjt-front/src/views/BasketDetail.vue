<template>
  <div>
    <p>{{ selectedBasketDetail }}</p>
    <h2>이 바스켓에서 이야기 나누는 공간</h2>
    <!-- 버튼 -->
    <comment-list></comment-list>
  </div>
</template>

<script>
import CommentList from '@/components/Basket/CommentList.vue'

import { mapState } from 'vuex'

export default {
  name: 'BasketDetail',
  components: {
    CommentList,
  },
  methods: {
    // ...mapActions('basketStore', [
    //   'getBasketDetail',
    // ])
  },
  computed: {
    ...mapState('basketStore', {
      selectedBasketDetail: state => state.selectedBasketDetail
    })
  },
}
</script>

<style>

</style>