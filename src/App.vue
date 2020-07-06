<template>
  <div id="app">
    <el-container style="height: 30em; margin:1em; border: 1px solid #eee">

      <el-aside width="200px"><side-bar/></el-aside>
      <el-container>
        <el-header><nav-menu/></el-header>
        <el-main></el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import NavMenu from './components/NavMenu.vue'
import SideBar from './components/SideBar.vue'

export default {
  name: 'app',
  components: {
    NavMenu,
    SideBar
  }
}
</script>

<style>

</style>
