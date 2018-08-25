<template>
    <div class="team">

        <search class="team-search" v-model="searchValue">
        </search>

        <div :class="{ placeHolder: placeHolderShow}"></div>

        <div class="team-toolBar">
            <div class="team-toolBar-select">
                <img src="">
                <div class="team-toolBar-select-text">全部</div>
            </div>
            <div class="team-toolBar-totalTeamMenber">团队总人数: {{totalTeamMenber}}</div>
        </div>

        <div class="team-list">
            <div class="team-list-item" v-for="item in searchFor(items, searchValue)" :key="item.number">
                <div class="team-list-item-content">
                    <img src="@/assets/ic_user.png" class="icon-user">
                    <div class="team-list-item-userinfo">
                        <div class="accountDetail-list-item-name">{{item.username}}</div>
                        <div class="accountDetail-list-item-recommendedBy">推荐人: {{item.recommendedBy}}</div>
                        <div>
                            <div class="accountDetail-list-item-recommendedTime">{{item.recommendedTime}}</div>
                            <div class="accountDetail-list-item-recommendedFrom">来源: {{item.recommendedFrom}}</div>
                        </div>
                    </div>
                    <x-icon type="ios-arrow-forward" size="24" class="accountDetail-icon-in"></x-icon>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import { Search } from "vux";

export default {
    name: "team",
    components: {
        Search
    },

    data: function() {
        return {
            totalTeamMenber: "85",
            results: [],
            searchValue: "",
            placeHolderShow: false,
            items: [
                {
                    number: "1",
                    username: "初夏c",
                    recommendedBy: "小黄",
                    recommendedTime: "2018-07-02 01:11:01",
                    recommendedFrom: "二维码"
                },
                {
                    number: "2",
                    username: "李颖l",
                    recommendedBy: "lily bai",
                    recommendedTime: "2018-07-02 01:11:01",
                    recommendedFrom: "分享"
                },
                {
                    number: "3",
                    username: "薄荷",
                    recommendedBy: "多多麻麻",
                    recommendedTime: "2018-07-02 01:11:01",
                    recommendedFrom: "二维码"
                }
            ]
        };
    },

    methods: {
        setFocus() {
            this.$refs.search.setFocus();
        },
        resultClick(item) {
            window.alert("you click the result item: " + JSON.stringify(item));
        },
        getResult(val) {
            console.log("on-change", val);
            console.log(this.searchValue);
            this.results = val ? getResult(this.value) : [];
        },
        onSubmit() {
            this.$refs.search.setBlur();
        },
        onFocus() {
            console.log("on focus");
            this.placeHolderShow = true;
        },
        onCancel() {
            console.log("on cancel");
            this.placeHolderShow = false;
        },

        searchFor(value, searchStr) {
            var result = [];

            if (searchStr == "") {
                return value;
            }

            searchStr = searchStr.trim();

            result = value.filter(function(item) {
                if (item.username.indexOf(searchStr) != -1) {
                    return item;
                }
            });

            return result;
        }
    }
};

function getResult(val) {
    let rs = [];
    for (let i = 0; i < 20; i++) {
        rs.push({
            title: `${val} result: ${i + 1} `,
            other: i
        });
    }
    return rs;
}
</script>

<style scoped>

.team-toolBar {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin: 0.9375rem 0.9375rem;
}

.team-toolBar-select {
    display: flex;
    flex-direction: column;
}

.team-list {
    display: flex;
    flex-direction: column;
}

.team-list-item {
    display: flex;
    flex-direction: column;
    margin: 0 0.9375rem;
    padding: .9375rem /* 15/16 */ 0;
    border-bottom: 1px solid #cccccc;
}

.team-list-item-content {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    position: relative;
}

.team-list-item-userinfo {
    width: 14.375rem /* 230/16 */;
    line-height: 1.5625rem /* 25/16 */;
    display: flex;
    flex-direction: column;
}

.accountDetail-list-item-recommendedBy {
    font-size: 15px;
    color: #888888;
}

.accountDetail-list-item-recommendedTime {
    font-size: 15px;
    color: #888888;
}

.accountDetail-list-item-recommendedFrom {
    font-size: 15px;
    align-self: flex-end;
}

.icon-user {
    width: 5rem /* 80/16 */;
    height: 5rem /* 80/16 */;
    margin-right: 0.625rem /* 10/16 */;
}

.accountDetail-icon-in {
    height: 5rem /* 80/16 */;
}

.accountDetail-list-item-recommendedTime,
.accountDetail-list-item-recommendedFrom {
    font-size: 0.8125rem /* 13/16 */;
    display: inline-block;
}

.accountDetail-list-item-recommendedFrom {
    float: right;
}
</style>
