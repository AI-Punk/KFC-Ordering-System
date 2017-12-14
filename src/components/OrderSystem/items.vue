<template lang="html">
<div class="ui basic segment" id="item-list">
  <div class="ui divided items">
    <div class="item" v-for="(product,i) in products">
      <div class="formal image">
        <img :src="product.image">
      </div>
      <div class="content">
        <a class="header">{{product.name}}</a>
        <div class="meta">
          $ {{product.price}}
        </div>
        <div class="description">
          <div class="ui label" v-for="label in product.labels" :style="label.color">
            {{label.name}}
          </div>
        </div>
        <div class="extra">
          <button class="ui red button" type="button" name="button" @click="priceAdd(i)">加入购物车</button>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'items',
  data: function () {
    return {
      products: [
        {
          name: '至尊牛肉堡',
          image: 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1512640133987&di=7e02676bcf6e4012f0c77d22eec28d5e&imgtype=0&src=http%3A%2F%2Fimgsrc.baidu.com%2Fimgad%2Fpic%2Fitem%2Fb812c8fcc3cec3fdf42a2b50dc88d43f879427fa.jpg',
          price: 12.00,
          labels: [
            {
              name: '汉堡',
              color: ''
            },
            {
              name: '特价',
              color: 'orange'
            }
          ]
        },
        {
          name: '香辣鸡肉堡',
          image: 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1512637978985&di=dbc8184e59da2717e1cf9bec73b84f3c&imgtype=0&src=http%3A%2F%2Fimg000.hc360.cn%2Fy3%2FM06%2F36%2FB7%2FwKhQh1WBkueETFEAAAAAAN1Bgy8234.jpg',
          price: 8.00,
          labels: [
            {
              name: '汉堡',
              color: ''
            },
            {
              name: '特价',
              color: 'orange'
            }
          ]
        },
        {
          name: '奢华薯条',
          image: 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1512640172198&di=d4a186bafc7ab88e01cb87cc884cb59c&imgtype=0&src=http%3A%2F%2Fscimg.jb51.net%2Fallimg%2F160318%2F14-16031Q41Z3334.jpg',
          price: 4.00,
          labels: [
            {
              name: '小食',
              color: ''
            }
          ]
        },
        {
          name: '巧克力圣代',
          image: 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1512638917152&di=1e7aaa510cea28f1b2825742cee92cb1&imgtype=0&src=http%3A%2F%2Fimg.100msh.net%2FItemsImage%2F141%2F26%2Fa229f052e47414.jpg',
          price: 2.00,
          labels: [
            {
              name: '甜品',
              color: ''
            },
            {
              name: '特价',
              color: 'green'
            }
          ]
        }
      ]
    }
  },
  methods: {
    priceAdd: function (i) {
      this.$emit('transferPrice', this.products[i])
    }
  }
}
</script>

<style lang="css">
.formal.image{
  /*width:10rem;*/
}
#item-list{
  height:729px;
  overflow:auto;
}
#item-list > .ui.divided.items > .item > .content > .meta{
  font-size: 1.6rem;
  color: rgb(213, 80, 31)!important
}
</style>
