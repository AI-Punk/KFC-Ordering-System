<template lang="html">
<div>
  <div class="ui red inverted top fixed menu">
    <a class="item" @click="returnPage()"><i class="angle left big icon"></i></a>
    <div class="item">
      <h3>{{title}}</h3>
    </div>
  </div>
  <div id="app-board">
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
      <payment-board :total-price="price" @transferPage="gotoPage"></payment-board>
    </div>
    <div v-if="app_status == 3">
      <order-board></order-board>
    </div>
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
import Order from './PaymentSystem/order.vue'

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
    PaymentBoard: Pay,
    OrderBoard: Order
  }
}
</script>

<style lang="css" scoped>
.ui.red.inverted.vertical.padded.segment{
  padding: 0.2rem;
}
#app-board{
  position: fixed;
  top: 3.6rem;
  bottom:3.6rem;
  left:0rem;
  right:0rem;
  /*overflow-y: auto;*/
}
/*#app-board > .ui.grid{
  height:100%;
}
#app-board > .ui.grid. > .six.wide.column{
  overflow-y: auto;
}*/
</style>
<style media="screen">
::-webkit-scrollbar{
  width: 2px!important;
  height: 2px;
  background-color: rgba(0,0,0,0);
}
/*定义滚动条的轨道，内阴影及圆角*/
::-webkit-scrollbar-track{
  border-radius: 1px;
  background-color: rgba(0,0,0,0);
}
/*定义滑块，内阴影及圆角*/
::-webkit-scrollbar-thumb{
  width: 2px;
  height: 20px;
  border-radius: 1px;
  -webkit-box-shadow: inset 0 0 1px rgba(0,0,0,0.2);
  background-color: rgba(255,122,122,0.5);
}
</style>
