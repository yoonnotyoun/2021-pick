<template>
  <div class="black-bg">
    <div class="white-bg">
      <h4>상세페이지</h4>
      <p>상세페이지내용임</p>
    </div>
  </div>
</template>

<script> // modal 안 할 수도 있음!!! 나중에 꼭 확인할 파일
export default {
  name: 'MovieDetailModal',
}
</script>

<style>
  body {
    margin : 0;
  }
  div {
    box-sizing: border-box;
  }
  .black-bg {
    width: 100%; height:100%;
    background: rgba(0,0,0,0.5);
    position: fixed; padding: 20px;
  }
  .white-bg {
    width: 100%; background: white;
    border-radius: 8px;
    padding: 20px;
  } 
</style>