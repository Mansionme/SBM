import Axios from "axios";
import request from 'axios'


const url ="http://localhost:8000/majors/"
export function getListByName(params) {
    return request({
      url:url,
      method: 'get',
      dataType:'json',
      data:{"class_name":params},
      params
    })
  }