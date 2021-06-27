<template>
  <div class="business-listing" id="app">
    <nav class="navbar is-white">
      <div class="navbar-brand">
        <figure class="image is-64x64">
          <img src="../assets/media/autopros_logo.png" alt="Logo">
        </figure>
      </div>
      <div class="navbar-menu">
        <div class="navbar-start" id="navbar-links">
          <a class="navbar-item">
            Browse Categories
          </a>
          <a class="navbar-item">
            Blog
          </a>
          <a class="navbar-item">
            Write a Review
          </a>
        </div>
      </div>
    </nav>
    <nav class="navbar has-background-white-ter">
      <div class="navbar-menu">
        <div class="navbar-start">
          <form class="form-inline" @submit.prevent="submitForm" novalidate>
            <div class="navbar-item" id="category-select">
              <div class="field">
                <div class="control">
                  <div class="select">
                    <select v-model="service_category_choice">
                      <option value="" selected disabled>Choose a Category</option>
                      <option v-bind:value="{name:service.name, companies:service.get_companies}" v-for="service in serviceCategories">
                        {{ service.name }}
                      </option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
            <div class="navbar-item">
              near
            </div>
            <div class="navbar-item">
              <div class="field">
                <div class="control">
                  <input class="input" type="search" v-model="location_choice" list="filtered-location-list">
                  <datalist id="filtered-location-list">
                    <option v-for="i in filterLocations" >{{ i }}</option>
                  </datalist>
                </div>
              </div>
            </div>
            <div class="navbar-item">
              <div class="field">
                <div class="control">
                  <button class="button" id="icon-button"><i class="fa fa-search"></i></button>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </nav>
    <nav class="navbar is-white">
      <div class="navbar-menu">
        <div class="navbar-start">
          <div class="tabs">
            <ul>
              <li class="is-active" id="matches">
                <a>
                  Category Match ({{ getNumOfMatches }})
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </nav>
    <div class="columns" id="columns-filter">
      <div class="column is-four-fifths py-1">
        <div class="box" id="query-string">
          {{ query_string }}
        </div>
      </div>
      <div class="column is-one-fifth py-1">
        <div class="card" id="card-sort">
          <header class="card-header">
            <p class="card-header-title">
              Sort Order
            </p>
          </header>
          <div class="card-content">
            <div class="control">
              <label class="radio">
                <input type="radio" v-on:click="filterByRating" name="radio-sort">
                  Avg Custom Rating
              </label>
              <br>
              <label class="radio">
                <input type="radio" v-on:click="filterByStarScore" name="radio-sort">
                  Star Score
              </label>
              <br>
              <label class="radio">
                <input type="radio" v-on:click="filterByRecentRating" name="radio-sort">
                  Recently Reviewed
              </label>
              <br>
              <label class="radio">
                <input type="radio" v-on:click="filterByBestOfHomestars" name="radio-sort">
                  Best of Homestars
              </label>
            </div>
          </div>
        </div>
      </div> 
    </div>
    <div class="business-boxes">
      <div class="box" id="borderBox-companies">
        <div class="columns is-multiline is-variable is-0">
          <CompanyBox 
            v-for="company in filtered_companies"
            v-bind:key="company.id"
            v-bind:company="company" />
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.navbar {
  height: 4rem;
}
.navbar-start {
  margin-left: 4rem;
}
#navbar-links{
  margin-left: 0;
}
.tabs ul {
  border-bottom-style: none;
}
.tabs li.is-active a {
  color: #000000;
  border-bottom-width: medium;
}
.business-listing {
  background-color: rgb(242, 246, 250);
}
.business-boxes {
  width: 50rem;
  height: 18.75rem;
}
#borderBox-companies {
    height: 30rem;
    width: 50rem;
    border-radius:0rem;
    overflow: auto;
    margin-left: 4rem;
    margin-top: 2rem;
}
#icon-button {
  border-radius:0.2rem;
  border: none;
  width: 2.5rem;
  height: 2.5rem;
  background-color: #3273dc;
}
#columns-filter {
  width:70rem;
  height:5rem;
  margin-top:1rem;
}
.card-header {
  background-color: black;
}
.card-header-title {
  color: white;
}
.fa {
  color: white;
}
#query-string {
  height:6rem;
  font-size:2rem;
  margin-left:4rem;
  text-align: left;
}
.card-content {
  padding: 0.8rem 0.8rem 0.8rem 0.8rem;
  background-color:white;
  text-align: left;
}
#category-select {
  padding-left:0;
}
.form-inline {  
  display: flex;
  flex-flow: row wrap;
  align-items: center;
}
</style>

<script>
import axios from 'axios'
import CompanyBox from '@/components/CompanyBox'

export default {
  name: 'BusinessListing',
  data() {
      return {
        companies: [],
        filtered_companies: [],
        serviceCategories: [],
        locations: [],
        service_category_choice: '',
        location_choice: '',
        query_string: 'Search: ',
        radio_sort: '',
      }
  },
  components: {
    CompanyBox
  },
  mounted() {
    this.initializeCompanies()
    this.getLocations()
    this.getServiceCategories()
    document.title = 'Business Listings'
  },
  computed: {
    getNumOfMatches: function () {
      return this.filtered_companies.length
    },
    filterLocations: function () {
      if (this.location_choice) {
        var temp_locations = this.locations.filter(i => (i.get_region.toLowerCase().indexOf(this.location_choice.toLowerCase()) !== -1)) 
        temp_locations = temp_locations.map(i => i.get_region)
      }else {
        var temp_locations = this.locations.map(i => i.get_region)
      }
      var temp_locations_array = [...new Set(temp_locations)]
      return temp_locations_array
    }
  },
  methods: {
    async initializeCompanies() {
      await axios
        .get('/api/v1/get-company-boxes/')
        .then(response => {
          this.companies = response.data
          this.filtered_companies = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    async getServiceCategories() {
      await axios
        .get('/api/v1/get-service-categories/')
        .then(response => {
          this.serviceCategories = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    async getLocations() {
      await axios
        .get('/api/v1/get-locations/')
        .then(response => {
          this.locations = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    async filterByRating() {
      this.filtered_companies = this.filtered_companies.sort((a, b) => b.get_rating - a.get_rating)
    },
    async filterByStarScore() {
    },
    async filterByRecentRating() {
      this.filtered_companies = this.filtered_companies.sort((a, b) => new Date(b.get_recent_rating) - new Date(a.get_recent_rating))
    },
    async filterByBestOfHomestars() {
    },
    async submitForm() {
      var location_company_list = []
      var service_company_list = []
      this.filtered_companies = this.companies
      this.query_string = 'Search:'
      if (this.service_category_choice){
        for (const i of this.service_category_choice.companies) {
          service_company_list.push(i)
        }
        this.filtered_companies = this.filtered_companies.filter(i => service_company_list.includes(i.id))
        this.query_string += ' ' + this.service_category_choice.name
      }
      if (this.location_choice){
        this.locations.forEach( i => {
          if (i.get_region.toLowerCase() === this.location_choice.toLowerCase() && !(location_company_list.includes(i.company))) {
            location_company_list.push(i.company)
          }
        })
        this.filtered_companies = this.filtered_companies.filter(i => location_company_list.includes(i.id))
        this.query_string += ' in ' + this.location_choice
      }
      if (!this.location_choice && !this.service_category_choice) {
        this.filtered_companies = this.companies
      }
      this.service_category_choice = ''
      this.location_choice = ''
    },
  }
}
</script>