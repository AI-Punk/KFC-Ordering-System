<template lang="html">
  <div class="ui container">
    <div class="ui basic segment">
      <h1 class="ui header">请以下订单号的用户取餐</h1>
    </div>
    <div class="ui red segment" v-for="order in orders">
      <h1 class="ui header">{{order.id}}</h1>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'AlertSystem',
  data () {
    return {
      orders: []
    }
  },
  mounted () {
    var orders
    $.ajax({
      url: 'http://localhost:5000/api/getorders',
      methods: 'get',
      dataType: 'json',
      async: false,
      success (res) {
        orders = res.orders
      }
    })
    console.log(orders)
    this.orders = orders
  }
}
</script>

<style lang="css">
</style>
