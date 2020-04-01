<template>
  <div id="app">
    <NavBarView v-bind:isLoggedIn="loggedIn"/>
    <LoginModal />
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
        jobDes: "Join our team of fun loving people",
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

    // Set the uni as UNSW for now
    credentials: Credentials = {
      Username: "",
      Password: "",
      Uni: "UNSW"
    };
    
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
  background-color: #ddd;
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
  background-color: #00d2ff;
  background-image: linear-gradient(to top, #00d2ff 0%, #3a7bd5 100%);
}

</style>
