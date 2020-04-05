<template>
  <div class="JobList">
    <b-row>
      <b-col md="8">
        <div class="text-center" v-if="jobList.length < 1">
          <b-spinner class="large-spinner" variant="primary" label="Text Centered">Fetching Jobs</b-spinner>
        </div>
        <div v-for="(jobItem, index) in jobList" v-bind:key="`job-${index}`">
          <JobItemView v-bind:jobItem="jobItem"/>
        </div>
      </b-col >
      <b-col md="4">
          <CartView class="cart" v-bind:cart="cart"/>
      </b-col >
    </b-row>
  </div>
</template>

<script lang="ts">
  import { Component, Prop, Vue } from 'vue-property-decorator';
  import { JobItem } from '../interfaces/bindingModels';
  import JobItemView from '../components/JobItemView.vue';
  import CartView from '../components/CartView.vue';
  

  @Component({
    components: {
      JobItemView,
      CartView
    },
  })
  export default class CombinedJobCartView extends Vue {
    @Prop() private jobList!: Array<JobItem>;
    @Prop() private cart!: Array<JobItem>;
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .large-spinner {
    width: 5rem;
    height: 5rem;
  }

  .cart {
    position: sticky;
    top: 15px;
  }

</style>
