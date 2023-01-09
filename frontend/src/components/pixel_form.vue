<script setup>
import { ref, reactive } from 'vue'
import { Picture as IconPicture } from '@element-plus/icons-vue'

import ImgChooser from './utils/img-chooser.vue'

import { pic_data } from '../store'


const outline_options = [
  {value: 0, label: 'None'},
  {value: 1, label: 'low'},
  {value: 2, label: 'medium'},
  {value: 3, label: 'high'},
  {value: 4, label: 'extreme'},
]
const file = ref(null)
const form = reactive({
  k: 8, scale: 1, precise: 3,
  blur: 0, erode: 0,
  saturation: 0, contrast: 0,
})


function submit(){
  //check if choosed file is valid
  if(file.value == undefined || file.value.raw == undefined){
    ElMessage({
      message: 'You should choose a file!',
      type: 'warning',
    })
    return
  }else if(file.value.raw.size > 20000000){
    ElMessage({
      message: 'File size over 20MB!',
      type: 'warning',
    })
    return
  }
  
  //build form
  let form_data = new FormData()
  for(let k in form){
    form_data.append(k, form[k])
  }
  let raw_file = file.value.raw
  form_data.append('file', raw_file)
  
  //read file data for showing original pic
  let fr = new FileReader();
  fr.onload = ()=>{pic_data.src_list[1] = fr.result}
  fr.readAsDataURL(raw_file);
  
  pic_data.src_list[0] = ''
  ElMessage('Generating...')
  fetch('/api/generate',{
    method: 'POST',
    body: form_data
  }).then((resp)=>{
    if(!resp.ok){
      ElMessage({
        message: 'Your request is failed!',
        type: 'error'
      })
    }
    return resp.json()
  }).then((resp)=>{
    switch (resp.status) {
      case 'ok':
        pic_data.src_list[0] = resp.data.output_img
        pic_data.colors = resp.data.colors
        ElMessage({message: 'Done!', type: 'success'})
        break;
      case 'Error':
        ElMessage({message: resp.Error, type: 'error'})
        break;
      default:
        ElMessage({
          message: 'Server Response is broken',
          type: 'error'
        })
    }
  })
}
</script>


<template>
  <el-form
    style="max-width: 100%;"
    label-position = "top"
    label-width = "100px"
    :model = "form"
  >
    <div class="p-4">
      <ImgChooser class="w-100" v-model:files="file" :limit="1"></ImgChooser>
      <div class="d-flex mt-4 mb-2">
        <div class="w-100 me-3">
          <p>Main Options</p>
          <el-form-item label="Number of Colors">
            <el-input-number class="w-100" :min="2" :max="48" v-model="form.k"/>
          </el-form-item>
          <el-form-item label="Dot size">
            <el-input-number class="w-100" :min="1" :max="8" v-model="form.scale"/>
          </el-form-item>
          <el-form-item label="Precision">
            <el-input-number class="w-100" :min="1" :max="10" v-model="form.precise"/>
          </el-form-item>
        </div>
        <div class="w-100 ms-3">
          <p>Picture Effect</p>
          <el-form-item label="Smoothing">
            <el-input-number class="w-100" :min="0" :max="10" v-model="form.blur"/>
          </el-form-item>
          <el-form-item label="Outline Inflating">
            <el-select class="w-100" v-model="form.erode" placeholder="Select">
              <el-option
                v-for="item in outline_options"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </el-form-item>
          <el-form-item label="Saturation">
            <el-input-number class="w-100" :min="-10" :max="10" v-model="form.saturation"/>
          </el-form-item>
          <el-form-item label="Contrast">
            <el-input-number class="w-100" :min="-10" :max="10" v-model="form.contrast"/>
          </el-form-item>
        </div>
      </div>
      <el-button class="w-100" type="success" plain @click="submit">Generate!</el-button>
    </div>
  </el-form>
</template>


<style>
.input{
  width: 60% !important;
}
</style>