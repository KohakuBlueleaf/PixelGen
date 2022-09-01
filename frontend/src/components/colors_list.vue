<script setup>
import { pic_data } from '../store'

function make_color_code(color){
  let bg = 'background: #'+color[0]+';'
  let tx = 'color: '+color[1]+';'
  return bg+tx
}
</script>


<template>
  <div class="mt-3">
    <p class="">
      Colors
    </p>
    <div class="d-flex flex-wrap">
      <div
        v-for = 'color in pic_data.colors'
        :key = 'color[0]'
        class="color-tag"
        :style="make_color_code(color)">
        <div>#{{color[0]}}</div>
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
  font-size: 12px;
  border: 1px solid black;
}
</style>