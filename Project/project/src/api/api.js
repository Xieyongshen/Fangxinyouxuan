import {
    wxRequest
} from '@/api/wxRequest';

// const apiFanxin = 'http://119.23.225.244';
// const apiFanxin = 'http://127.0.0.1:8000';
const apiFanxin = 'http://fangxintech.com';
//根据位置获取商店
const getShops = (params) => wxRequest(params, apiFanxin + "/api/getShops");
//获取首页店铺商品分类
const getShopCategory = (params) => wxRequest(params, apiFanxin + "/api/getShopCategory");
//获取首页banner
const getBanners = (params) => wxRequest(params, apiFanxin + "/api/getBanners");
//获取首页当前店铺下的商品
const getShopProduct = (params) => wxRequest(params, apiFanxin + "/api/getShopProduct");
//登录
const login = (params) => wxRequest(params, apiFanxin + "/api/login");
//获取当前大分类下小分类商品
const getCategoryProduct = (params) => wxRequest(params, apiFanxin + "/api/getCategoryProduct");
//获取分类页banner
const getCategoryBanners =  (params) => wxRequest(params, apiFanxin + "/api/getCategoryBanners");

//获取商品详情
const getProductDetail = (params) => wxRequest(params, apiFanxin + "/api/getProductDetail");

//获取购物车列表
const getShoppingCart = (params) => wxRequest(params, apiFanxin + "/api/getShoppingCart");
//获取用户订单列表
const getOrderList = (params) => wxRequest(params, apiFanxin + "/api/getOrderList");
//获取订单详情
const getOrderDetail = (params) => wxRequest(params, apiFanxin + "/api/getOrderDetail");


//获取用户收货地址
const getUserAddress = (params) => wxRequest(params, apiFanxin + "/api/getUserAddress");
//获取用户余额
const getMyBalance = (params) => wxRequest(params, apiFanxin + "/api/getMyBalance");
//提交订单
const submitOrder = (params) => wxRequest(params, apiFanxin + "/api/submitOrder");
//获取用户红包
const getUserRedPacket = (params) => wxRequest(params, apiFanxin + "/api/getUserRedPacket");
//获取推荐商品
const getRecommendPros = (params) => wxRequest(params, apiFanxin + "/api/getRecommendPros");
//获取优惠券页面商品
const getCouponProducts = (params) => wxRequest(params, apiFanxin + "/api/getCouponProducts");
//获取热门搜索
const getHotSearch = (params) => wxRequest(params, apiFanxin + "/api/getHotSearch");
//获取搜索结果
const getSearchResult = (params) => wxRequest(params, apiFanxin + "/api/getSearchResult");

//保存或新增收货地址
const saveMyAddress = (params) => wxRequest(params, apiFanxin + "/api/saveMyAddress");
//删除收货地址
const deleteMyAddress = (params) => wxRequest(params, apiFanxin + "/api/deleteMyAddress");
export default {
    getShops,
    getShopCategory,
    getBanners,
    getShopProduct,
    login,
    getCategoryProduct,
    getCategoryBanners,
    getProductDetail,
    getOrderList,
    getOrderDetail,
    getShoppingCart,
    getUserAddress,
    getMyBalance,
    getUserRedPacket,
    getRecommendPros,
    getCouponProducts,
    submitOrder,
    getSearchResult,
    getHotSearch,
    saveMyAddress,
    deleteMyAddress
}