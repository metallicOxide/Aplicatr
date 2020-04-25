<template>
  <div class="JobList">
    <b-row>
      <b-col md="8" class="fixed-height-job-items">
        <div class="text-center" v-if="localJobList.length < 1">
          <b-spinner class="large-spinner" variant="primary" label="Text Centered">Fetching Jobs</b-spinner>
        </div>
        <div v-for="(jobItem, index) in localJobList" v-bind:key="`job-${index}`">
          <JobItemView @saveJobClick="saveJobClick" v-bind:jobItem="jobItem"/>
        </div>
      </b-col >
      <b-col md="4">
          <CartView class="cart"
            @removeFromCart="removeFromCart"
            @login="emitLoginRequest"  
            v-bind:cart="localCart"
            v-bind:jwtToken="jwtToken"/>
      </b-col >
    </b-row>
  </div>
</template>

<script lang="ts">
  import { Component, Prop, Vue, Watch } from 'vue-property-decorator';
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
    @Prop() private jwtToken!: string;

    localCart = this.cart;
    localJobList = this.jobList;

    @Watch('jobList', { immediate: true, deep: true })
    onCartChanged(val: Array<JobItem>) {
      this.localJobList = val;
    }

    saveJobClick(jobItem: JobItem) {
      this.localJobList = this.localJobList.filter( (j) => this.genJobItemPrimeKey(j) !== this.genJobItemPrimeKey(jobItem));

      this.localCart = this.localCart.filter( (j) => this.genJobItemPrimeKey(j) !== this.genJobItemPrimeKey(jobItem));

      this.localCart.push(jobItem); 
    }

    removeFromCart(jobItem: JobItem) {
      this.localCart = this.localCart.filter( (j) => this.genJobItemPrimeKey(j) !== this.genJobItemPrimeKey(jobItem));

      this.localJobList = this.localJobList.filter( (j) => this.genJobItemPrimeKey(j) !== this.genJobItemPrimeKey(jobItem));

      this.localJobList.push(jobItem); 
    }

    genJobItemPrimeKey(job: JobItem) {
      return job.title + job.location + job.company + job.closing_date;
    }

    emitLoginRequest() {
      this.$emit("login");
    }

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

  .fixed-height-job-items {
    max-height: 40rem;
    overflow-y: scroll;
  }

</style>
