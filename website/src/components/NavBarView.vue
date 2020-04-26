<template>
  <div class="NavBar">

    <div class="header">
      <ButtonAnimation width="300">
        <a id="about-us" href="#">
          <span>About Us</span>
        </a>
        <a id="job-portals" href="#">
          <span>Job Portals</span>
        </a>
      </ButtonAnimation>
      <a class="MainTitle" href="#">Aplicatr</a>
    </div>
  </div>
</template>

<script lang="ts">
  import { Vue, Component } from 'vue-property-decorator';
  import { Push } from 'vue-burger-menu'

  @Component({
    components: {
      ButtonAnimation: Push
    },
  })
  export default class NavBarView extends Vue {
  }
</script>


<style>
  .user {
    color: white;
  } 

  .header {
    width:100%;
    height: 60px;
    background-color: #303f9f !important;
    display:flex;
    flex-direction: row;
  }

  .MainTitle {
    padding-top: 12px;
    font-weight: bold;
    color: rgb(221, 221, 221);
    font-size: 25px;
    text-decoration: none;
    order: 2;
    transition: filter 300ms;
    margin-left: 100px;
  }

  .MainTitle:hover {
    text-decoration: none;
    filter: brightness(1.5);
    color: #fff;
  }

  .bm-burger-button {
    top: 15px;
    order: 1;
    transform: scale(0.8);
  }

  .bm-burger-bars {
    background-color: #ddd;
  }

  .bm-menu {
    background-color: #303f9f !important;
  }

</style>
