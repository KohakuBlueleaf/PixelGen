<script setup>
const props = defineProps(['sticky_style'])
</script>

<style scope>
.position-sticky{
  position: sticky
}
</style>


<template>
  <div>
    <div class="position-sticky" :style="props.sticky_style">
      <slot></slot>
    </div>
  </div>
</template>