<template>
  <v-container>
    <v-btn
      @click="sendRequest()"
      height="50"
      width="150"
    >
      写真を撮影
    </v-btn>
  </v-container>
</template>

<script>
import axios from 'axios'
import { getResults } from '../api/index'

export default {
  name: 'GetImageButton',
  methods: {
    sendRequest: async function() {
      const results = await getResults()
      this.$store.commit('updateResults', results.data)
      console.log(this.$store.state.results)
    }
  }
}
</script>

<style scoped>

</style>