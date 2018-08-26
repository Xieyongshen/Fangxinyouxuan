<template>
    <div class="manage">

        <div class="manage-head">
            <img src="@/assets/ic_user.png" class="icon-user">
            <div class="manage-head-username">{{username}}</div>
            <div class="manage-head-identity">{{identity}}</div>
            <div class="manage-head-selector">
                <group>
                    <PopupRadio @on-hide="onhide" title="" placeholder="在线商品" v-model="productStatusSelected" :options="productStatusList"></PopupRadio>
                </group>
            </div>
        </div>

        <div class="manage-list">
            <div class="manage-list-title">
                <span>{{productStatusSelected}}</span>
                <div class="manage-search">
                    <x-icon type="ios-search-strong" class="manage-search-icon"></x-icon>
                    <input type="text" placeholder="商品" class="manage-search-input" v-model="searchValue">
                </div>
            </div>
            <div class="manage-list-label">
                <div class="manage-list-label-item manage-list-label-rebate">每单返利</div>
                <div class="manage-list-label-item">价格</div>
                <div class="manage-list-label-item">库存</div>
            </div>
            <checker v-model="productSelected" type="checkbox" default-item-class="manage-list-item-selector" selected-item-class="manage-list-item-selector-selected">
                <div class="manage-list-item" v-for="item in searchFor(items, searchValue)" :key="item.number">
                    <checker-item :value="item.number"></checker-item>
                    <img class="img-product">
                    <div class="manage-list-item-productName">{{item.productName}}</div>
                    <div class="manage-list-item-productRebate">{{item.productRebate}}</div>
                    <div class="manage-list-item-productPrice">￥{{item.productPrice}}</div>
                    <div class="manage-list-item-productAmount">{{item.productAmount}}</div>
                    <div class="manage-list-item-productStatus">{{item.productStatus}}</div>
                </div>
                <div class="button-more">
                    <XButton @click.native="viewmore" mini>查看更多</XButton>
                </div>
                <div class="manage-list-tollbar">
                    <checker-item :value="-1"></checker-item>
                    <div class="manage-selectAll">全选</div>
                    <div class="button-option">
                        <XButton mini type="primary">{{productOption}}</XButton>
                    </div>
                </div>
            </checker>
        </div>

    </div>
</template>

<script>
import { PopupRadio, Checker, CheckerItem, XButton } from "vux";

export default {
    name: "manage",
    components: {
        PopupRadio,
        Checker,
        CheckerItem,
        XButton
    },

    data: function() {
        return {
            username: "青冥",
            identity: "小区店长",
            productStatusChoose: 0,
            productStatusSelected: "在线商品",
            productStatusList: ["在线商品", "下架商品", "缺货商品", "全部商品"],
            productOption: "申请下架",
            productOptionList: ["申请下架", "申请上架", "心愿单", ""],
            searchValue: "",
            items: [
                {
                    number: "1",
                    productName: "商品1",
                    productRebate: "10%",
                    productPrice: "10.0",
                    productAmount: "666",
                    productStatus: "在线"
                },
                {
                    number: "2",
                    productName: "商品2",
                    productRebate: "10%",
                    productPrice: "10.0",
                    productAmount: "666",
                    productStatus: "在线"
                },
                {
                    number: "3",
                    productName: "商品3",
                    productRebate: "10%",
                    productPrice: "10.0",
                    productAmount: "666",
                    productStatus: "在线"
                },
                {
                    number: "4",
                    productName: "商品4",
                    productRebate: "10%",
                    productPrice: "10.0",
                    productAmount: "666",
                    productStatus: "在线"
                },
                {
                    number: "5",
                    productName: "商品5",
                    productRebate: "10%",
                    productPrice: "10.0",
                    productAmount: "666",
                    productStatus: "在线"
                },
                {
                    number: "6",
                    productName: "商品6",
                    productRebate: "10%",
                    productPrice: "10.0",
                    productAmount: "666",
                    productStatus: "在线"
                },
                {
                    number: "7",
                    productName: "商品7",
                    productRebate: "10%",
                    productPrice: "10.0",
                    productAmount: "666",
                    productStatus: "在线"
                },
                {
                    number: "8",
                    productName: "商品8",
                    productRebate: "10%",
                    productPrice: "10.0",
                    productAmount: "666",
                    productStatus: "在线"
                },
                {
                    number: "9",
                    productName: "商品9",
                    productRebate: "10%",
                    productPrice: "10.0",
                    productAmount: "666",
                    productStatus: "在线"
                },
                {
                    number: "10",
                    productName: "商品10",
                    productRebate: "10%",
                    productPrice: "10.0",
                    productAmount: "666",
                    productStatus: "在线"
                }
            ],
            productSelected: ""
        };
    },

    methods: {
        viewmore() {},

        searchFor(value, searchStr) {
            var result = [];

            if (searchStr == "") {
                return value;
            }

            searchStr = searchStr.trim();

            result = value.filter(function(item) {
                if (item.productName.indexOf(searchStr) != -1) {
                    return item;
                }
            });

            return result;
        }
    }
};
</script>

<style scoped>
.divider {
    color: #888888;
    line-height: 1px;
    margin: 1.25rem 0.9375rem;
}

.manage {
    display: flex;
    flex-direction: column;
}

.manage-head {
    display: flex;
    align-items: center;
    width: 100%;
    height: 3.125rem /* 50/16 */;
    padding: 0.625rem /* 10/16 */;
    border-bottom: 1px solid #cccccc;
    box-sizing: border-box;
    background: #ffffff;
    position: relative;
}

.icon-user {
    width: 1.875rem /* 30/16 */;
    height: 1.875rem /* 30/16 */;
}

.manage-head-username {
    font-size: 0.875rem /* 14/16 */;
    line-height: 1.875rem /* 30/16 */;
    margin: 0 0.625rem /* 10/16 */ 0 0.3125rem /* 5/16 */;
    vertical-align: top;
    display: inline-block;
}

.manage-head-identity {
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

.manage-head-selector {
    position: absolute;
    bottom: 0;
    right: 0;
    z-index: 98;
}

.manage-list {
    display: flex;
    flex-direction: column;
    margin: 0 0.625rem /* 10/16 */;
}

.manage-list-title {
    font-size: 1rem /* 16/16 */;
    text-align: center;
    padding: 0.3125rem /* 5/16 */ 0;
    position: relative;
}

.manage-search {
    height: 1.5rem /* 24/16 */;
    text-align: right;
    box-sizing: border-box;
    position: absolute;
    right: 0;
    top: 0.4375rem /* 7/16 */;
}

.manage-search-icon {
    size: 1.5rem /* 24/16 */;
}

.manage-search-input {
    width: 6.25rem /* 100/16 */;
    height: 1.5rem /* 24/16 */;
    margin: 0;
    padding: 0 0.75rem /* 12/16 */;
    border: 1px solid #cccccc;
    border-radius: 0.75rem /* 12/16 */;
    vertical-align: top;
    box-sizing: border-box;
    outline: none;
}

.manage-list-label {
    width: 9.375rem /* 150/16 */;
    margin-top: 0.9375rem;
    margin-left: 9.375rem /* 150/16 */;
    display: flex;
    justify-content: space-between;
}

.manage-list-label-item {
    width: 3.125rem /* 50/16 */;
    font-size: 0.875rem /* 14/16 */;
    white-space: nowrap;
    text-align: center;
}

.manage-list-label-rebate {
    position: relative;
    right: 0.5rem /* 8/16 */;
}

.manage-list-item {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.625rem /* 10/16 */;
}

.manage-list-item-productStatus {
    font-size: 0.875rem /* 14/16 */;
    padding: 0 0.625rem;
    border: 1px solid;
    border-radius: 0.5rem;
}

.manage-list-item-selector {
    width: 1.25rem /* 20/16 */;
    height: 1.25rem /* 20/16 */;
    border: 1px solid #ccc;
    display: inline-block;
    border-radius: 50%;
    line-height: 2.5rem;
    text-align: center;
}

.manage-list-item-selector-selected {
    background-color: #1aad19;
}

.img-product {
    width: 2.5rem /* 40/16 */;
    height: 2.5rem /* 40/16 */;
    margin: 0 0.3125rem /* 5/16 */;
    border-radius: 0.625rem /* 10/16 */;
}

.manage-list-item-productName {
    width: 3.75rem /* 60/16 */;
    font-size: 0.875rem /* 14/16 */;
    text-align: center;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
}

.manage-list-item-productRebate,
.manage-list-item-productPrice,
.manage-list-item-productAmount {
    width: 3.125rem /* 50/16 */;
    font-size: 0.875rem /* 14/16 */;
    text-align: center;
}

.manage-list-tollbar {
    display: flex;
    flex-direction: row;
    align-items: center;
    line-height: 1.875rem /* 30/16 */;
    margin-top: 0.625rem /* 10/16 */;
    padding: 0.625rem /* 10/16 */ 0;
}

.manage-selectAll {
    font-size: 0.875rem /* 14/16 */;
    margin-left: 0.625rem /* 10/16 */;
}

.button-option {
    margin: 0 1.25rem;
}

.button-more {
    position: relative;
    left: 40%;
}
</style>