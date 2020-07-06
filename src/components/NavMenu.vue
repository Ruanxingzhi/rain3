<template>
  <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
    <el-menu-item index="1">仪表盘</el-menu-item>
    <el-menu-item index="2">靶机管理</el-menu-item>
    <el-menu-item index="3">exp管理</el-menu-item>
    <el-menu-item index="4">试验台</el-menu-item>
    </el-menu>
</template>

<script>
  export default {
    data() {
      return {
        activeIndex: '1'
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>

<style>

</style>