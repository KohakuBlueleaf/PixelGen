<script setup>
import $ from "jquery";
import ImgChooser from './utils/img-chooser.vue'
import RelativeSquare from './utils/relative_sq.vue'
import { Picture as IconPicture } from '@element-plus/icons-vue'
import { ref, reactive, watch, provide } from 'vue'


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

const pic_active = ref("Pixelized")
const src_list = reactive(['', ''])
const color_list = ref([])


function make_color_code(color){
  let bg = 'background: #'+color[0]+';'
  let tx = 'color: '+color[1]+';'
  return bg+tx
}
function submit(){
  let form_data = new FormData()
  
  for(let k in form){
    form_data.append(k, form[k])
  }
  if(file.value == undefined || file.value.raw == undefined){
    ElMessage({
      message: 'You should choose a file!',
      type: 'warning',
    })
    return
  }
  let raw_file = file.value.raw
  form_data.append('file', raw_file)
  
  let fr = new FileReader();
  fr.onload = ()=>{
    src_list[1] = fr.result
  }
  fr.readAsDataURL(raw_file);
  
  $.ajax({
    url: 'http://127.0.0.1:5000/api/generate',
    type: 'POST',
    contentType: false,
    processData: false,
    data: form_data
  }).done((resp)=>{
    console.log(resp)
    if(resp.status == 'ok'){
      src_list[0] = resp.data.output_img
      color_list.value = resp.data.colors
    }else if(resp.status == 'Error'){
      ElMessage({
        message: 'Something Wrong!',
        type: 'alarm'
      })
    }
  }).fail((err)=>{
    console.log(err)
  })
}
</script>


<template>
  <div class='col col-lg-4 col-12'>
    <el-form
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
  </div>
  
  <div class="col col-lg-5 col-12 d-flex">
    <div class="position-relative m-4 w-100">
      <el-tabs v-model="pic_active" class="w-100">
        <el-tab-pane label="Pixelized" name="Pixelized">
          <RelativeSquare class="w-100" style="text-align: center">
            <el-image 
              class="d-inline"
              style="max-width: 100%; max-height: 100%; width: 100%; height: 100%"
              fit="scale-down"
              :src="src_list[0]"
              :initial-index="0"
              :preview-src-list="src_list"
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
              :src="src_list[1]"
              :initial-index="1"
              :preview-src-list="src_list"
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
  </div>
  
  <div class="col col-lg-3 col-12 d-block">
    <div class="m-3">
      <p class="">
        Colors
      </p>
      <div class="d-flex flex-wrap">
        <div
          v-for = 'color in color_list'
          :key = 'color[0]'
          class="color-tag"
          :style="make_color_code(color)">
          <div>#{{color[0]}}</div>
        </div>
      </div>
    </div>
  </div>
</template>


<style>
.color-scroll{
  margin-top: 3rem;
}
.color-tag{
  border: white 1px solid;
  border-radius: .3rem;
  padding: .1rem;
  margin: .1rem;
  width: 3.6rem;
  text-align: center;
  font-size: .3rem;
  border: 1px solid black;
}

.input{
  width: 60% !important;
}

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