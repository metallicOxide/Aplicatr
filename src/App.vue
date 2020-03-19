<template>
  <div id="app">
    <b-container> 
      <img alt="Vue logo" src="./assets/logo.png">
      <JobListView v-bind:jobList="jobList" v-bind:title="title"/>
    </b-container>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import JobListView from './components/JobListView.vue';
import { JobItem } from './interfaces/bindingModels';

@Component({
  components: {
    JobListView,
  },
})
export default class App extends Vue {
  jobList: Array<JobItem> = [
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
</style>
