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
import GetImageButton from '@/components/GetImageButton.vue'
import ImageDialog from '@/components/ImageDialog'
import { getResults } from '../api/index'

export default {
  name: 'Home',
  components: {
    GetImageButton,
    ImageDialog
  },
  created: async function() {
    const results = await getResults()
    this.$store.commit('updateResults', results.data)
  }
}
</script>