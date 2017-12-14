<template lang="html">
<div class="ui vertical fluid menu">
  <a class="item" v-for="type in types">
    <div class="ui basic segment">
      <div class="image">
        <img width="100%" :src="type.image">
      </div>
      {{type.name}}
    </div>
  </a>

</div>
</template>

<script>
export default {
  name: 'menu',
  data: function () {
    return {
      types: [
        {
          name: '汉堡',
          image: 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1512637978985&di=dbc8184e59da2717e1cf9bec73b84f3c&imgtype=0&src=http%3A%2F%2Fimg000.hc360.cn%2Fy3%2FM06%2F36%2FB7%2FwKhQh1WBkueETFEAAAAAAN1Bgy8234.jpg'
        },
        {
          name: '套餐',
          image: 'https://timgsa.baidu.com/timg?image&quality=80&size=b10000_10000&sec=1512629140&di=dd31e13e1aa9f7409b7e87b53ac71b0d&src=http://img05.tooopen.com/images/20140327/sy_57725985633.jpg'
        },
        {
          name: '特价',
          image: 'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1670154472,205332476&fm=27&gp=0.jpg'
        },
        {
          name: '小食',
          image: 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1512638884423&di=22f08b8945ed4e0a170c70e8fd0b846b&imgtype=0&src=http%3A%2F%2Fwww.dinsong.com%2Fupload%2Fdish%2F573c918245e93CC%402x%402x.png'
        },
        {
          name: '甜品',
          image: 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1512638917152&di=1e7aaa510cea28f1b2825742cee92cb1&imgtype=0&src=http%3A%2F%2Fimg.100msh.net%2FItemsImage%2F141%2F26%2Fa229f052e47414.jpg'
        },
        {
          name: '饮料',
          image: 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1512638951217&di=1a0b8805589a26d6bff07e962b5b85ac&imgtype=0&src=http%3A%2F%2Fimg1.sc115.com%2Fuploads%2Fsc%2Fjpg%2F146%2F2261.jpg'
        }
      ]
    }
  }
}
</script>

<style lang="css">
.image{
  width:4rem;
}
</style>
