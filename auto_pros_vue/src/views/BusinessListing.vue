<template>
  <div class="business-listing" id="app">
    <Navbar></Navbar>
    <form class="form-inline" @submit.prevent="submitForm" novalidate>
      <div class="control" id="search-service">
        <input placeholder="What would you like help with?" class="input" type="search" v-model="service_choice" list="filtered-service-list">
        <datalist id="filtered-service-list">
          <option v-for="service in filterServiceQueries" >{{ service }}</option>
        </datalist>
      </div>
      <div class="control">
        <p> near </p>
      </div>
      <div class="control">
        <input class="input" type="search" v-model="location_choice" list="filtered-location-list">
        <datalist id="filtered-location-list">
          <option v-for="location in filterLocations" >{{ location }}</option>
        </datalist>
      </div>
      <div class="control">
        <button class="button" id="icon-button"><i class="fa fa-search"></i></button>
      </div>
    </form>
    <div id="navbar-tabs">
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
    <div class="columns is-mobile" id="columns-filter">
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
                <input type="radio" v-on:click="filterByRating" id="radio-sort" name="radio-sort">
                  Avg Custom Rating
              </label>
              <br>
              <label class="radio">
                <input type="radio" v-on:click="filterByRecentRating" id="radio-sort" name="radio-sort">
                  Recently Reviewed
              </label>
            </div>
          </div>
        </div>
      </div> 
    </div>
    <div class="business-boxes">
      <div class="box" id="borderBox-companies">
        <div class="columns is-multiline is-variable is-mobile is-0">
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
#navbar-tabs {
  width: 100%;
  background-color: white;
}
.control {
  margin-right: 1rem;
}
.form-inline {  
  display: flex;
  width: 100%;
  margin-left: 1rem;
  flex-flow: row wrap;
  align-items: center;
  padding-top: 1rem;
  padding-bottom: 1rem;
}
#search-service {
  width: 20%;
  min-width: 95px;
}
#radio-sort {
  width: 1rem;
  vertical-align: middle;
}
.tabs {
  padding-top: 1rem;
  margin-left: 1rem;
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
  width: 50%;
  height: 50%;
}
#borderBox-companies {
    height: 100%;
    width: 100%;
    border-radius:0rem;
    overflow: auto;
    margin-left: 1rem;
}
#icon-button {
  border-radius:0.2rem;
  border: none;
  width: 2.5rem;
  height: 2.5rem;
  background-color: #3273dc;
  margin-bottom: 0;
}
#columns-filter {
  width:70%;
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
  height:80%;
  font-size:2rem;
  margin-left:1rem;
  text-align: left;
  vertical-align: middle;
}
.card-content {
  padding: 0.5rem 0rem 0.5rem 0.5rem;
  background-color:white;
  text-align: left;
}
</style>

<script>
import axios from 'axios'
import CompanyBox from '@/components/CompanyBox'
import Navbar from '@/components/Navbar'

export default {
  name: 'BusinessListing',
  data() {
      return {
        companies: [],
        filtered_companies: [],
        service_queries: [],
        services: [],
        locations: [],
        service_choice: '',
        location_choice: '',
        query_string: 'Search: ',
        radio_sort: '',
      }
  },
  components: {
    CompanyBox,
    Navbar
  },
  mounted() {
    this.initializeCompanies()
    this.initializeLocations()
    this.initializeServices()
    document.title = 'Business Listings'
  },
  computed: {
    getNumOfMatches: function () {
      return this.filtered_companies.length
    },
    filterLocations: function () {
      if (this.location_choice) {
        var temp_locations = this.locations.filter(location => (location.get_region.toLowerCase().indexOf(this.location_choice.toLowerCase()) !== -1)) 
        temp_locations = temp_locations.map(location => location.get_region)
      }else {
        var temp_locations = this.locations.map(location => location.get_region)
      }
      var temp_locations_array = [...new Set(temp_locations)]
      return temp_locations_array
    },
    filterServiceQueries: function () {
      if (this.service_choice) {
        var temp_services = this.service_queries.filter(service => (service.name.toLowerCase().indexOf(this.service_choice.toLowerCase()) !== -1)) 
        temp_services = temp_services.map(service => service.name)
      }else {
        var temp_services = this.service_queries.map(service => service.name)
      }
      var temp_services_array = [...new Set(temp_services)]
      return temp_services_array
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
    async initializeServices() {
      await axios
        .get('/api/v1/get-services/')
        .then(response => {
          this.services = response.data
          this.service_queries = this.services.filter(leafService => !(this.services.filter(service => service.parent == leafService.id)).length).sort((a, b) => (a.name < b.name))
        })
        .catch(error => {
          console.log(error)
        })
    },
    async initializeLocations() {
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
    async filterByRecentRating() {
      this.filtered_companies = this.filtered_companies.sort((a, b) => new Date(b.get_recent_rating) - new Date(a.get_recent_rating))
    },
    async submitForm() {
      this.filtered_companies = this.companies
      this.query_string = 'Search: '
      if (this.service_choice) {
        var service_company_list = []
        var current_service = this.services.find(service => service.name.toLowerCase() == this.service_choice.toLowerCase())
        if (current_service) {
          while (true) {
            current_service.get_companies.forEach(company => {
              if (!(service_company_list.includes(company))) {
                service_company_list.push(company)
              }
            })
            if (current_service.parent != null) {
              current_service = this.services.find(service => service.id == current_service.parent)
            } else {
              break
            }
          }
        }
        this.filtered_companies = this.filtered_companies.filter(company => service_company_list.includes(company.id))
        this.query_string += ' ' + this.service_choice
      }
      if (this.location_choice) {
        var location_company_list = []
        this.locations.forEach( location => {
          if (location.get_region.toLowerCase() === this.location_choice.toLowerCase() && !(location_company_list.includes(location.company))) {
            location_company_list.push(location.company)
          }
        })
        this.filtered_companies = this.filtered_companies.filter(company => location_company_list.includes(company.id))
        this.query_string += ' in ' + this.location_choice
      }
      if (!this.location_choice && !this.service_choice) {
        this.filtered_companies = this.companies
      }
      this.service_choice = ''
      this.initializeServices()
      this.location_choice = ''
    }
  }
}
</script>