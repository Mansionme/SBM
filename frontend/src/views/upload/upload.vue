<template>
    <div class="app-container">
<el-card class="box-card">
<el-upload
class="upload-demo"
ref="upload"
action="http://localhost:8000/read/"
:on-preview="handlePreview"
:on-remove="handleRemove"
:file-list="fileList"
:auto-upload="false"
:before-remove="beforeRemove">
<el-button slot="trigger" size="medium" type="primary" round>选取文件</el-button>
<el-button style="margin-left: 10px;" size="medium" type="success" @click="submitUpload" round :loading="Loading">上传到服务器</el-button>
<div slot="tip" class="el-upload__tip">只能上传模版Excel文件</div>
</el-upload>
</el-card>
</div>
</template>
<script>
    export default{
        data() {
            return {
              fileList:[],
              Loading:false,
              timer
            };
          },
          methods: {
            submitUpload() {
              this.$confirm('确定上传吗').then(()=>{
                this.Loading=true;
                this.$refs.upload.submit();
                this.timer =setTimeout(()=>{
                  this.$message("上传成功")
                  this.Loading=false
                },600);
              })
              .catch(()=>{
                this.$message("上传失败")
              })
              
              
            },
            handleRemove(file, fileList) {
              console.log(file, fileList);
            },
            handlePreview(file) {
              console.log(file);
            },
            beforeRemove(file,fileList){
              return this.$confirm(`确定移除 ${ file.name }？`);
            }
          }
    }


</script>