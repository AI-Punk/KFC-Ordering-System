<template lang="html">
  <div class="ui red inverted bottom fixed menu">
    <div class="item">
      <i class="ui inverted big food icon"></i>
      $ {{TotalPrice}}
    </div>
    <div class="ui right red inverted menu">
      <div class="item" @click="payBill()">
        Finished.
        <i class="ui right angle icon"></i>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'cart',
  props: ['TotalPrice'],
  data: function () {
    return {
      price: 0
    }
  },
  methods: {
    payBill: function () {
      this.$emit('transferPage',2)
    }
  }
}
</script>

<style lang="css">
</style>
