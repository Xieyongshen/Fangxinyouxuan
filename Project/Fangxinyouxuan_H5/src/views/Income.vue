<template>
  <div class="income">
    <img src="@/assets/me-bg.png" class="me-bg">

    <div class="me-userinfo">
      <div class="me-share">分享店铺</div>
      <img class="me-userinfo-avatar">
      <div class="me-userinfo-name">nickName</div>
    </div>

    <grid class="income-totalSales">
      <grid-item>
        <div class="income-totalSales-money">
          <div class="income-totalSales-money-label">累计销售额</div>
          <div class="income-totalSales-money-total">
            <img src="@/assets/ic_money.png" class="icon-money">
            <div>{{totalSales}}</div>
          </div>
        </div>
      </grid-item>
      <grid-item label="查看我的金库" link="/account">
        <img slot="icon" src="@/assets/ic_user.png">
      </grid-item>
    </grid>

    <grid class="income-detailedSales">
      <grid-item class="income-totalSales-money">
        <div>今日销售额</div>
        <div>{{todaySales}}</div>
      </grid-item>
      <grid-item class="income-totalSales-money">
        <div>本周销售额</div>
        <div>{{weekSales}}</div>
      </grid-item>
      <grid-item class="income-totalSales-money">
        <div>本月销售额</div>
        <div>{{mouthSales}}</div>
      </grid-item>
    </grid>

    <grid class="income-totalIncome">
      <grid-item>
        <div class="income-totalIncome-money">
          <div class="income-totalIncome-money-total">
            <img src="@/assets/ic_totalIncome.png" class="icon-totalIncome">
            <div>累计销售收益</div>
          </div>
          <div class="income-totalSales-money-label">{{totalIncome}}</div>
        </div>
      </grid-item>
      <grid-item>
        <div class="income-totalIncome-money">
          <div class="income-totalIncome-money-total">
            <img src="@/assets/ic_totalOrder.png" class="icon-totalIncome">
            <div>累计订单</div>
          </div>
          <div class="income-totalSales-money-label">{{totalOrders}} 笔</div>
        </div>
      </grid-item>
    </grid>

    <div class="income-trend-selector">
      <group>
        <PopupRadio title="销售趋势图" placeholder="今日" v-model="trend" :options="trendList"></PopupRadio>
      </group>
    </div>

    <img class="img-trend" src="@/assets/trend.png">

  </div>
</template>

<script>
import { Grid, GridItem, PopupRadio } from 'vux'

export default {
  name: 'income',
  components: {
    Grid,
    GridItem,
    PopupRadio
  },

  data: function(){
      return{
        totalSales: '66666.0',
        todaySales: '666.0',
        weekSales: '6666.0',
        mouthSales: '16666.0',
        totalIncome: '23333.0',
        totalOrders: '666',
        trend: '今日',
        trendList: ['今日', '本周', '本月', '历史']
      }
  }
}
</script>

<style scoped>

.me-bg {
    width: 100%;
    height: 18.75rem;
    position: absolute;
    z-index: -1;
}

.me-userinfo {
    width: 100%;
    height: 14.6875rem;
    margin-bottom: 4.375rem;
    padding-top: 0.9375rem;
    text-align: center;
    box-sizing: border-box;
    position: relative;

}

.me-userinfo-avatar {
    width: 6.25rem;
    height: 6.25rem;
    border: 0.3125rem solid #ffffff;
    border-radius: 50%;
    background: #d4d5d2;
    box-sizing: border-box;
    margin-top: 3.125rem;
}

.me-userinfo-name {
    width: 100%;
    height: 2.1875rem;
    color: #ffffff;
    font-size: 1.0625rem /* 17/16 */;
    line-height: 1.875rem;
    text-align: center;
    margin-top: 0.625rem;
    box-sizing: border-box;
    display: block;
}

.me-share {
    color: #ffffff;
    font-size: 1.0625rem /* 17/16 */;
    line-height: 30px;
    position: absolute;
    top: 0.625rem;
    left: 1.875rem;
}

.income-totalSales{
  margin: 0;
}

.income-totalSales-money{
  color: #333;
  font-size: 14px;
  text-align: center;
}

.income-totalSales-monye-label{
  display: block;
}

.income-totalSales-money-total{
  color: #fdb85d;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: .5rem;
}

.income-detailedSales{
  margin: 1.25rem 0;
}

.income-totalIncome-money{
  color: #333;
  font-size: 14px;
  text-align: center;
}

.income-totalIncome-monye-label{
  display: block;
}

.income-totalIncome-money-total{
  display: flex;
  justify-content: center;
  align-items: center;
}

.icon-money{
  width: 2.25rem;
  height: 2.25rem;
}

.icon-totalIncome{
  width: 2.5rem;
  height: 2.5rem;
  margin: 0 .3125rem;
}

.img-trend{
  width: 70%;
  margin: 1.25rem 15%;
}



</style>
