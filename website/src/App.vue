<template>
  <div id="app">
    <NavBarView v-bind:isLoggedIn="loggedIn"/>
    <LoginModal @jobItems="populateJobs" v-bind:credentials="credentials"/>
    <SearchBar v-bind:searchTerm="searchTerm"/>
    <b-container>
      <JobListView v-bind:jobList="jobs" v-bind:title="title"/>
    </b-container>
  </div>
</template>

<script lang="ts">
  import { Component, Vue } from 'vue-property-decorator';
  import JobListView from './components/JobListView.vue';
  import { JobItem, Credentials } from './interfaces/bindingModels';
  import NavBarView from './components/NavBarView.vue';
  import LoginModal from './components/LoginModalView.vue';

  @Component({
    components: {
      'JobListView': JobListView,
      'NavBarView': NavBarView,
      'LoginModal': LoginModal
    },
  })
  export default class App extends Vue {
    jobs: Array<JobItem> = [
      {
        id: "1",
        endDate: "28/03/2020",
        jobTitle: "Full stacc dev",
        jobCompany: "@lassian",
        jobType: "Computer Science",
        jobLoc: "Sydney",
        jobDes: "Jane Street is a proprietary trading firm that operates around the clock and around the globe. We bring a deep understanding of markets, a scientific approach, and innovative technology to bear on the problem of trading profitably in the world's highly competitive financial markets.",
        jobUrl: "//www.google.com",
      }, 
      {
        id: "2",
        endDate: "11/04/2020",
        jobTitle: "Python dev",
        jobCompany: "Maccas",
        jobType: "Computer Science",
        jobLoc: "Canada",
        jobDes: "We need some good ppls",
        jobUrl: "//www.google.com",
      },
      {
        id: "3",
        endDate: "05/03/2020",
        jobTitle: "Frontend dev",
        jobCompany: "NASA",
        jobType: "Computer Science",
        jobLoc: "Sydney",
        jobDes: "Angular experience preferred",
        jobUrl: "//www.google.com",
      }, 
      {
        id: "4",
        endDate: "16/12/2020",
        jobTitle: "Backend dev",
        jobCompany: "Canva",
        jobType: "Computer Science",
        jobLoc: "Sydney",
        jobDes: "C# Asp.Net Dev",
        jobUrl: "//www.google.com",
      }
    ];

    title = 'Job List';

    loggedIn = false;

    searchTerm = "";

    // Set the uni as UNSW for now
    credentials: Credentials = {
      Username: "qwe",
      Password: "qwe",
      Uni: "UNSW"
    };

    populateJobs(jobs: any) {
      console.log(jobs);
      this.jobs = jobs;
    }
    
  }
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#app {
  margin-top: 0px;
}

/* scroll bar styling */
::-webkit-scrollbar {
  width: 5px;
}

/* Track */
::-webkit-scrollbar-track {
  background: #eee;
}

/* Handle */
::-webkit-scrollbar-thumb {
  border-radius: 1rem;
  background-color: #3a7bd5;
  background-image: linear-gradient(to top, #3a7bd5 0%, #00d2ff 100%);
}

</style>
