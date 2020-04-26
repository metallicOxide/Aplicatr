<template>
    <div class="footer">

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
        height: 45px;
        background-color: #303f9f !important;
        bottom: 0;
        margin-top: 2%;
        width: 100%;
    }
</style>
