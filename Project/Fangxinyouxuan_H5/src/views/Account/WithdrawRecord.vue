<template>
    <div class="withdrawRecord">
        <user-info></user-info>

        <div class="withdrawRecord-list">
            <div class="withdrawRecord-list-item" v-for="item in items" :key="item.number">
                <div class="withdrawRecord-list-item-row1">
                    <div class="withdrawRecord-list-item-name">{{item.name}}</div>
                    <div class="withdrawRecord-list-item-change">{{item.change}}</div>
                </div>
                <div class="withdrawRecord-list-item-time">{{item.time}}</div>
            </div>
        </div>

    </div>
</template>

<script>
import userInfo from "@/components/userInfo.vue";

export default {
    name: "withdrawRecord",
    components: {
        userInfo
    },

    data: function() {
        return {
            items: [
                {
                    number: "1",
                    name: "提现记录一",
                    change: "-88.88",
                    time: "2018-07-02 01:11:01"
                },
                {
                    number: "2",
                    name: "提现记录二",
                    change: "-88.88",
                    time: "2018-07-02 01:11:01"
                },
                {
                    number: "3",
                    name: "提现记录三",
                    change: "-88.88",
                    time: "2018-07-02 01:11:01"
                },
                {
                    number: "4",
                    name: "提现记录四",
                    change: "-88.88",
                    time: "2018-07-02 01:11:01"
                },
                {
                    number: "5",
                    name: "提现记录五",
                    change: "-88.88",
                    time: "2018-07-02 01:11:01"
                }
            ]
        };
    }
};
</script>

<style scoped>
.withdrawRecord-list {
    display: flex;
    flex-direction: column;
}

.withdrawRecord-list-item {
    display: flex;
    flex-direction: column;
    margin: 0 0.9375rem;
    padding: 0.9375rem /* 15/16 */ 0;
    border-bottom: 1px solid #cccccc;
}

.withdrawRecord-list-item-row1 {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}
</style>
