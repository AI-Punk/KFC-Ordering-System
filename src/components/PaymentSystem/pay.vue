<template lang="html">
  <div class="ui basic segment">
    <div class="ui segment">
      <h3 class="ui header">就餐方式</h3>
      <div class="ui buttons">
        <button class="ui red inverted button" type="button" name="button">堂食</button>
        <button class="ui orange inverted button" type="button" name="button">外带</button>
      </div>
    </div>
    <div class="ui segment">
      <h3 class="ui header">联系方式</h3>
      <form class="ui form" action="index.html" method="post">
        <div class="field">
          <input type="text" name="" value="1383838438">
        </div>
      </form>
    </div>
    <div class="ui segment">
      <h3 class="ui header">价格</h3>
      $ {{TotalPrice}}
      <div class="ui divider"></div>
      <h3 class="ui header">支付方式</h3>
      <div class="ui five column grid">
        <div class="column" v-for="type in types">
          <div class="ui card">
            <div class="ui circular image">
              <img :src="type.image" alt="">
            </div>
          </div>
        </div>
      </div>
      <div class="ui divider"></div>
      <button class="ui green button" type="button" name="button" @click="confirmPayment()">确认支付</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'pay',
  props: ['TotalPrice'],
  data: function () {
    return {
      types: [
        {
          title: 'Wechat',
          image: 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1513851389&di=5d72b246f4f7da4b1d1d8f1ba9204f38&imgtype=jpg&er=1&src=http%3A%2F%2F58pic.ooopic.com%2F58pic%2F12%2F25%2F04%2F02k58PICVwf.jpg'
        },
        {
          title: 'QQ',
          image: 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1513256702768&di=66ef517ec3c5587ee883b124ba6096d2&imgtype=0&src=http%3A%2F%2Fdown1.sucaitianxia.com%2Fai%2F21%2Fai4572.jpg'
        },
        {
          title: 'Weibo',
          image: 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1403279034,2865000485&fm=27&gp=0.jpg'
        }
      ]
    }
  },
  methods: {
    confirmPayment: function () {
      this.$emit('transferPage', 3)
    }
  }
}
</script>

<style lang="css">
</style>
