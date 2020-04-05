<template>
  <div class="Cart">
    <b-navbar toggleable="lg" type="dark" variant="primary">
      <b-navbar-brand href="#"><b>Job Calendar Gen</b></b-navbar-brand>
    </b-navbar>
  </div>
</template>

<script lang="ts">
  import { Vue, Component } from 'vue-property-decorator';

  @Component
  export default class CartView extends Vue {
  }
</script>


<style scoped>
  .user {
    color: white;
  } 
</style>
