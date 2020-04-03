<template>
  <div class="SearchBar">
      Search term is {{searchTerm}}
  </div>
</template>

<script lang="ts">
  import { Component, Prop, Vue } from 'vue-property-decorator';

  @Component
  export default class SearchBar extends Vue {
    @Prop() private searchTerm!: string;
    
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
