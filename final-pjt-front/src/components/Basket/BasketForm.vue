<template>
  <div>
    <div>
      <label for="title">바스켓 이름: </label>
      <input type="text" id="title" v-model="info.title">
    </div>
    <div>
      <label for="explanation">바스켓 설명: </label>
      <input type="text" id="explanation" v-model="info.explanation">
    </div>
    <div>
      <label for="tags">바스켓 태그: </label>
      <b-form-tags input-id="tags" v-model="info.tags"></b-form-tags>
    </div>
    <div>
      <b-form-group label="public" v-slot="{ ariaDescribedby }">
        <b-form-radio v-model="info.public" :aria-describedby="ariaDescribedby" name="public" value="True">공개</b-form-radio>
        <b-form-radio v-model="info.public" :aria-describedby="ariaDescribedby" name="public" value="False">비공개</b-form-radio>
      </b-form-group>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BasketForm',
  data: function () {
    return {
      info: {
        title: '',
        explanation: '',
        basket_tags_names: [],
        public: false,
        participants_ids: [],
        image: '',
        movies_ids: [],
      }
    }
  }
}
</script>

<style>

</style>