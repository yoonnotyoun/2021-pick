<template>
  <div>
    <p>{{ selectedBasketDetail }}</p>
    <h2>아래부터는 comment</h2>
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
  // created: function () {
  //   this.getBasketDetail(this.selectedBasketDetail)
  // }
}
</script>

<style>

</style>