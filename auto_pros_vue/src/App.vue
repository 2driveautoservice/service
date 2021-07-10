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
  width: 100%;
  margin: 0;
  padding: 0;
  top:0;
  left:0;
}
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
