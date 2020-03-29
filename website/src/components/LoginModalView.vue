<template>
  <div class="LoginModal">
    <b-container> 
      <JobListView v-bind:jobList="jobList" v-bind:title="title"/>
    </b-container>
  </div>
</template>

<script lang="ts">
  import { Component, Prop, Vue } from 'vue-property-decorator';

  @Component
  export default class LoginModal extends Vue {
    @Prop() private title!: string;

  }
</script>