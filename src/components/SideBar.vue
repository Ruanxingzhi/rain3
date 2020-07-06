<template>
  <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    <el-col>
        <el-menu
            :default-active="activeNav"
            class="el-menu-vertical-demo">

            <el-menu-item index="nav">
                <i class="el-icon-menu"></i>
                <span slot="title">导航</span>
            </el-menu-item>
            <el-menu-item index="doc">
            <i class="el-icon-document"></i>
            <span slot="title">手册</span>
            </el-menu-item>
            
        </el-menu>
        </el-col>
    </el-aside>
</template>

<script>
export default {
  methods: {
    handleOpen(key, keyPath) {
    console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
    console.log(key, keyPath);
    }
  }
}
</script>

<style>

</style>