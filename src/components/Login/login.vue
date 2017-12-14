<template lang="html">
  <div class="ui segment">
    <h3 class="ui header">Login Methods</h3>
    <div class="ui divider">

    </div>
    <div class="ui three column grid">
      <div class="column" v-for="method in methods">
        <div class="ui link card" @click="gotoPage()">
          <div class="ui image">
            <img style="width:100%" :src="method.image" alt="">
          </div>
          <div class="extra">
            {{method.title}}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'login',
  data: function () {
    return {
      methods: [
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
    gotoPage: function () {
      console.log('change page')
      this.$emit('transferPage', 1)
    }
  }
}
</script>

<style lang="css" scoped>
.ui.image > img{
  height: 4rem
}
</style>
