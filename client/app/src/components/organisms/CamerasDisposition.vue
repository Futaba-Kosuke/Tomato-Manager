<template>
<v-row justify="center">
  <div class="div">
    <v-row justify="center">
      <img src='../../assets/farm.png' class="img"/>
    </v-row>
    <CameraButton windowId="1" position="absolute" top=0 left=0 />
    <CameraButton windowId="2" position="absolute" top=0 right=0 />
    <CameraButton windowId="3" position="absolute" bottom=0 left=0 />
    <CameraButton windowId="4" position="absolute" bottom=0 right=0 />
  </div>
</v-row>
</template>

<script>
import CameraButton from '@/components/molecules/CameraButton'

export default {
  name: 'CameraDisposition',
  components: {
    CameraButton,
  },
  data: function() {
    return {
      top: 0,
      left: 0,
      right: 0,
      bottom: 0,
    }
  }
}
</script>

<style scoped>
.div {
  margin-top: 50px;
  width: 906px;
  height: 681px;
  position: relative;
}

.row {
  position: relative;
}

.img {
  position: absolute;

  border: solid;
  padding: 0;
}
</style>