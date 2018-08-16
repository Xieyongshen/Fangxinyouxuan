import {
    wxRequest
} from '@/api/wxRequest';

const apiFanxin = 'http://119.23.225.244';
// const apiFanxin = 'http://127.0.0.1:8000';
//根据位置获取商店
const getShops = (params) => wxRequest(params, apiFanxin + "/api/getShops");
//获取首页店铺商品分类
const getShopCategory = (params) => wxRequest(params, apiFanxin + "/api/getShopCategory");
//获取首页当前店铺下的商品
const getShopProduct = (params) => wxRequest(params, apiFanxin + "/api/getShopProduct");
//登录
const login = (params) => wxRequest(params, apiFanxin + "/api/login");
//获取当前大分类下小分类商品
const getCategoryProduct = (params) => wxRequest(params, apiFanxin + "/api/getCategoryProduct");
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

export default {
    getShops,
    getShopCategory,
    getShopProduct,
    login,
    getCategoryProduct,
    getProductDetail,
    getOrderList,
    getOrderDetail,
    getShoppingCart,
    getUserAddress
}