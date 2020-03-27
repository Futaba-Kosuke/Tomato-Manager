<template>
  <v-container justify="center">
    <GetImageButton/>
    <CamerasDisposition/>
  </v-container>
</template>

<script>
import GetImageButton from '@/components/organisms/GetImageButton.vue'
import CamerasDisposition from '@/components/organisms/CamerasDisposition.vue'
import { getResults } from '../../api/index'

export default {
  name: 'Home',
  components: {
    GetImageButton,
    CamerasDisposition
  },
  created: async function() {
    const results = await getResults()
    this.$store.commit('updateResults', results.data)
  }
}
</script>