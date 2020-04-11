<template>
  <div class="Footer">
      <div class="footer">

      </div>
  </div>
</template>

<script lang="ts">
  import { Vue, Component } from 'vue-property-decorator';

  @Component
  export default class FooterView extends Vue {
  }
</script>


<style scoped>
    .footer {
        height: 60px;
        background-color: #007bff!important;
        bottom: 0px;
        margin-top: 2%;
    }
</style>
