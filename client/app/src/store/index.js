import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    results: {
      '1': {
        'y': true,
        'img_base64': '',
      },
      '2': {
        'y': true,
        'img_base64': '',
      },
      '3': {
        'y': true,
        'img_base64': '',
      },
      '4': {
        'y': true,
        'img_base64': '',
      },
    }
  },
  mutations: {
    updateResults(state, results) {
      state.results = results
    }
  },
  actions: {
  },
  modules: {
  }
})
