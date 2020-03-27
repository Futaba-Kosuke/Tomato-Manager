<template>
  <v-app>
    <v-app-bar app dark color="rgb(245, 90, 80)" height="90">
      <v-toolbar-title class="headline text-uppercase">
        <span class="title_font">トマト監視システム</span>
      </v-toolbar-title>
    </v-app-bar>

    <v-content class="content">
      <Home/>
    </v-content>
  </v-app>
</template>

<script>
import Home from './views/Home'

export default {
  name: 'App',
  components: {
    Home,
  },
}
</script>

<style scoped>
.content {
  background-color: rgb(188, 210, 3);
}
</style>