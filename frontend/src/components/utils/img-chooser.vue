<script setup>
import { ref, watch } from 'vue';
import { genFileId } from 'element-plus'
const emit = defineEmits([
  'update:files'
])
const props = defineProps(['files', 'limit'])
const upload = ref()
const file_list = ref([])


watch(file_list, (nv, ov) =>{
  if(props.limit == 1){
    emit('update:files', nv[0])
  }else{
    emit('update:files', nv)
  }
}, {
  immediate: true
})


function handle_exceed(files, u_files){
  upload.value.clearFiles()
  const file = files[0]
  file.uid = genFileId()
  upload.value.handleStart(file)
}
function handle_remove(files, u_files){
  if(props.limit == 1){
    emit('update:files', undefined)
  }else{
    emit('update:files', u_files)
  }
}
</script>


<template>
  <div class="d-block">
    <el-upload
      ref="upload"
      action="__placeholder__"
      :limit="limit"
      :on-exceed="handle_exceed"
      :on-remove="handle_remove"
      :auto-upload="false"
      v-model:file-list="file_list"
    >
      <template #trigger>
        <el-button type="primary">
          Choose file
        </el-button>
      </template>
    </el-upload>
  </div>
</template>