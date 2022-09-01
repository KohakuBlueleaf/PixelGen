<script setup>
import { ref } from 'vue'
import { Picture as IconPicture } from '@element-plus/icons-vue'

import RelativeSquare from './utils/relative_sq.vue'

import { pic_data } from '../store'
const pic_active = ref("Pixelized")
</script>


<template>
  <div class="position-relative mt-3 w-100">
    <el-tabs v-model="pic_active" class="w-100">
      <el-tab-pane label="Pixelized" name="Pixelized">
        <RelativeSquare class="w-100" style="text-align: center">
          <el-image 
            class="d-inline"
            style="max-width: 100%; max-height: 100%; width: 100%; height: 100%"
            fit="scale-down"
            :src="pic_data.src_list[0]"
            :initial-index="0"
            :preview-src-list="pic_data.src_list"
          >
            <template #error>
              <div class="image-slot">
                <el-icon><icon-picture /></el-icon>
              </div>
            </template>
          </el-image>
        </RelativeSquare>
      </el-tab-pane>
      <el-tab-pane label="Original" name="Original">
        <RelativeSquare class="w-100" style="text-align: center">
          <el-image 
            class="d-inline"
            style="max-width: 100%; max-height: 100%; width: 100%; height: 100%"
            fit="scale-down"
            :src="pic_data.src_list[1]"
            :initial-index="1"
            :preview-src-list="pic_data.src_list"
          >
            <template #error>
              <div class="image-slot">
                <el-icon><icon-picture /></el-icon>
              </div>
            </template>
          </el-image>
        </RelativeSquare>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>


<style>
.image-slot {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  background: var(--el-fill-color-light);
  color: var(--el-text-color-secondary);
  font-size: 30px;
}

.image-slot .el-icon {
  font-size: 30px;
}
</style>