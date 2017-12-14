<template lang="html">
<div>
  <div class="ui red inverted vertical padded segment">
    <div class="ui red inverted basic menu">
      <a class="item" @click="returnPage()"><i class="angle left big icon"></i></a>
      <div class="item">
        <h3>{{title}}</h3>
      </div>
    </div>
  </div>
  <div class="ui basic segment" v-if="app_status == 0">
    <login-board @transferPage="gotoPage"></login-board>
  </div>
  <div class="ui grid" v-if="app_status == 1">
    <div class="six wide column">
      <menu-board></menu-board>
    </div>
    <div class="ten wide column">
      <item-board @transferPrice="priceAdd"></item-board>
    </div>
  </div>
  <div v-if="app_status == 2">
    <payment-board :total-price="price"></payment-board>
  </div>
  <cart-board :total-price="price" :item-list="purchased_list" @transferPage="gotoPage" v-if="app_status == 1"></cart-board>
</div>

</template>

<script>
import Menu from './OrderSystem/menu.vue'
import Item from './OrderSystem/items.vue'
import Login from './Login/login.vue'
import Cart from './ShoppingCart/cart.vue'
import Pay from './PaymentSystem/pay.vue'

export default {
  name: 'main',
  data: function () {
    return {
      title: 'KFC',
      app_status: 0,
      price: 0,
      purchased_list: []
    }
  },
  methods: {
    gotoPage: function (i) {
      this.app_status = i
    },
    returnPage: function () {
      if (this.app_status > 0) {
        this.app_status --
      }
    },
    priceAdd: function (item) {
      this.price += parseInt(item.price)
      this.purchased_list.push(item)
    }
  },
  components: {
    MenuBoard: Menu,
    ItemBoard: Item,
    LoginBoard: Login,
    CartBoard: Cart,
    PaymentBoard: Pay
  }
}
</script>

<style lang="css" scoped>
.ui.red.inverted.vertical.padded.segment{
  padding: 0.2rem;
}
</style>
