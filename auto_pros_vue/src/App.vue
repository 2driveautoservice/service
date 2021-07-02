<template>
  <router-view/>
</template>

<style lang="scss">
//Import css frameworks and stuff like bulma

@import '../node_modules/bulma';
//Or specify the fonts and stuff yourself
html,
body,
#app {
  text-align: center;
  min-height: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
}
</style>


<script>
import axios from 'axios'

export default {
  data() {
    return {}
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
}
</script>
