<template>
  <div class="JobList">
    <b-row>
      <b-col md="12" v-bind:key="jobItem.id" v-for="jobItem in jobList">
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
    @Prop() private title!: string;
    @Prop() private jobList!: Array<JobItem>;

  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
