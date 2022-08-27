<template>
  <div class="position-relative d-inline-block">
    <div style="margin-top: 100%"></div>
    <div class="sq-block d-flex">
      <slot></slot>
    </div>
  </div>
</template>

<style>
.sq-block{
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
}
</style>