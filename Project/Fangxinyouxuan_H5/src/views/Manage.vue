<template>
  <div class="manage">
    
    <div class="manage-head">
      <img src="@/assets/ic_user.png" class="icon-user">
      <div class="manage-head-username">{{username}}</div>
      <div class="manage-head-identity">{{identity}}</div>
    </div>
    <div class="manage-head-selector">
      <group>
        <PopupRadio @on-hide="onhide" title="" placeholder="在线商品" v-model="productStatusSelected" :options="productStatusList"></PopupRadio>
      </group>
    </div>
    <hr class="divider">

    <div class="manage-list">
      <div class="manage-list-title">
        {{productStatusSelected}}
        <img src="@/assets/search.png" class="icon-search">
      </div>
      <div class="manage-list-label">
        <div>每单返利</div>
        <div>价格</div>
        <div>库存</div>
      </div>
      <checker v-model="productSelected" type="checkbox" default-item-class="manage-list-item-selector" selected-item-class="manage-list-item-selector-selected">
        <div class="manage-list-item" v-for="item in items" :key="item.number">
            <checker-item :value="item.number"></checker-item>
            <img src="" class="img-product">
            <div class="manage-list-item-productName">{{item.productName}}</div>
            <div class="manage-list-item-productRebate">{{item.productRebate}}</div>
            <div class="manage-list-item-productPrice">{{item.productPrice}}</div>
            <div class="manage-list-item-productAmount">{{item.productAmount}}</div>
            <div class="manage-list-item-productStatus">{{item.productStatus}}</div>
        </div>
        <div class="button-more">
          <XButton @click.native="viewmore" mini>查看更多</XButton>
        </div>
        <div class="manage-list-tollbar">
          <checker-item :value="-1"></checker-item>
          <div style="margin-left: 1rem">全选</div>
          <div class="button-option">
            <XButton mini type="primary">{{productOption}}</XButton>
          </div>
        </div>
      </checker>
    </div>
    


  </div>
</template>

<script>
import { PopupRadio, Checker, CheckerItem,  XButton } from 'vux'

export default {
  name: 'manage',
  components: {
    PopupRadio,
    Checker,
    CheckerItem,
    XButton
  },

  data: function(){
      return{
        username: '青冥',
        identity: '小区店长',
        productStatusSelected: '在线商品',
        productStatusList: ['在线商品', '下架商品', '缺货商品', '全部商品'],
        productOption: '申请下架',
        productOptionList: ['申请下架', '申请上架', '心愿单', ''],
        items: [
          {
            number: '1',
            productName: '商品1',
            productRebate: '10%',
            productPrice: '10.0',
            productAmount: '666',
            productStatus: '在线'
          },
          {
            number: '2',
            productName: '商品2',
            productRebate: '10%',
            productPrice: '10.0',
            productAmount: '666',
            productStatus: '在线'
          },
          {
            number: '3',
            productName: '商品3',
            productRebate: '10%',
            productPrice: '10.0',
            productAmount: '666',
            productStatus: '在线'
          },
          {
            number: '4',
            productName: '商品4',
            productRebate: '10%',
            productPrice: '10.0',
            productAmount: '666',
            productStatus: '在线'
          },
          {
            number: '5',
            productName: '商品5',
            productRebate: '10%',
            productPrice: '10.0',
            productAmount: '666',
            productStatus: '在线'
          },
          {
            number: '6',
            productName: '商品6',
            productRebate: '10%',
            productPrice: '10.0',
            productAmount: '666',
            productStatus: '在线'
          },
          {
            number: '7',
            productName: '商品7',
            productRebate: '10%',
            productPrice: '10.0',
            productAmount: '666',
            productStatus: '在线'
          },
          {
            number: '8',
            productName: '商品8',
            productRebate: '10%',
            productPrice: '10.0',
            productAmount: '666',
            productStatus: '在线'
          },
          {
            number: '9',
            productName: '商品9',
            productRebate: '10%',
            productPrice: '10.0',
            productAmount: '666',
            productStatus: '在线'
          },
          {
            number: '10',
            productName: '商品10',
            productRebate: '10%',
            productPrice: '10.0',
            productAmount: '666',
            productStatus: '在线'
          },
        ],
        productSelected: ''
      }
  },

  methods: {
    viewmore(){
      
    }
      }
}
</script>

<style scoped>
.divider{
    color: #888888;
    line-height: 1px;
    margin: 1.25rem 0.9375rem;
}

.manage{
  display: flex;
  flex-direction: column;
}

.manage-head{
  display: flex;
  align-items: center;
  margin:4.5rem 0 0 0.9375rem;
}

.manage-head-username{
  margin:0 .9375rem;
}

.manage-head-identity{ 
  padding: 0.25rem 0.625rem;
  border: 1px solid;
  border-radius: 0.5rem;
}

.manage-head-selector{
  position: absolute;
  top: 4.25rem;
  right: 0.9375rem;
  z-index: 98;
}

.manage-list{
  display: flex;
  flex-direction: column;
  margin: 0 .9375rem;
}

.manage-list-title{
  font-size: 18px;
  align-self: center;
}

.manage-list-label{
  width: 40%;
  margin-top: .9375rem;
  display: flex;
  justify-content: space-between;
  align-self: center;
  position: relative;
  left: 3.5rem;
}

.manage-list-item{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  margin-bottom: .9375rem;
}

.manage-list-item-productStatus{ 
  padding: 0.25rem 0.625rem;
  border: 1px solid;
  border-radius: 0.5rem;
}

.manage-list-item-selector{
  width: 2rem;
  height: 2rem;
  border: 1px solid #ccc;
  display: inline-block;
  border-radius: 50%;
  line-height: 2.5rem;
  text-align: center;
}

.manage-list-item-selector-selected{
  background-color: #1AAD19;
}

.manage-list-tollbar{
  display: flex;
  margin-top: 1.25rem;
}

.icon-user{
  width: 3.125rem;
  height: 3.125rem;
}

.icon-search{
  width: 1.75rem;
  height: 1.8125rem;
  position: relative;
  left:100%;
}

.img-product{
  width: 3.75rem;
  height: 3.75rem;
}

.button-option{
  margin: 0 1.25rem;
}

.button-more{
  position: relative;
  left: 40%;
}

</style>