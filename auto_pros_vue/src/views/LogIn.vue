<template>
    <div class="log-in" id="app">
        <div class="columns is-vcentered is-mobile" id="side-image">
            <div class="column is-three-fifths p-0" id="side-image" >
                <figure class="image" id="side-image">
                        <img src="../assets/media/autopros_auth_image.png" alt="Error loading image" id="side-image">
                </figure>
            </div>
            <div class="column is-3 is-offset-1" >
                <h1 class="title" style="margin-bottom:3.75rem;">Log In</h1>
                <form @submit.prevent="submitForm" novalidate>
                    <div class="field" v-if="email_errors.length">
                        <div class="control">
                            <input class="input is-danger" type="email" placeholder="Email" v-model="email">
                            <div class="help is-danger is-pulled-left" v-if="email_errors.length">
                                <p v-for="error in email_errors" v-bind:key="error">{{ error }}</p>
                            </div>
                        </div>
                    </div>
                    <div class="field" v-else>
                        <div class="control">
                            <input class="input" type="email" placeholder="Email" v-model="email">
                        </div>
                    </div>
                    <div class="field" style="margin-top:1.25rem;" v-if="password_errors.length">
                        <div class="control">
                            <input class="input is-danger" type="password" placeholder="Password" v-model="password">
                            <div class="help is-danger is-pulled-left">
                                <p v-for="error in password_errors" v-bind:key="error">{{ error }}</p>
                            </div>
                        </div>
                    </div>
                    <div class="field" style="margin-top:1.25rem;" v-else>
                        <div class="control">
                            <input class="input" type="password" placeholder="Password" v-model="password" >
                        </div>
                    </div>
                    <div class="field" style="margin-top:1.875rem; margin-bottom:1.875rem;">
                        <div class="control">
                            <button class="button is-light is-link" style="width:100%">Log In</button>
                        </div>
                    </div>
                    Don't have an account? <router-link to="/sign-up">Sign up</router-link>
                    <div class="help is-danger" style="margin-top:1.875rem;" v-if="general_errors.length">
                        <p v-for="error in general_errors" v-bind:key="error">{{ error }}</p>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<style>
#side-image {
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
    name: 'LogIn',
    data() {
        return {
            email: '',
            password: '',
            email_errors: [],
            password_errors: [],
            general_errors: [],
        }
    },
    mounted () {
        document.title = "Log In"
    },
    methods: {
        emailIsNotValid(email) {
            if(!email || !(/\S+@\S+\.\S+/.test(email))) {
                return 'Please enter your email'
            }
        },
        passwordIsNotValid(password, passwordCfm) {
            if(!password) {
                return 'Please enter your password'
            }
            return false
        },
        resetErrors() {
            this.email_errors = []
            this.password_errors = []
            this.general_errors = []
        },

        async submitForm() {
            this.resetErrors()
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")

            const emailIsNotValid = this.emailIsNotValid(this.email)
            if (emailIsNotValid) {
                this.email_errors.push(emailIsNotValid)
            }else {
                const passwordIsNotValid = this.passwordIsNotValid(this.password, this.passwordCfm)
                if (passwordIsNotValid) {
                    this.password_errors.push(passwordIsNotValid)
                }
            }

            if (!this.email_errors.length && !this.password_errors.length) {
                const formData = {
                    email: this.email,
                    password: this.password
                }
                
                await axios
                .post("/api/v1/token/login/", formData)
                .then(response => {
                    const token = response.data.auth_token
                    this.$store.commit('setToken', token)
                        
                    axios.defaults.headers.common["Authorization"] = "Token " + token
                    localStorage.setItem("token", token)
                    //Luke: eventually make this only if they a consumer user or something
                    const toPath = this.$route.query.to || '/business-listings'
                    this.$router.push(toPath)
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                    if (error.response.status === 429) {
                        this.general_errors.push('Too many failed log in attempts. Please try again later.')
                    }
                    if (error.response) {
                        this.general_errors.push('Incorrect email or password.')
                    } else {
                        this.general_errors.push('Something went wrong. Please try again')

                    }
                 })
            }
        }
    }
}
</script>
      