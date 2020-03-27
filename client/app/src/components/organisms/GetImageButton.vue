<template>
  <v-row justify="center" class="row">
    <v-btn
      @click="sendRequest()"
      height="50"
      width="150"
      class="v-btn"
    >
      写真を再撮影
    </v-btn>
  </v-row>
</template>

<script>
import axios from 'axios'
import { getResults } from '../../api/index'

export default {
  name: 'GetImageButton',
  methods: {
    sendRequest: async function() {
      const results = await getResults()
      this.$store.commit('updateResults', results.data)
    }
  }
}
</script>

<style scoped>
.row{
  margin-top: 50px;
}
</style>