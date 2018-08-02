import {
    wxRequest
} from '@/api/wxRequest';

const apiFanxin = 'http://127.0.0.0:8000'

const getIndex = (params) => wxRequest(params, apiBenshi + "/api/getIndex");

export default {
    getIndex
}