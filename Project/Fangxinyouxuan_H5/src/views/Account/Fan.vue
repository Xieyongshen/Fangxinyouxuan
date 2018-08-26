<template>
    <div class="fan">
        <user-info></user-info>

        <div class="fan-order">
            <group>
                <PopupRadio title="用户筛选排序" placeholder="本月消费top10用户" v-model="fanOrder" :options="fanOrderList"></PopupRadio>
            </group>
        </div>

        <div class="fan-list">
            <div class="fan-list-item" v-for="item in items" :key="item.number">
                <div class="fan-list-item-content">
                    <div class="fan-list-item-number">{{item.number}}</div>
                    <img src="@/assets/ic_user.png" class="icon-user">

                    <div class="fan-list-item-userinfo">
                        <div class="fan-list-userinfo-baseinfo">
                            <div class="fan-list-userinfo-name">{{item.name}}</div>
                            <div class="fan-list-userinfo-sex">{{item.sex}}</div>
                        </div>
                        <div class="fan-list-userinfo-cost">本月消费: {{item.cost}}</div>
                    </div>
                    <div class="fan-list-item-contact">
                        <div class="fan-list-userinfo-wechat">微信: {{item.wechat}}</div>
                        <div class="fan-list-userinfo-tel">电话: {{item.tel}}</div>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import userInfo from "@/components/userInfo.vue";
import { PopupRadio } from "vux";

export default {
    name: "fan",
    components: {
        userInfo,
        PopupRadio
    },

    data: function() {
        return {
            fanOrder: "",
            fanOrderList: [
                { key: "0", value: "本月消费top10用户" },
                { key: "1", value: "本周消费top10用户" },
                { key: "2", value: "累计消费排名" }
            ],
            items: [
                {
                    number: "1",
                    name: "小花",
                    sex: "女",
                    wechat: "xiaohuazuimei",
                    cost: "999",
                    tel: "13006666666"
                },
                {
                    number: "2",
                    name: "小花",
                    sex: "女",
                    wechat: "xiaohuazuimei",
                    cost: "999",
                    tel: "13006666666"
                },
                {
                    number: "3",
                    name: "小花",
                    sex: "女",
                    wechat: "xiaohuazuimei",
                    cost: "999",
                    tel: "13006666666"
                },
                {
                    number: "4",
                    name: "小花",
                    sex: "女",
                    wechat: "xiaohuazuimei",
                    cost: "999",
                    tel: "13006666666"
                },
                {
                    number: "5",
                    name: "小花",
                    sex: "女",
                    wechat: "xiaohuazuimei",
                    cost: "999",
                    tel: "13006666666"
                },
                {
                    number: "6",
                    name: "小花",
                    sex: "女",
                    wechat: "xiaohuazuimei",
                    cost: "999",
                    tel: "13006666666"
                },
                {
                    number: "7",
                    name: "小花",
                    sex: "女",
                    wechat: "xiaohuazuimei",
                    cost: "999",
                    tel: "13006666666"
                },
                {
                    number: "8",
                    name: "小花",
                    sex: "女",
                    wechat: "xiaohuazuimei",
                    cost: "999",
                    tel: "13006666666"
                },
                {
                    number: "9",
                    name: "小花",
                    sex: "女",
                    wechat: "xiaohuazuimei",
                    cost: "999",
                    tel: "13006666666"
                },
                {
                    number: "10",
                    name: "小花",
                    sex: "女",
                    wechat: "xiaohuazuimei",
                    cost: "999",
                    tel: "13006666666"
                }
            ]
        };
    }
};
</script>

<style scoped>
.fan-list {
    display: flex;
    flex-direction: column;
}

.fan-list-item {
    display: flex;
    flex-direction: column;
    margin: 0 0.625rem /* 10/16 */;
    font-size: 0.875rem /* 14/16 */;
    line-height: 1.5625rem /* 25/16 */;
    padding: 0.9375rem /* 15/16 */ 0;
    border-bottom: 1px solid #cccccc;
}

.fan-list-item-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.fan-list-item-number {
    width: 1.875rem /* 30/16 */;
    height: 1.25rem /* 20/16 */;
    line-height: 1.25rem /* 20/16 */;
    background: #ddbe59;
    border-radius: 0.625rem;
    text-align: center;
    color: #ffffff;
}

.icon-user {
    width: 3.125rem /* 50/16 */;
    height: 3.125rem /* 50/16 */;
}

.fan-list-userinfo-name {
    max-width: 4.6875rem /* 75/16 */;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
}

.fan-list-userinfo-baseinfo {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.fan-list-userinfo-contact {
    display: flex;
    flex-direction: column;
}
</style>
