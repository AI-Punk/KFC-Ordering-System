<template lang="html">
  <div class="ui basic segment">
    <div class="ui segment" id="order-num">
      <h3 class="ui header">订单号</h3>
      <p>凭此订单号取餐</p>
      <div class="ui divider">

      </div>
      <h1 class="ui red header">1501</h1>
      <div class="ui divider"></div>
      <button class="ui red button" type="button" name="button" @click="gotoMainPage()">Back</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'order',
  data: function () {
    return {}
  },
  methods: {
    gotoMainPage: function () {
      this.$emit('transferPage', 1)
      this.initShoppingCart()
    },
    initShoppingCart: function () {
      this.$emit('transferShoppingCart', 0)
    }
  }
}
</script>

<style lang="css">
#order-num{
  margin:auto;
}
</style>
