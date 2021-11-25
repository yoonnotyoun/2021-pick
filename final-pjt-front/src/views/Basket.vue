<template>
  <div class="mt-5 container">
    <basket-search-bar class="mt-4"></basket-search-bar>
    <div align="right" class="mx-3">
      <b-button class="action-button mb-3" @click="showBasketForm">새 바스켓 생성</b-button>
    </div>
    <basket-search-result v-if="searchedBaskets"></basket-search-result>
    <basket-list v-if="recommendedBaskets"></basket-list>
  </div>
</template>

<script>
import BasketList from '@/components/Basket/BasketList.vue'
import BasketSearchBar from '@/components/Basket/BasketSearchBar.vue'
import BasketSearchResult from '@/components/Basket/BasketSearchResult.vue'

import { mapState, mapActions } from 'vuex'

export default {
  name: 'Basket',
  components: {
    BasketList,
    BasketSearchBar,
    BasketSearchResult,
  },
  methods: {
    ...mapActions('basketStore', [
      'resetBaskets',
      'showBasketForm',
      'getBasketRecommendation',
      'resetBaskets',
    ])
  },
  computed: {
    ...mapState('basketStore', {
      searchedBaskets: state => state.searchedBaskets,
      recommendedBaskets: state => state.recommendedBaskets,
    })
  },
  created: function () {
    if (this.$store.getters.isLoggedIn) {
      this.resetBaskets('recommended')
      this.getBasketRecommendation()
      this.getBasketRecommendation()
      this.getBasketRecommendation()
      this.getBasketRecommendation()
      this.getBasketRecommendation()
    }
  }
}
</script>

<style>

</style>