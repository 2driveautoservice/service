<template>
    <div class="sign-up" id="app">
        <div class="columns is-vcentered is-mobile" id="side-image">
            <div class="column is-three-fifths p-0" id="side-image">
                <figure class="image" id="side-image">
                        <img src="../assets/media/autopros_auth_image.png" alt="Error loading image" id="side-image">
                </figure>
            </div>
            <div class="column is-3 is-offset-1">
                <h1 class="title" style="margin-bottom:3.75rem;">Sign up</h1>
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
                    <div class="field" style="margin-top:1.25rem;">
                        <div class="control">
                            <input class="input" type="password" placeholder="Confirm Password" v-model="passwordCfm" >
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <div class="select">
                            <select v-model="userType">
                                <option value="" disabled selected>Account Type</option>
                                <option value="Business">Business</option>
                                <option value="Employee">Employee</option>
                                <option value="Personal">Personal</option>
                            </select>
                            </div>
                        </div>
                        <div class="help is-danger" v-if="userType_errors.length">
                            <p v-for="error in userType_errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </div>

                    <label class="checkbox" style="margin-top:1.25rem;">
                        <input type="checkbox" v-model="terms">
                            I Accept <a href="#" style="color: #838996;">Terms and Conditions and Privacy Policy</a>
                    </label>

                    <div class="field" style="margin-top:1.875rem; margin-bottom:1.875rem;">
                        <div class="control">
                            <button class="button is-light is-link" style="width:100%">Create new account</button>
                        </div>
                    </div>
                    Already have an account? <router-link to="/log-in">Log in</router-link>
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
    name: 'SignUp',
    data() {
        return {
            email: '',
            password: '',
            passwordCfm: '',
            userType: '',
            terms: '',
            is_business_owner: false,
            is_business_user: false,
            is_consumer_user: false,
            email_errors: [],
            password_errors: [],
            userType_errors: [],
            general_errors: [],
        }
    },
    mounted () {
        document.title = "Sign up"
    },
    methods: {
        emailIsNotValid(email) {
            if(!email) {
                return 'Please enter your email'
            }
            if (!(/\S+@\S+\.\S+/.test(email))) {
                return 'Please enter a valid email'
            }
            return false
        },
        passwordIsNotValid(password, passwordCfm) {
            if(!password) {
                return 'Please enter a password'
            }
            if(!passwordCfm) {
                return 'Please confirm your password'
            }
            if(!(/[A-Z]/.test(password))) {
                return 'Password must contain at least 1 uppercase letter'
            }
            if (!(/[a-z]/.test(password))) {
                return 'Password must contain at least 1 letter'
            }
            if (!(/[0-9]/ .test(password))) {
                return 'Password must contain at least 1 digit'
            }
            if (password.length < 6) {
                return 'Password must contain at least 5 characters'
            }
            if (password !== passwordCfm) {
                return 'Passwords must match'
            }
            return false
        },
        resetErrors() {
            this.email_errors = []
            this.password_errors = []
            this.userType_errors = []
            this.general_errors = []
        },
        async submitForm() {
            this.resetErrors()

            const emailIsNotValid = this.emailIsNotValid(this.email)
            if (emailIsNotValid) {
                this.email_errors.push(emailIsNotValid)
            }else {
                const passwordIsNotValid = this.passwordIsNotValid(this.password, this.passwordCfm)
                if (passwordIsNotValid) {
                    this.password_errors.push(passwordIsNotValid)
                }else {
                    if (!this.userType) {
                        this.userType_errors.push('Account type must be selected')
                    }else {
                        if (!this.terms) {
                            this.general_errors.push('Please accept the Terms and Conditions and Private Policy')
                        }
                    }
                }
            }

            if (!this.email_errors.length && !this.password_errors.length && !this.userType_errors.length && !this.general_errors.length) {

                if (this.userType === 'Business') {
                    this.is_business_owner = true
                }else if (this.userType === 'Employee') {
                    this.is_business_user = true
                }else {
                    this.is_consumer_user = true
                }
                 
                //Set the formData to be sent to API
                const formData = {
                    email: this.email,
                    password: this.password,
                    is_business_owner: this.is_business_owner,
                    is_business_user: this.is_business_user,
                    is_consumer_user: this.is_consumer_user,
                }

                await axios
                .post("/api/v1/users/", formData)
                .then(response => {
                    this.$router.push('/log-in')
                })
                .catch(error => {
                    if (error.response) {
                        if (error.response.status.toString() == '400')
                        {
                            this.general_errors.push('Account creation has failed. Please ensure your credentials are valid')
                        }
                        console.log(JSON.stringify(error.response.data))
                    } else if (error.message) {
                        this.general_errors.push('Something went wrong. Please try again')
                        console.log(JSON.stringify(error))
                    }
                })
            }
        }
    }
}
</script>