<template>
  <div id="app">
      <NavBarView/>
      <main id="page-wrap">
        <b-container>
          <LoginModal @token="getToken" 
            v-bind:credentials="credentials"
            ref="loginModal"
          />
          <SearchBar v-bind:jobSearch="jobSearch" 
            v-bind:jwtToken="jwtToken"
            @jobs="getJobs"
            @login="handleLoginRequest"
          />
          <CombinedJobCartView v-bind:jwtToken="jwtToken" 
            v-bind:jobList="jobs" 
            v-bind:cart="cart"
            @login="handleLoginRequest"
            @updateJobList="updateJobList"/>
        </b-container>
      </main>
      <Footer class="footer" />
  </div>
</template>

<script lang="ts">
  import { Component, Vue } from 'vue-property-decorator';
  import CombinedJobCartView from './components/CombinedJobCartView.vue';
  import { JobItem, LoginBindingModel, SearchBindingModel } from './interfaces/bindingModels';
  import NavBarView from './components/NavBarView.vue';
  import LoginModal from './components/LoginModalView.vue';
  import SearchBar from './components/SearchBar.vue';
  import Footer from './components/FooterView.vue';

  @Component({
    components: {
      CombinedJobCartView,
      NavBarView,
      LoginModal,
      SearchBar,
      Footer
    },
  })

  export default class App extends Vue {
    // jobs: Array<JobItem> = [
    //   {
    //     closing_date: "2020-03-28 12:00:00",
    //     company: "Jane street",
    //     title: "Full stacc dev",
    //     location: "Sydney",
    //     summary: "Jane Street is a proprietary trading firm that operates around the clock and around the globe. We bring a deep understanding of markets, a scientific approach, and innovative technology to bear on the problem of trading profitably in the world's highly competitive financial markets.",
    //     link: "//www.google.com",
    //   }, 
    //   {
    //     closing_date: "2020-04-11 12:00:00",
    //     title: "Python dev",
    //     company: "Atlassian",
    //     location: "Canada",
    //     summary: "We need some good ppls",
    //     link: "//www.google.com",
    //   },
    //   {
    //     closing_date: "2020-03-05 12:00:00",
    //     title: "Frontend dev",
    //     company: "Atlassian",
    //     location: "Sydney",
    //     summary: "Angular experience preferred",
    //     link: "//www.google.com",
    //   }, 
    //   {
    //     closing_date: "2020-12-16 12:00:00",
    //     title: "Backend dev",
    //     company: "Atlassian",
    //     location: "Sydney",
    //     summary: "C# Asp.Net Dev",
    //     link: "//www.google.com",
    //   },      
    //   {
    //     closing_date: "2020-03-28 12:00:00",
    //     title: "Full stacc dev",
    //     company: "Atlassian",
    //     location: "Sydney",
    //     summary: "Jane Street is a proprietary trading firm that operates around the clock and around the globe. We bring a deep understanding of markets, a scientific approach, and innovative technology to bear on the problem of trading profitably in the world's highly competitive financial markets.",
    //     link: "//www.google.com",
    //   }, 
    //   {
    //     closing_date: "2020-04-11 12:00:00",
    //     title: "Python dev",
    //     company: "Jane Street",
    //     location: "Canada",
    //     summary: "We need some good ppls",
    //     link: "//www.google.com",
    //   }
    // ];

    jobs: Array<JobItem> = [
    ];

    cart: Array<JobItem> = [
    ];

    jobSearch: SearchBindingModel = {
      Keywords: "",
      Location: ""
    };

    // Set the uni as UNSW for now
    credentials: LoginBindingModel = {
      Username: "",
      Password: "",
      Uni: "UNSW"
    };

    jwtToken = "";

    getToken(token: string) {
      this.jwtToken = token;
    }

    getJobs(allJobs: Array<JobItem>) {
      this.jobs = allJobs;
    }

    handleLoginRequest() {
      this.$root.$emit('login');
    }

    updateJobList(jobList: Array<JobItem>) {
      this.jobs = jobList;
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

html, body {
  height: 100%;
}

html, body {
  background-color: #fff;
}

.footer {
  bottom:0;
  position:absolute;
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

.bm-overlay {
  background: #fff;
}

@media (min-width: 1500px) {
    .container{
        max-width: 1250px !important;
    }
}

@media (max-width: 765px) {
    .footer {
      display: none;
    }
}

</style>
