<template>
  <v-container>
    <GetImageButton/>
    <ImageDialog windowId="1" />
    <ImageDialog windowId="2" />
    <ImageDialog windowId="3" />
    <ImageDialog windowId="4" />
  </v-container>
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'
import GetImageButton from '@/components/GetImageButton.vue'
import ImageDialog from '@/components/ImageDialog'

export default {
  name: 'Home',
  components: {
    HelloWorld,
    GetImageButton,
    ImageDialog
  },
}
</script>