import request from 'axios'

const url ="http://localhost:8000/query/ "
export function getList(params) {
  return request({
    url:url,
    method: 'get',
    params
  })
}