<template>
  <div>
    <div class="basket-search-result row row-cols-3">
      <basket-list-item
        v-for="(basket, idx) in searchedBaskets"
        :basket="basket"
        :key="idx"
      ></basket-list-item>
    </div>
  </div>
</template>

<script>
import BasketListItem from '@/components/Basket/BasketListItem.vue'

import { mapState } from 'vuex'

export default {
  name: 'BasketSearchResult',
  components: {
    BasketListItem,
  },
  computed: {
    ...mapState('basketStore', {
      searchedBaskets: state => state.searchedBaskets
    })
  },
}
</script>

<style>

</style>