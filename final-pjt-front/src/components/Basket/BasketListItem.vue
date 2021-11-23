<template>
  <div class="col" @click="getBasketDetail(basket)">
    <div class="card">
      <img :src="basket.image" alt="basket image">
      <div class="card-body">
        <p>{{ basket.title }}</p>
        <p>{{ basket.like_users }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'BasketListItem',
  props: {
    basket: {
      type: Object,
    },
  },
  methods: {
    ...mapActions('basketStore', [
      'getBasketDetail',
    ])
  },
}
</script>

<style>

</style>