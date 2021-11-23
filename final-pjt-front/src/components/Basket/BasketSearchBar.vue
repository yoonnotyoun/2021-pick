<template>
  <div>
    <input @keypress.enter="getBasketSearchResult" type="text" placeholder="Basket Search">
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'BasketSearchBar',
  methods: {
    ...mapActions('basketStore', [
      'getBasketSearchResult',
    ])
  },
  computed: {
    ...mapState('basketStore', {
      baskets: state => state.baskets,
    })
  },
}
</script>

<style>

</style>