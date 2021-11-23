<template>
  <div>
    <p>{{ selectedBasketDetail }}</p>
    <h2>이 바스켓에서 이야기 나누는 공간</h2>
    <b-form-checkbox @change="setSpoilerFilter(showSpoiler)" v-model="showSpoiler" name="spoiler-button" switch>
      스포일러 보기
    </b-form-checkbox>
    <comment-list></comment-list>
  </div>
</template>

<script>
import CommentList from '@/components/Basket/CommentList.vue'

import { mapState, mapActions } from 'vuex'

export default {
  name: 'BasketDetail',
  data: function () {
    return {
      showSpoiler: false,
    }
  },
  components: {
    CommentList,
  },
  methods: {
    ...mapActions('basketStore', [
      'setSpoilerFilter'
    ])
  },
  computed: {
    ...mapState('basketStore', {
      selectedBasketDetail: state => state.selectedBasketDetail,
      showSpoilerOption: state => state.showSpoilerOption,
    })
  },
}
</script>

<style>

</style>