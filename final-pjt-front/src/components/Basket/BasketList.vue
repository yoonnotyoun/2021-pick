<template>
  <div>
    <div v-for="(basketListData, idx) in recommendedBaskets"
      :basketListData="basketListData"
      :key="idx">{{ basketListData.recommended_name }}
      <div class="container">
        <div class="basket-search-result row row-cols-1 row-cols-md-2 row-cols-xl-3">
          <basket-list-item v-for="(basket, idx) in basketListData.baskets"
            :basket="basket"
            :key="idx"
            class=""
          ></basket-list-item>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import BasketListItem from './BasketListItem.vue'

export default {
  components: { BasketListItem },
  name: 'BasketList',
  computed: {
    ...mapState('basketStore', {
      recommendedBaskets: state => state.recommendedBaskets
    })
  }
}
</script>

<style>

</style>