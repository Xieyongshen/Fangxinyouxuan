<template>
    <div class="home">
        <user-info></user-info>

        <div class="me-function">
            <div class="me-function-item">
                <img @click="goOrder" class="me-icon" src="@/assets/ic_order.png">
                <router-link to="/order" class="me-function-item-a">本店订单</router-link>
            </div>
            <div class="me-function-item">
                <img @click="goIncome" class="me-icon" src="@/assets/ic_income.png">
                <router-link to="/income" class="me-function-item-a">本店收益</router-link>
            </div>
            <div class="me-function-item">
                <img @click="goManage" class="me-icon" src="@/assets/ic_manage.png">
                <router-link to="/manage" class="me-function-item-a">商品管理</router-link>
            </div>
        </div>

        <div class="me-manage weui-cells">
            <a @click="goAccount" class="weui-cell weui-cell_access" href="javascript:;">
                <div class="weui-cell__bd">
                    <p>我的金库</p>
                </div>
                <div class="weui-cell__ft"></div>
            </a>
            <a @click="goOrder" class="weui-cell weui-cell_access" href="javascript:;">
                <div class="weui-cell__bd">
                    <p>货品到店</p>
                </div>
                <div class="weui-cell__ft">一键收货</div>
            </a>
            <a @click="goTeam" class="weui-cell weui-cell_access" href="javascript:;">
                <div class="weui-cell__bd">
                    <p>我的团队</p>
                </div>
                <div class="weui-cell__ft"></div>
            </a>
            <a @click="goRanking" class="weui-cell weui-cell_access" href="javascript:;">
                <div class="weui-cell__bd">
                    <p>优质用户排行榜</p>
                </div>
                <div class="weui-cell__ft"></div>
            </a>
            <a @click="goDeliver" class="weui-cell weui-cell_access" href="javascript:;">
                <div class="weui-cell__bd">
                    <p>门店配送设置</p>
                </div>
                <div class="weui-cell__ft">{{postConfig}}</div>
            </a>

        </div>
    </div>
</template>

<script>
import userInfo from "@/components/userInfo.vue";

export default {
    name: "home",
    components: {
        userInfo
    },

    data: function() {
        return {
            postConfig: "已开启"
        };
    },

    methods: {
        goOrder() {
            this.$router.push("/order");
        },
        goIncome() {
            this.$router.push("/income");
        },
        goManage() {
            this.$router.push("/manage");
        },
        goAccount() {
            this.$router.push("/account");
        },
        goTeam() {
            this.$router.push("/team");
        },
        goRanking() {
            this.$router.push("/ranking");
        },
        goDeliver() {
            this.$router.push("/deliver");
        }
    }
};
</script>

<style scoped>
.home {
    position: relative;
}

.me-function {
    margin: 0 auto;
    display: flex;
}

.me-function-item {
    width: 13.75rem;
    padding: 0.9375rem;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.me-function-item-a {
    font-size: 1rem /* 16/16 */;
    text-decoration: none;
    color: #333;
}

.me-icon {
    width: 2.5rem;
    height: 2.5rem;
    margin-bottom: 0.625rem;
}

.me-manage {
    font-size: 1rem /* 16/16 */;
}
</style>
