<template>
  <div class="order">
    <div class="order-userInfo">
      <img class="userInfo-avatar">
      <div class="userInfo-name">xxx</div>
      <div class="userInfo-label">小区店长</div>
    </div>

    <flexbox :gutter="0" class="order-flexbox">
      <flexbox-item class="order-flexbox-item">
        <div class="order-flexbox-label">今日订单</div>
        <div class="order-flexbox-count">8888单</div>
      </flexbox-item>
      <flexbox-item class="order-flexbox-item">
        <div class="order-flexbox-label">今日销售额</div>
        <div class="order-flexbox-count">￥8888.88</div>
      </flexbox-item>
    </flexbox>

    <div class="order-search">
      <x-icon type="ios-search-strong" class="order-search-icon"></x-icon>
      <input type="text" placeholder="订单号、客户名、手机号" class="order-search-input" v-model="searchValue" v-on:click="type = 0">
    </div>

    <div class="order-type">
      <tab custom-bar-width="30px">
        <tab-item class="order-type-item" :selected="type === index" v-for="(item, index) in typeList" @on-item-click="changeType" :key="index">{{item}}</tab-item>
      </tab>
    </div>

    <div class="order-list-all" v-if="type == 0">
      <div class="order-list-item" v-for="(item, index) in searchFor(orderList, searchValue)" :key="index">
        <div class="order-head">
          <span>{{item.createTime}}</span>
          <span class="order-text-tip">单号：{{item.orderNum}}</span>
        </div>
        <div class="order-info">
          <div class="order-user">
            <div>客户：{{item.user.name}}</div>
            <div>电话：{{item.user.phone}}</div>
            <div>微信号：{{item.user.wechat}}</div>
          </div>
          <div class="order-status">{{statusList[item.status]}}</div>
        </div>
        <div class="order-product">
          <div class="order-product-item" v-for="(item, index) in item.product" :key="item.id">
            <img class="order-product-img">
            <div class="order-product-content">
              <div class="order-product-name">{{item.name}}</div>
              <div class="order-product-price">￥{{item.price}}</div>
            </div>
            <div class="order-product-count">数量<br>× {{item.count}}</div>
          </div>
        </div>
        <div class="order-status-list">
          <div class="order-status-item" v-if="sindex != 2 && sindex != 4" v-for="status,sindex in statusList" :key="status.index">
            <span>{{status}}</span>
            <div class="order-status-active" v-if="(item.status == 0 && sindex == 0) || (item.status >= sindex && sindex > 0)"></div>
          </div>
          <div class="order-total">￥{{item.total}}</div>
        </div>
      </div>
    </div>

    <div class="order-toDeliver" v-if="type == 1">
      <div class="order-toDeliver-time">
        <span>我的订单</span>
        <div class="order-text-tip">
          <div>预计发货时间：{{toSendTime}}</div>
          <div>预计到货时间：{{toReceiveTime}}</div>
        </div>
      </div>
      <div class="order-toDeliver-item" v-for="(item, index) in orderList" v-if="item.status == 2" :key="index">
        <div class="order-toDeliver-info">
          <span>{{item.user.name}}</span>
          <span class="order-text-tip">订单号码：{{item.orderNum}}</span>
        </div>
        <div class="order-toDeliver-product">
          <div class="order-toDeliver-product-item" v-for="(item, index) in item.product" :key="index">
            <img class="order-toDeliver-product-img">
            <div class="order-toDeliver-product-content">
              <div class="order-toDeliver-product-name">{{item.name}}</div>
              <div class="order-toDeliver-product-count">数量 ×{{item.count}}</div>
              <div class="order-toDeliver-product-price">￥{{item.price}}</div>
              <div class="order-toDeliver-product-status">待发货</div>
            </div>
          </div>
        </div>
        <div class="order-toDeliver-total">
          <span>商品共计{{item.product.length}}件</span>
          <span class="order-toDeliver-total-price">商品总价￥{{item.total}}</span>
        </div>
        <div class="order-toDeliver-detail">
          <div class="order-toDeliver-detail-content">
            <div>订单号码：{{item.orderNum}}</div>
            <div>订单时间：{{item.createTime}}</div>
            <div>订单备注：{{item.comment}}</div>
          </div>
          <div class="order-toDeliver-detail-copy">复制</div>
        </div>
      </div>
    </div>

    <div class="order-deliver" v-if="type == 2">
      <div class="order-deliver-time">
        <div>我的订单</div>
        <span>已发货</span>
        <div class="order-text-tip">预计到货时间：{{deliverTime}}</div>
      </div>
      <div class="order-deliver-item" v-if="item.status == 3" v-for="(item, index) in orderList" :key="index">
        <div class="order-deliver-btn" v-on:click="checkAll = !checkAll">全选</div>
        <div class="order-deliver-product-item" v-for="(item, index) in item.product" :key="item.id">
          <label :for="item.id">
            <div>
              <input class="order-deliver-product-checkbox" type="checkbox" :id="item.id" :checked="checkAll">
              <img class="order-deliver-product-img">
              <div class="order-deliver-product-content">
                <div class="order-deliver-product-name">{{item.name}}</div>
                <div class="order-deliver-product-count">数量 ×{{item.count}}</div>
              </div>
              <div class="order-deliver-product-price">￥{{item.price}}</div>
            </div>
          </label>
        </div>
        <div class="order-deliver-btn">一键收货</div>
        <div class="order-deliver-btn order-deliver-lack">缺货/少货</div>
        <div class="order-item">商品共计{{item.product.length}}件</div>
        <div class="order-item">商品总价￥{{item.total}}</div>
        <div class="order-deliver-detail">
          <div class="order-deliver-detail-content">
            <div>订单号码：{{item.orderNum}}</div>
            <div>订单时间：{{item.createTime}}</div>
            <div>支付方式：{{item.pay}}</div>
            <div>订单备注：{{item.comment}}</div>
          </div>
          <div class="order-deliver-detail-copy">复制</div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { Flexbox, FlexboxItem } from "vux";
import { Tab, TabItem } from "vux";

export default {
    name: "order",
    components: {
        Flexbox,
        FlexboxItem,
        Tab,
        TabItem
    },

    data: function() {
        return {
            type: 0,
            searchValue: "",
            checkAll: false,
            typeList: [
                "全部订单",
                "待发货",
                "发货中",
                "待提货",
                "售后中",
                "已完成"
            ],
            statusList: [
                "未支付",
                "待成团",
                "已支付",
                "配送中",
                "售后中",
                "已签收"
            ],
            deliverTime: "2018-08-27 10:00:00",
            toSendTime: "2018-08-28 10:00:00",
            toReceiveTime: "2018-08-30 10:00:00",
            orderList: [
                {
                    orderNum: "20180707185959",
                    createTime: "2018-07-07 18:59:59",
                    status: 2,
                    total: 32.5,
                    pay: "在线支付",
                    comment: "",
                    user: {
                        name: "莉莉",
                        phone: "18511323712",
                        wechat: "1843892973"
                    },
                    product: [
                        {
                            id: "000001",
                            name: "红心火龙果",
                            imgUrl: "",
                            price: 39.2,
                            count: 2
                        },
                        {
                            id: "000002",
                            name: "黄心火龙果",
                            imgUrl: "",
                            price: 39.2,
                            count: 2
                        }
                    ]
                },
                {
                    orderNum: "20180708185959",
                    createTime: "2018-07-08 18:59:59",
                    status: 3,
                    total: 32.5,
                    pay: "在线支付",
                    comment: "",
                    user: {
                        name: "莉莉",
                        phone: "18511323712",
                        wechat: "1843892973"
                    },
                    product: [
                        {
                            id: "000003",
                            name: "蓝心火龙果",
                            imgUrl: "",
                            price: 39.2,
                            count: 2
                        },
                        {
                            id: "000004",
                            name: "紫心火龙果",
                            imgUrl: "",
                            price: 39.2,
                            count: 2
                        }
                    ]
                }
            ]
        };
    },

    methods: {
        changeType(index) {
            this.type = index;
        },

        searchFor(value, searchStr) {
            var result = [];

            if (searchStr == "") {
                return value;
            }

            searchStr = searchStr.trim();

            result = value.filter(function(item) {
                if (item.orderNum.indexOf(searchStr) != -1) {
                    return item;
                } else if (item.user.name.indexOf(searchStr) != -1) {
                    return item;
                } else if (item.user.phone.indexOf(searchStr) != -1) {
                    return item;
                }
            });

            return result;
        }
    }
};
</script>

<style>
.order {
    font-size: 0.875rem /* 14/16 */;
}

.order-item {
    padding: 0 1.25rem /* 20/16 */;
}

.order-userInfo {
    width: 100%;
    height: 3.125rem /* 50/16 */;
    padding: 0.625rem /* 10/16 */;
    box-sizing: border-box;
    background: #ffffff;
    position: sticky;
    top: 0;
    z-index: 99;
}

.userInfo-avatar {
    width: 1.875rem /* 30/16 */;
    height: 1.875rem /* 30/16 */;
    border-radius: 50%;
    background: #fdedeb;
    display: inline-block;
}

.userInfo-name {
    font-size: 1.125rem /* 18/16 */;
    line-height: 1.875rem /* 30/16 */;
    margin: 0 0.625rem /* 10/16 */ 0 0.3125rem /* 5/16 */;
    vertical-align: top;
    display: inline-block;
}

.userInfo-label {
    height: 1.5rem /* 24/16 */;
    line-height: 1.5rem /* 24/16 */;
    margin: 0.1875rem /* 3/16 */ 0;
    padding: 0 0.3125rem /* 5/16 */;
    border: 1px solid #cccccc;
    border-radius: 0.3125rem /* 5/16 */;
    vertical-align: top;
    display: inline-block;
}

.order-flexbox {
    border-top: 1px solid #cccccc;
    border-bottom: 1px solid #cccccc;
    margin-bottom: 0.625rem /* 10/16 */;
}

.order-flexbox-item {
    text-align: center;
    padding: 0.625rem /* 10/16 */ !important;
}

.order-flexbox-item:first-child {
    border-right: 1px solid #cccccc;
}

.order-flexbox-label {
    height: 1.5rem /* 24/16 */;
    line-height: 1.5rem /* 24/16 */;
    margin: 0.1875rem /* 3/16 */ 0;
    padding: 0 0.9375rem /* 15/16 */;
    border: 1px solid #cccccc;
    border-radius: 0.75rem /* 12/16 */;
    vertical-align: top;
    display: inline-block;
}

.order-flexbox-count {
    color: #ffba00;
    font-size: 1.25rem /* 20/16 */;
    line-height: 3.125rem /* 50/16 */;
}

.order-search {
    height: 1.5rem /* 24/16 */;
    padding: 0 0.625rem /* 10/16 */;
    text-align: right;
    box-sizing: border-box;
    background: #ffffff;
    position: sticky;
    top: 3.0625rem /* 49/16 */;
    z-index: 99;
}

.order-search-icon {
    size: 1.5rem /* 24/16 */;
}

.order-search-input {
    height: 1.5rem /* 24/16 */;
    margin: 0;
    padding: 0 0.75rem /* 12/16 */;
    border: 1px solid #cccccc;
    border-radius: 0.75rem /* 12/16 */;
    vertical-align: top;
    box-sizing: border-box;
    outline: none;
}

.order-type {
    height: 2.75rem /* 44/16 */;
    background: #ffffff;
    position: sticky;
    top: 4.5625rem /* 73/16 */;
    z-index: 99;
}

.order-list-item {
    line-height: 1.5rem /* 24/16 */;
    margin-bottom: 1.25rem /* 20/16 */;
}

.order-head {
    padding: 0.3125rem /* 5/16 */ 0.625rem /* 10/16 */;
    border-bottom: 1px solid #cccccc;
}

.order-user {
    padding: 0.625rem /* 10/16 */ 1.25rem /* 20/16 */;
    display: inline-block;
}

.order-status {
    line-height: 1.5rem /* 24/16 */;
    margin: 2.125rem /* 34/16 */ 1.25rem /* 20/16 */;
    background: #ffba00;
    float: right;
}

.order-product-item {
    width: 100%;
    padding: 0.3125rem /* 5/16 */ 1.25rem /* 20/16 */;
    box-sizing: border-box;
}

.order-product-img {
    width: 5rem /* 80/16 */;
    height: 5rem /* 80/16 */;
    margin-right: 0.625rem /* 10/16 */;
}

.order-product-content {
    width: 9.375rem /* 150/16 */;
    display: inline-block;
    vertical-align: top;
    position: relative;
}

.order-product-name {
    height: 3.75rem /* 60/16 */;
    line-height: 1.875rem /* 30/16 */;
}

.order-product-price {
    height: 1.25rem /* 20/16 */;
    line-height: 1.25rem /* 20/16 */;
}

.order-product-count {
    width: 4.6875rem /* 75/16 */;
    height: 5rem /* 80/16 */;
    line-height: 2.5rem /* 40/16 */;
    text-align: center;
    vertical-align: top;
    display: inline-block;
}

.order-status-list {
    height: 1.875rem /* 30/16 */;
    font-size: 0.75rem /* 12/16 */;
    line-height: 1.875rem /* 30/16 */;
    padding: 0 1.25rem /* 20/16 */;
    border-top: 1px solid #cccccc;
    border-bottom: 1px solid #cccccc;
}

.order-status-item {
    width: 3.125rem /* 50/16 */;
    height: 1.875rem /* 30/16 */;
    text-align: center;
    display: inline-block;
    position: relative;
}

.order-status-active {
    width: 2.5rem /* 40/16 */;
    height: 1.25rem /* 20/16 */;
    background: #ffba00;
    position: absolute;
    top: 0.3125rem /* 5/16 */;
    left: 0.3125rem /* 5/16 */;
    z-index: -1;
}

.order-total {
    margin-right: 1.875rem /* 30/16 */;
    float: right;
}

.order-toDeliver-time,
.order-deliver-time {
    line-height: 1.5rem /* 24/16 */;
    padding: 0.3125rem /* 5/16 */ 1.25rem /* 20/16 */;
    border-bottom: 1px solid #cccccc;
    overflow: hidden;
}

.order-text-tip {
    color: #999999;
    float: right;
}

.order-toDeliver-item {
    margin-bottom: 1.25rem /* 20/16 */;
}

.order-toDeliver-info {
    line-height: 1.875rem /* 30/16 */;
    padding: 0 1.25rem /* 20/16 */;
    border-bottom: 1px solid #cccccc;
    overflow: hidden;
}

.order-toDeliver-product-item,
.order-deliver-product-item {
    width: 100%;
    height: 4.375rem /* 70/16 */;
    padding: 0.625rem /* 10/16 */ 1.25rem /* 20/16 */;
    padding-right: 0;
    box-sizing: border-box;
    border-bottom: 1px solid #cccccc;
}

.order-toDeliver-product-img {
    width: 3.125rem /* 50/16 */;
    height: 3.125rem /* 50/16 */;
    margin-right: 0.625rem /* 10/16 */;
    border-radius: 0.625rem /* 10/16 */;
}

.order-toDeliver-product-content,
.order-deliver-product-content {
    line-height: 1.5625rem /* 25/16 */;
    display: inline-block;
    vertical-align: top;
}

.order-toDeliver-product-count,
.order-toDeliver-product-price,
.order-toDeliver-product-status {
    width: 5.625rem /* 90/16 */;
    display: inline-block;
    vertical-align: top;
}

.order-toDeliver-product-price,
.order-toDeliver-product-status {
    text-align: center;
}

.order-toDeliver-total {
    height: 1.875rem /* 30/16 */;
    line-height: 1.875rem /* 30/16 */;
    padding: 0 1.875rem /* 30/16 */;
    box-sizing: border-box;
}

.order-toDeliver-total-price {
    float: right;
}

.order-toDeliver-detail,
.order-deliver-detail {
    line-height: 1.5rem /* 24/16 */;
    padding: 0.3125rem /* 5/16 */ 1.875rem /* 30/16 */;
    box-sizing: border-box;
    border-bottom: 1px solid #cccccc;
}

.order-toDeliver-detail-content,
.order-deliver-detail-content {
    display: inline-block;
}

.order-toDeliver-detail-copy,
.order-deliver-detail-copy {
    padding: 0 0.625rem /* 10/16 */;
    border: 1px solid #cccccc;
    float: right;
}

.order-deliver-btn {
    width: 70px;
    text-align: center;
    line-height: 1.5rem /* 24/16 */;
    margin: 0.3125rem /* 5/16 */ 1.25rem /* 20/16 */;
    border: 1px solid #cccccc;
    border-radius: 0.3125rem /* 5/16 */;
    background: #ffba00;
    display: inline-block;
}

.order-deliver-product-item {
    border-top: 1px solid #cccccc;
    padding-right: 1.25rem /* 20/16 */;
}

.order-deliver-product-checkbox {
    width: 1.25rem /* 20/16 */;
    height: 1.25rem /* 20/16 */;
    margin: 0.9375rem /* 15/16 */ 0;
    vertical-align: top;
    outline: none;
}

.order-deliver-product-img {
    width: 3.125rem /* 50/16 */;
    height: 3.125rem /* 50/16 */;
    margin: 0 0.625rem /* 10/16 */;
    border-radius: 0.625rem /* 10/16 */;
}

.order-deliver-product-price,
.order-deliver-lack {
    float: right;
}

.order-deliver-detail {
    padding: 0.3125rem /* 5/16 */ 1.25rem /* 20/16 */;
}
</style>
