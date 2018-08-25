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
                <div class="order-flexbox-count">
                    <countup :start-val="1" :end-val="8888" :duration="1"></countup>单</div>
            </flexbox-item>
            <flexbox-item class="order-flexbox-item">
                <div class="order-flexbox-label">今日销售额</div>
                <div class="order-flexbox-count">￥
                    <countup :start-val="1" :end-val="888.88" :decimals="2" :duration="1"></countup>
                </div>
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
                    <span>客户：{{item.user.name}}</span>
                    <div class="order-status">{{statusList[item.status]}}</div>
                    <div class="order-info-detail">
                        <span class="order-product-info" v-for="(item, index) in item.product" :key="item.id">{{item.name}}×{{item.count}}</span>
                        <div class="order-info-more">
                            <div class="order-info-more-title">详情</div>
                            <x-icon type="ios-arrow-down" size="20" class="order-info-more-icon"></x-icon>
                        </div>
                    </div>
                </div>
                <div class="order-detail">
                    <div>电话：{{item.user.phone}}</div>
                    <div>微信号：{{item.user.wechat}}</div>
                    <div class="order-product-item" v-for="(item, index) in item.product" :key="item.id">
                        <div class="order-product-name">{{item.name}}</div>
                        <img class="order-product-img">
                        <div class="order-product-price">价格<br>￥{{item.price}}</div>
                        <div class="order-product-multiply">×</div>
                        <div class="order-product-count">数量<br>{{item.count}}</div>
                    </div>
                    <div class="order-total">共计￥{{item.total}}</div>
                </div>
            </div>
        </div>

        <div class="order-toDeliver" v-if="type == 1">
            <div class="order-toDeliver-count">
                <span>待发货订单共计：{{toDeliverOrderList.length}}</span>
                <span>快递发货共计：{{toDeliverOrderCount[0]}}</span>
                <span>到店自提共计：{{toDeliverOrderCount[1]}}</span>
                <span>配送到家共计：{{toDeliverOrderCount[2]}}</span>
            </div>
            <div class="order-toDeliver-item" v-for="(item, index) in orderList" v-if="item.status == 1" :key="index">
                <div class="order-toDeliver-info">
                    <div>
                        <span>{{item.user.name}}</span>
                        <span class="order-text-tip">订单号码：{{item.orderNum}}</span>
                    </div>
                    <div>
                        <span>{{item.type == 2 ? '拼团款' : ''}}{{item.type == 4 ? '预售款' : ''}}</span>
                        <span class="order-text-tip">预计发货：{{toSendTime}}</span>
                    </div>
                    <div>
                        <span>{{item.deliver.name}}</span>
                        <span class="order-text-tip">预计到货：{{toReceiveTime}}</span>
                    </div>
                </div>
                <div class="order-toDeliver-total">
                    <span>商品共计{{item.product.length}}件</span>
                    <span class="order-toDeliver-info-more">
                        <div class="order-info-more-title">详情</div>
                        <x-icon type="ios-arrow-down" size="20" class="order-info-more-icon"></x-icon>
                    </span>
                    <span class="order-toDeliver-total-price">商品总价￥{{item.total}}</span>
                </div>
                <div class="order-toDeliver-detail">
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
                    <div class="order-toDeliver-detailInfo">
                        <span>
                            <div>订单号码：{{item.orderNum}}</div>
                            <div>订单时间：{{item.createTime}}</div>
                            <div>配送方式：
                                <div v-for="(deliver, index) in deliverList" class="order-toDeliver-detail-deliverItem">
                                    <span v-if="deliver != item.deliver.name">{{deliver}}</span>
                                    <span v-if="deliver == item.deliver.name" class="deliver-active">{{deliver}}</span>
                                </div>
                            </div>
                            <div>快递单号：{{item.orderNum}}</div>
                            <div>订单备注：{{item.comment}}</div>
                        </span>
                        <div class="order-toDeliver-detail-copy">复制</div>
                    </div>
                </div>
            </div>
        </div>

        <div class="order-deliver" v-if="type == 2">
            <div class="order-deliver-count">
                <span>到店订单共计：{{deliverOrderList.length}}</span>
                <span>快递发货共计：{{deliverOrderCount[0]}}</span>
                <span>到店自提共计：{{deliverOrderCount[1]}}</span>
                <span>配送到家共计：{{deliverOrderCount[2]}}</span>
            </div>
            <div class="order-deliver-info">
                <div>本店今日到货商品</div>
                <div>
                    <span>已发货</span>
                    <div class="order-text-tip">预计到货时间：{{deliverTime}}</div>
                </div>
            </div>
            <div class="order-deliver-btn" v-on:click="checkAll = !checkAll">全选</div>
            <div class="order-deliver-product-item" v-for="(item, index) in deliverProductList" :key="index">
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
            <div class="order-item">商品共计{{deliverProductList.length}}件</div>
            <div class="order-item">商品总价￥{{deliverOrderTotal}}</div>
        </div>

        <div class="order-toReceive" v-if="type == 3">
            <div class="order-toReceive-count">
                <span>待签收订单共计：{{toReceiveOrderList.length}}</span>
                <span>快递发货共计：{{toReceiveOrderCount[0]}}</span>
                <span>到店自提共计：{{toReceiveOrderCount[1]}}</span>
                <span>配送到家共计：{{toReceiveOrderCount[2]}}</span>
            </div>
            <div class="order-toReceive-item" v-for="(item, index) in orderList" v-if="item.status == 3" :key="index">
                <div class="order-toReceive-info">
                    <div>
                        <span>{{item.user.name}}</span>
                        <span class="order-text-tip">订单号码：{{item.orderNum}}</span>
                    </div>
                    <div>
                        <span>{{item.deliver.name}}</span>
                        <span class="order-text-tip">预计到货：{{toReceiveTime}}</span>
                    </div>
                </div>
                <div class="order-toReceive-total">
                    <span>商品共计{{item.product.length}}件</span>
                    <span class="order-toReceive-info-more">
                        <div class="order-info-more-title">详情</div>
                        <x-icon type="ios-arrow-down" size="20" class="order-info-more-icon"></x-icon>
                    </span>
                    <span class="order-toReceive-total-price">商品总价￥{{item.total}}</span>
                </div>
                <div class="order-toReceive-detail">
                    <div>电话：{{item.user.phone}}</div>
                    <div>微信号：{{item.user.wechat}}</div>
                    <div class="order-toReceive-product">
                        <div class="order-toReceive-product-item" v-for="(item, index) in item.product" :key="index">
                            <img class="order-toReceive-product-img">
                            <div class="order-toReceive-product-content">
                                <div class="order-toReceive-product-name">{{item.name}}</div>
                                <div class="order-toReceive-product-count">数量 ×{{item.count}}</div>
                            </div>
                            <div class="order-toReceive-product-price">￥{{item.price}}</div>
                        </div>
                    </div>
                    <div class="order-toReceive-detailInfo">
                        <span>
                            <div>订单号码：{{item.orderNum}}</div>
                            <div>订单时间：{{item.createTime}}</div>
                            <div>配送方式：
                                <div v-for="(deliver, index) in deliverList" class="order-toReceive-detail-deliverItem">
                                    <span v-if="deliver != item.deliver.name">{{deliver}}</span>
                                    <span v-if="deliver == item.deliver.name" class="deliver-active">{{deliver}}</span>
                                </div>
                            </div>
                            <div>快递单号：{{item.orderNum}}</div>
                            <div>订单备注：{{item.comment}}</div>
                        </span>
                        <div class="order-toReceive-detail-copy">复制</div>
                    </div>
                </div>
            </div>
        </div>

        <div class="order-return" v-if="type == 4">
            <div class="order-return-item" v-for="(item, index) in orderList" v-if="item.status == 4" :key="index">
                <div>单号：{{item.orderNum}}</div>
                <div>{{item.user.name}}</div>
                <div>审批完成后12h内退回原账户，如有疑问请询问客服</div>
                <div class="order-return-product">
                    <div class="order-return-product-item" v-for="(item, index) in item.product" :key="index">
                        <img class="order-return-product-img">
                        <div class="order-return-product-content">
                            <div class="order-return-product-name">{{item.name}}</div>
                            <div class="order-return-product-count">数量 ×{{item.count}}</div>
                        </div>
                        <div class="order-return-product-price">￥{{item.price}}</div>
                    </div>
                </div>
            </div>
        </div>

        <div class="order-complete" v-if="type == 5">
            <div class="order-complete-item" v-for="(item, index) in orderList" v-if="item.status == 5" :key="index">
                <div class="order-complete-info">
                    <span>{{item.createTime}}</span>
                    <div class="order-text-tip">单号：{{item.orderNum}}</div>
                </div>
                <div class="order-complete-detail">
                    <span>{{item.user.name}}</span>
                    <div class="order-complete-status order-status">已完成</div>
                    <div class="order-complete-product">
                        <div class="order-complete-product-item" v-for="(item, index) in item.product" :key="index">
                            <div class="order-complete-product-name">{{item.name}}</div>
                            <div class="order-complete-product-count">×  {{item.count}}</div>
                            <div class="order-complete-product-price">￥{{item.price}}</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { Flexbox, FlexboxItem } from "vux";
import { Countup } from "vux";
import { Tab, TabItem } from "vux";
import { CheckIcon } from "vux";

export default {
    name: "order",
    components: {
        Flexbox,
        FlexboxItem,
        Countup,
        Tab,
        TabItem,
        CheckIcon
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
                "待签收",
                "售后中",
                "已完成"
            ],
            statusList: [
                "未支付",
                "待发货",
                "已支付",
                "配送中",
                "售后中",
                "已签收"
            ],
            deliverList: ["快递发货", "到店自提", "配送到家"],
            deliverTime: "2018-08-27 10:00:00",
            toSendTime: "2018-08-28 10:00:00",
            toReceiveTime: "2018-08-30 10:00:00",
            orderList: [
                {
                    orderNum: "20180707185959",
                    createTime: "2018-07-07 18:59:59",
                    type: 2,
                    status: 1,
                    total: 32.5,
                    pay: "在线支付",
                    deliver: {
                        name: "快递发货"
                    },
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
                    type: 4,
                    status: 3,
                    total: 32.5,
                    pay: "在线支付",
                    deliver: {
                        name: "配送到家"
                    },
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
                },
                {
                    orderNum: "20180708185959",
                    createTime: "2018-07-08 18:59:59",
                    type: 4,
                    status: 3,
                    total: 32.5,
                    pay: "在线支付",
                    deliver: {
                        name: "配送到家"
                    },
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
                            id: "000005",
                            name: "绿心火龙果",
                            imgUrl: "",
                            price: 39.2,
                            count: 2
                        }
                    ]
                },
                {
                    orderNum: "20180708185959",
                    createTime: "2018-07-08 18:59:59",
                    type: 0,
                    status: 4,
                    total: 32.5,
                    pay: "在线支付",
                    deliver: {
                        name: "配送到家"
                    },
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
                            id: "000005",
                            name: "绿心火龙果",
                            imgUrl: "",
                            price: 39.2,
                            count: 2
                        }
                    ]
                },
                {
                    orderNum: "20180708185959",
                    createTime: "2018-07-08 18:59:59",
                    type: 0,
                    status: 5,
                    total: 32.5,
                    pay: "在线支付",
                    deliver: {
                        name: "配送到家"
                    },
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
                            id: "000005",
                            name: "绿心火龙果",
                            imgUrl: "",
                            price: 39.2,
                            count: 2
                        }
                    ]
                }
            ]
        };
    },

    computed: {
        toDeliverOrderList() {
            var list = [];
            this.orderList.forEach(element => {
                if (element.status == 1) {
                    list.push(element);
                }
            });
            return list;
        },

        toDeliverOrderCount() {
            var countI = 0;
            var countII = 0;
            var countIII = 0;
            var self = this;
            self.orderList.forEach(element => {
                if (
                    element.status == 1 &&
                    element.deliver.name == self.deliverList[0]
                ) {
                    countI++;
                } else if (
                    element.status == 1 &&
                    element.deliver.name == self.deliverList[1]
                ) {
                    countII++;
                } else if (
                    element.status == 1 &&
                    element.deliver.name == self.deliverList[2]
                ) {
                    countIII++;
                }
            });
            return [countI, countII, countIII];
        },

        deliverOrderList() {
            var list = [];
            this.orderList.forEach(element => {
                if (element.status == 3) {
                    list.push(element);
                }
            });
            return list;
        },

        deliverOrderCount() {
            var countI = 0;
            var countII = 0;
            var countIII = 0;
            var self = this;
            self.orderList.forEach(element => {
                if (
                    element.status == 3 &&
                    element.deliver.name == self.deliverList[0]
                ) {
                    countI++;
                } else if (
                    element.status == 3 &&
                    element.deliver.name == self.deliverList[1]
                ) {
                    countII++;
                } else if (
                    element.status == 3 &&
                    element.deliver.name == self.deliverList[2]
                ) {
                    countIII++;
                }
            });
            return [countI, countII, countIII];
        },

        deliverProductList() {
            var self = this;
            var list = [];
            var count = 0;
            self.orderList.forEach(element => {
                if (element.status == 3) {
                    element.product.forEach(pro => {
                        list.push(pro);
                    });
                }
            });

            list.forEach((element, idx) => {
                list.forEach((item, index) => {
                    if (idx < index && element.id == item.id) {
                        element.count += item.count;
                        list.splice(index, 1);
                    }
                });
            });

            return list;
        },

        deliverOrderTotal() {
            var self = this;
            var total = 0;
            var cur = 0;
            self.deliverProductList.forEach(element => {
                cur = element.price * 100;
                cur = parseInt(cur) * element.count;
                total += cur;
            });

            return total / 100;
        },

        toReceiveOrderList() {
            var list = [];
            this.orderList.forEach(element => {
                if (element.status == 3) {
                    list.push(element);
                }
            });
            return list;
        },

        toReceiveOrderCount() {
            var countI = 0;
            var countII = 0;
            var countIII = 0;
            var self = this;
            self.orderList.forEach(element => {
                if (
                    element.status == 3 &&
                    element.deliver.name == self.deliverList[0]
                ) {
                    countI++;
                } else if (
                    element.status == 3 &&
                    element.deliver.name == self.deliverList[1]
                ) {
                    countII++;
                } else if (
                    element.status == 3 &&
                    element.deliver.name == self.deliverList[2]
                ) {
                    countIII++;
                }
            });
            return [countI, countII, countIII];
        }
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
    line-height: 1.875rem /* 30/16 */;
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
    margin: 0 0.3125rem /* 5/16 */;
    vertical-align: top;
    display: inline-block;
}

.userInfo-label {
    height: 1.25rem /* 20/16 */;
    font-size: 0.75rem /* 12/16 */;
    line-height: 1.25rem /* 20/16 */;
    margin: 0.3125rem /* 5/16 */ 0;
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
    position: sticky;
    top: 0.8125rem /* 13/16 */;
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
    top: 3.0625rem /* 49/16 */;
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

.order-info {
    line-height: 1.875rem /* 30/16 */;
    padding: 0.625rem /* 10/16 */ 1.25rem /* 20/16 */ 0 1.25rem /* 20/16 */;
    border-bottom: 1px solid #cccccc;
}

.order-status {
    line-height: 1.5rem /* 24/16 */;
    margin-top: 0.1875rem /* 3/16 */;
    background: #ffba00;
    float: right;
}

.order-info-detail {
    padding-right: 5rem /* 80/16 */;
    position: relative;
}

.order-product-info {
    margin-right: 1.25rem /* 20/16 */;
}

.order-info-more {
    position: absolute;
    right: 0;
    bottom: 0;
}

.order-info-more-title {
    color: #999999;
    display: inline-block;
    vertical-align: top;
}

.order-info-more-icon {
    margin-top: 0.3125rem /* 5/16 */;
    vertical-align: top;
}

.order-detail,
.order-toDeliver-detail,
.order-toReceive-detail {
    padding: 0.3125rem /* 5/16 */ 1.25rem /* 20/16 */;
    border-bottom: 1px solid #cccccc;
}

.order-product-item {
    width: 100%;
    padding: 0.3125rem /* 5/16 */ 0;
    box-sizing: border-box;
}

.order-product-name {
    line-height: 1.5rem /* 24/16 */;
    margin-bottom: 0.3125rem /* 5/16 */;
    margin-left: 0.3125rem /* 5/16 */;
}

.order-product-img {
    width: 5rem /* 80/16 */;
    height: 5rem /* 80/16 */;
    margin-right: 1.25rem /* 20/16 */;
}

.order-product-price {
    height: 5rem /* 80/16 */;
    line-height: 2.5rem /* 40/16 */;
    padding: 0 1.875rem /* 30/16 */;
    text-align: center;
    vertical-align: top;
    display: inline-block;
}

.order-product-multiply {
    height: 5rem /* 80/16 */;
    line-height: 5rem /* 80/16 */;
    text-align: center;
    vertical-align: top;
    display: inline-block;
}

.order-product-count {
    height: 5rem /* 80/16 */;
    line-height: 2.5rem /* 40/16 */;
    padding: 0 1.875rem /* 30/16 */;
    text-align: center;
    vertical-align: top;
    display: inline-block;
}

.order-total {
    text-align: right;
}

.order-toDeliver-count,
.order-deliver-count,
.order-toReceive-count {
    padding: 0.3125rem /* 5/16 */ 1.25rem /* 20/16 */;
}

.order-deliver-count {
    border-bottom: 1px solid #cccccc;
}

.order-toDeliver-count span,
.order-deliver-count span,
.order-toReceive-count span {
    width: 9.6875rem /* 155/16 */;
    display: inline-block;
}

.order-text-tip {
    color: #999999;
    float: right;
}

.order-toDeliver-item,
.order-toReceive-item {
    border-top: 1px solid #cccccc;
    margin-bottom: 1.25rem /* 20/16 */;
}

.order-toDeliver-info,
.order-toReceive-info {
    line-height: 1.875rem /* 30/16 */;
    padding: 0 1.25rem /* 20/16 */;
    overflow: hidden;
}

.order-toDeliver-total,
.order-toReceive-total {
    height: 1.875rem /* 30/16 */;
    line-height: 1.875rem /* 30/16 */;
    padding: 0 1.25rem /* 20/16 */;
    box-sizing: border-box;
    border-bottom: 1px solid #cccccc;
}

.order-toDeliver-total-price,
.order-toDeliver-info-more,
.order-toReceive-total-price,
.order-toReceive-info-more {
    margin-left: 0.625rem /* 10/16 */;
    float: right;
}

.order-toDeliver-product-item,
.order-deliver-product-item,
.order-toReceive-product-item,
.order-return-product-item {
    width: 100%;
    height: 4.375rem /* 70/16 */;
    padding: 0.625rem /* 10/16 */ 0;
    padding-right: 0;
    box-sizing: border-box;
}

.order-toDeliver-product-item {
    margin-right: -1.25rem /* 20/16 */;
}

.order-toDeliver-product-img,
.order-toReceive-product-img,
.order-return-product-img {
    width: 3.125rem /* 50/16 */;
    height: 3.125rem /* 50/16 */;
    margin-right: 0.625rem /* 10/16 */;
    border-radius: 0.625rem /* 10/16 */;
}

.order-toDeliver-product-content,
.order-deliver-product-content,
.order-toReceive-product-content,
.order-return-product-content {
    line-height: 1.5625rem /* 25/16 */;
    display: inline-block;
    vertical-align: top;
}

.order-toDeliver-product-count,
.order-toDeliver-product-price,
.order-toDeliver-product-status {
    width: 5rem /* 80/16 */;
    display: inline-block;
    vertical-align: top;
}

.order-toDeliver-product-price {
    text-align: center;
}

.order-toDeliver-product-status {
    text-align: right;
}

.order-toDeliver-detailInfo,
.order-toReceive-detailInfo {
    line-height: 1.875rem /* 30/16 */;
    padding: 0.3125rem /* 5/16 */ 0;
    box-sizing: border-box;
    position: relative;
}

.order-toDeliver-detail-deliverItem,
.order-toReceive-detail-deliverItem {
    display: inline-block;
}

.order-toDeliver-detail-deliverItem span,
.order-toReceive-detail-deliverItem span {
    height: 1.5rem /* 24/16 */;
    line-height: 1.5rem /* 24/16 */;
    margin: 0.1875rem /* 3/16 */ 0;
    padding: 0 0.625rem /* 10/16 */;
    border-radius: 0.3125rem /* 5/16 */;
    display: inline-block;
}

.deliver-active {
    background: #f5333f;
    color: #ffffff;
}

.order-toDeliver-detail-copy,
.order-deliver-detail-copy,
.order-toReceive-detail-copy {
    padding: 0 0.625rem /* 10/16 */;
    border: 1px solid #cccccc;
    position: absolute;
    right: 1.25rem /* 20/16 */;
    top: 0.3125rem /* 5/16 */;
}

.order-deliver-info {
    line-height: 1.875rem /* 30/16 */;
    padding: 0 1.25rem /* 20/16 */;
}

.order-deliver-btn {
    width: 70px;
    text-align: center;
    font-size: 0.75rem /* 12/16 */;
    line-height: 1.5rem /* 24/16 */;
    margin: 0.3125rem /* 5/16 */ 1.25rem /* 20/16 */;
    border: 1px solid #cccccc;
    border-radius: 0.3125rem /* 5/16 */;
    background: #ffba00;
    display: inline-block;
}

.order-deliver-product-item {
    padding: 0.625rem /* 10/16 */ 1.25rem /* 20/16 */;
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
.order-deliver-lack,
.order-toReceive-product-price,
.order-return-product-price {
    float: right;
}

.order-deliver-detail {
    padding: 0.3125rem /* 5/16 */ 1.25rem /* 20/16 */;
}

.order-return-item {
    line-height: 1.5rem /* 24/16 */;
    padding: 0.3125rem /* 5/16 */ 1.25rem /* 20/16 */;
    border-bottom: 1px solid #cccccc;
}

.order-complete-info,
.order-complete-detail {
    line-height: 1.875rem /* 30/16 */;
    padding: 0 1.25rem /* 20/16 */;
    border-bottom: 1px solid #cccccc;
}

.order-complete-status{
    margin-right: 1.5625rem /* 25/16 */;
}

.order-complete-product-name,
.order-complete-product-count,
.order-complete-product-price {
    width: 6.25rem /* 100/16 */;
    display: inline-block;
    vertical-align: top;
}

.order-complete-product-count {
    text-align: center;
}

.order-complete-product-price {
    text-align: right;
}
</style>
