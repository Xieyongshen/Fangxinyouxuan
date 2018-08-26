<template>
    <div class="accountDetail">
        <user-info></user-info>

        <div class="accountDetail-list">
            <div class="accountDetail-list-item" v-for="item in items" :key="item.number">
                <div class="accountDetail-list-item-row1">
                    <div class="accountDetail-list-item-name">{{item.name}}</div>
                    <div class="accountDetail-list-item-change">{{item.change}}</div>
                </div>
                <div class="accountDetail-list-item-time">{{item.time}}</div>
            </div>
        </div>

    </div>
</template>

<script>
import userInfo from "@/components/userInfo.vue";

export default {
    name: "accountDetail",
    components: {
        userInfo
    },

    data: function() {
        return {
            items: [
                {
                    number: "1",
                    name: "资金明细一",
                    change: "+88.88",
                    time: "2018-07-02 01:11:01"
                },
                {
                    number: "2",
                    name: "资金明细二",
                    change: "-28.88",
                    time: "2018-07-02 01:11:01"
                },
                {
                    number: "3",
                    name: "资金明细三",
                    change: "+88.88",
                    time: "2018-07-02 01:11:01"
                }
            ]
        };
    }
};
</script>

<style scoped>
.accountDetail-list {
    margin: 0;
}

.accountDetail-list-item {
    display: flex;
    flex-direction: column;
    margin: 0 0.9375rem;
    padding: 0.9375rem /* 15/16 */ 0;
    border-bottom: 1px solid #cccccc;
}

.accountDetail-list-item-row1 {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}
</style>
