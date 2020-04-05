<template>
  <b-card
    header="Your Job Cart"
    header-text-variant="white"
    header-bg-variant="primary"
  >
    <b-list-group flush>
      <b-list-group-item class="scrollable">
        <div v-for="(cartItem, index) in cart" v-bind:key="`job-${index}`">
          <CartItemView v-bind:jobItem="cartItem"/>
        </div>
      </b-list-group-item>
      <b-list-group-item>
        <div>
            <label for="datepicker-buttons"><b>Pick a Date to be Reminded</b></label>
            <b-form-datepicker
            id="datepicker-buttons"
            reset-button
            close-button
            locale="en"
            min="initialDay"
            required
            ></b-form-datepicker>
        </div>
      </b-list-group-item>
    </b-list-group>

    <b-card-footer>
        <b-button variant="outline-primary">Generate Jobs</b-button>
    </b-card-footer>

  </b-card>
</template>

<script lang="ts">
  import { Vue, Component, Prop } from 'vue-property-decorator';
  import { JobItem } from '../interfaces/bindingModels';
  import CartItemView from '../components/CartItemView.vue';

  @Component ({
      components: {
        CartItemView
      }
  })
  export default class CartView extends Vue {
      @Prop () private cart!: Array<JobItem>;
      initialDay = Date.now();
  }
</script>


<style scoped>
    .card-header {
        font-weight: bold;
    }
    
    .scrollable {
        max-height: 300px;
        overflow-y: scroll;
    }
</style>
