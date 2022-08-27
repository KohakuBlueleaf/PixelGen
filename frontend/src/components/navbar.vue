<template>
  <el-menu
    mode="horizontal"
    router
  >
    <div class="container-fluid d-flex" style='max-width: 1320px'>
      <el-menu-item index="1">
        <el-link class="pixel-text" href="/" :underline="false" style="font-size: 2rem;">PixelGen</el-link>
      </el-menu-item>
      <div class="flex-grow-1"></div>
      <el-menu-item index="2">
        <el-link href="/about" :underline="false">About</el-link>
      </el-menu-item>
    </div>
  </el-menu>
</template>

<style>
.pixel-text{
  font-family: 'DotGothic16', sans-serif;
}
</style>