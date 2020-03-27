<template>
<div
  :style="styles"
>
  <v-btn
    :color="buttonColor"
    @click.stop="dialogFlag = true"
    dark
    rounded
    width=100
    height=50
    bordered
  >
    {{ 'カメラ' + this.windowId }}
  </v-btn>
  <v-dialog
    v-model="dialogFlag"
    max-width="700"
  >
    <v-card>
      <v-toolbar dark :color="buttonColor">
        <v-btn icon dark @click="dialogFlag = false">
          <v-icon>mdi-close</v-icon>
        </v-btn>
        <v-toolbar-title>{{ 'カメラ' + this.windowId }}</v-toolbar-title>
        <v-spacer></v-spacer>
        <p class="p">{{ predictResult }}</p>
      </v-toolbar>
      <v-img
        :src="getImageBase64"
      />
    </v-card>
  </v-dialog>
</div>
</template>

<script>
export default {
  name: 'ImageWindow',
  props: {
    windowId: String,
    position: {},
    top: {},
    bottom: {},
    left: {},
    right: {}
  },
  data: function() {
    return {
      dialogFlag: false
    }
  },
  computed: {
    getImageBase64: function() {
      const imgBase64 = this.$store.state.results[this.windowId]['img_base64']
      if (imgBase64 != '')
        return 'data:image/jpeg;base64,' + imgBase64
      return ''
    },
    styles: function() {
      return {
        position: this.position,
        top: Number(this.top),
        bottom: Number(this.bottom),
        left: Number(this.left),
        right: Number(this.right),
      }
    },
    buttonColor: function() {
      const result = this.$store.state.results[this.windowId]['result']
      if (result) {
        return 'rgb(235, 80, 70)'
      }
      return 'rgb(178, 200, 0)'
    },
    predictResult: function() {
      const result = this.$store.state.results[this.windowId]['result']
      if (result) {
        return '熟しています！'
      }
      return '熟していません！'
    },
  },
}
</script>
<style scoped>
.p {
  font-size: 20px;
}
</style>