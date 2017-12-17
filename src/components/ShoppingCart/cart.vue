<template lang="html">
  <div class="ui orange inverted bottom fixed menu">
    <div class="item">
      <i class="ui inverted big food icon"></i>
      $ {{TotalPrice}}
    </div>
    <!-- <div class="ui simple dropdown item">
      <i class="ui angle up big icon"></i>
      <div class="menu">
        <a class="item" v-for="item in ItemList">
          {{item.name}} | {{item.price}}
        </a>
      </div>
    </div> -->
    <div class="ui right orange inverted menu">
      <a class="item" @click="payBill()">
        Finished.
        <i class="ui right angle icon"></i>
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'cart',
  props: ['TotalPrice', 'ItemList'],
  data: function () {
    return {
      price: 0
    }
  },
  methods: {
    payBill: function () {
      this.$emit('transferPage', 2)
    }
  }
}
</script>

<style lang="css">
</style>
