<template>
  <div class="NavBar">

    <b-navbar toggleable="lg" type="dark" variant="primary">
      <b-navbar-brand href="#"><b>Job Calendar Gen</b></b-navbar-brand>

    </b-navbar>
  </div>
</template>

<script lang="ts">
  import { Vue, Component, Prop } from 'vue-property-decorator';

  @Component
  export default class NavBarView extends Vue {
    @Prop() private isLoggedIn!: string;
  }
</script>


<style scoped>
  .user {
    color: white;
  } 
</style>
