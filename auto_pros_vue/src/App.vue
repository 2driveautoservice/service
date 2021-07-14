<template>
  <router-view/>
</template>

<style lang="scss">
@import '../node_modules/bulma';

//Properties that all pages have in common
html,
body,
#app {
  text-align: center;
  min-height: 100%;
  height: 100%;
  width: 100%;
}

p {
  font-size: 1rem;
}

//Auto resize font's based on screen width
@media all and (min-width: 100px)  {  html, body, #app  { font-size:0.30em;  } }
@media all and (min-width: 700px)  {  html, body, #app  { font-size:0.40em;  } }
@media all and (min-width: 900px)  {  html, body, #app  { font-size:0.50em;  } }
@media all and (min-width: 1100px)  {  html, body, #app  { font-size:0.60em;  } }
@media all and (min-width: 1300px) {  html, body, #app  { font-size:0.70em;  } }
@media all and (min-width: 1500px) {  html, body, #app  { font-size:0.90em;  } }
@media all and (min-width: 1700px) {  html, body, #app  { font-size:1.0em;  } }
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
