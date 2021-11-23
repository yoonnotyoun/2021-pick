<template>
  <div>
    <h2>바스켓</h2>
    <h3>바스켓검색창 / 추천기준 5줄</h3>
    <basket-search-bar></basket-search-bar>
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
      'getBasketRecommendation',
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