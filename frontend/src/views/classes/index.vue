<template>
    <div class="app-container">
      <span></span>
      <el-input v-model="class_name" placeholder="请输入要查询的班级 例：数学一班" style="width: 300px;;"></el-input>&nbsp;
      <el-button type="primary" @click="handelQuery" plain>查询</el-button>
      <br>
      <br>
      <el-table
        v-loading="listLoading"
        :data="studentList"
        element-loading-text="Loading"
       border
        fit
        highlight-current-row
      >
      <el-table-column prop="student_num" label="学号" min-width="100">
        <template slot-scope="scope"> {{ scope.row.student_num}} </template>
        </el-table-column>
        <el-table-column prop="name" label="学生姓名" min-width="100">
        <template slot-scope="scope"> {{ scope.row.name }} </template>
        </el-table-column>
        <el-table-column prop="major" label="专业" min-width="100">
        <template slot-scope="scope"> {{ scope.row.major}} 
        </template>
        </el-table-column>
        <el-table-column prop="1judge" label="诚信评价（第一学期）" min-width="100">
            <template slot-scope="scope"> {{ scope.row.the_1st_judge}} 
            </template>
            </el-table-column>
        <el-table-column prop="2judge" label="诚信评价（第二学期）" min-width="100">
                <template slot-scope="scope"> {{ scope.row.the_2nd_judge}} 
                </template>
                </el-table-column>
        <el-table-column prop="3judge" label="诚信评价（第三学期）" min-width="100">
                <template slot-scope="scope"> {{ scope.row.the_3rd_judge}} 
                </template>
                </el-table-column>
                <el-table-column prop="4judge" label="诚信评价（第四学期）" min-width="100">
                    <template slot-scope="scope"> {{ scope.row.the_4th_judge}} 
                    </template>
                    </el-table-column>
                    <el-table-column prop="5judge" label="诚信评价（第五学期）" min-width="100">
                        <template slot-scope="scope"> {{ scope.row.the_5th_judge}} 
                        </template>
                        </el-table-column>
                        <el-table-column prop="6judge" label="诚信评价（第六学期）" min-width="100">
                            <template slot-scope="scope"> {{ scope.row.the_6th_judge}} 
                            </template>
                            </el-table-column>
                            <el-table-column prop="7judge" label="诚信评价（第七学期）" min-width="100">
                                <template slot-scope="scope"> {{ scope.row.the_7th_judge}} 
                                </template>
                                </el-table-column>
                                <el-table-column prop="8judge" label="诚信评价（第八学期）" min-width="100">
                                    <template slot-scope="scope"> {{ scope.row.the_8th_judge}} 
                                    </template>
                                    </el-table-column>
      </el-table>
    </div>
  </template>
  
  <script>
  import { getListByName } from '@/api/class'
  
  export default {
    filters: {
      statusFilter(status) {
        const statusMap = {
          published: 'success',
          draft: 'gray',
          deleted: 'danger'
        }
        return statusMap[status]
      }
    },
    data() {
      return {
        list: null,
        listLoading: true,
        studentList:[],
        class_name:''
      }
    },
   
    created() {
      this.fetchData()
    },
    methods: {
      fetchData() {
        this.listLoading = true
         //这里传入this.name， 
        getListByName({
          class_name:this.class_name}
        ).then(res => {
          this.studentList = res.data.data
          this.listLoading = false
          console.log(this.list,'res')
          
  
        })
      },
      handelQuery(){
        this.fetchData()
      }
    },
   
  }
  </script>
  