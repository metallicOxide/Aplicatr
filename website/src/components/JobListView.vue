<template>
  <div class="JobList">
    <b-row>
      <b-col md="8" v-for="(jobItem, index) in jobList" v-bind:key="`job-${index}`">
        <JobItemView v-bind:jobItem="jobItem"/>
      </b-col >
    </b-row>
  </div>
</template>

<script lang="ts">
  import { Component, Prop, Vue } from 'vue-property-decorator';
  import { JobItem } from '../interfaces/bindingModels';
  import JobItemView from '../components/JobItemView.vue';

  @Component({
    components: {
      JobItemView,
    },
  })
  export default class JobListView extends Vue {
    @Prop() private jobList!: Array<JobItem>;
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
