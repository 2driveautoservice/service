import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

//Luke: Set url for starting the frontend

axios.defaults.baseURL = 'https://autopros.app/backend'

//Luke: Added axios to help mount app? Probably keep it the same if using axios
createApp(App).use(store).use(router, axios).mount('#app')
