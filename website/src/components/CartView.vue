<template>
  <div class="Cart">
    <div v-show="error">
      <b-alert variant="danger" v-model="showAlert" dismissible>{{error}}</b-alert>
    </div>

    <b-card
      header="Your Job Cart"
      header-text-variant="white"
      header-bg-variant="primary"
    >
      <b-list-group flush>
        <b-list-group-item class="scrollable">
          <div v-for="(cartItem, index) in cart" v-bind:key="`job-${index}`">
            <CartItemView @removeFromCart="removeFromCart" v-bind:jobItem="cartItem"/>
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
              v-model="selectedDate"
              required
              ></b-form-datepicker>
          </div>
        </b-list-group-item>
      </b-list-group>

      <b-card-footer>
          <b-button variant="outline-primary" @click="postJobCart">Generate Jobs</b-button>
      </b-card-footer>

    </b-card>

  </div>
</template>

<script lang="ts">
  import { Vue, Component, Prop } from 'vue-property-decorator';
  import { JobItem, CalendarItemBindingModel, CalendarBindingModel } from '../interfaces/bindingModels';
  import CartItemView from '../components/CartItemView.vue';
  import { ApiRoutes } from '../interfaces/apiRoutes';
  import axios from 'axios';

  @Component ({
      components: {
        CartItemView
      }
  })
  export default class CartView extends Vue {
    @Prop () private cart!: Array<JobItem>;
    @Prop () private jwtToken!: string;

    showAlert = false;
    selectedDate = null;
    error = "";

    removeFromCart(jobItem: JobItem) {
      this.$emit('removeFromCart', jobItem);
    }

    convertJobItemToCalendarItem (jobItem: JobItem): CalendarItemBindingModel {
      const model: CalendarItemBindingModel = {
        title: jobItem.title,
        link: jobItem.link,
        summary: jobItem.summary,
        chosen_date: jobItem.closing_date,
        location: jobItem.location
      } 
      return model;
    }

    async postJobCart() {
      console.log("post jobs");
      this.showAlert = false;
      this.error = "";
      
      if (this.cart.length < 1) {
        this.showAlert = true;
        this.error = "Please select at least one Job";
        return;
      }

      if (this.selectedDate === null) {
        this.showAlert = true;
        this.error = "Please select a day to be alerted";
        return;
      }

      if (!this.jwtToken) {
        this.$emit('login');
      }

      const calendarItemList: Array<CalendarItemBindingModel> = this.cart.map((c) => this.convertJobItemToCalendarItem(c));
      const calenderBindingModel: CalendarBindingModel = {
        jobs: calendarItemList
      };

      const calendarRoute = ApiRoutes.calendarRoute;
      try {

        const response = await axios.post(calendarRoute,
          calenderBindingModel,
          {params: {"token": this.jwtToken}}
        );

        console.log(response);
      } 

      catch (error) 
      {
        console.log(error);
      }
    }

  }
</script>


<style scoped>
    .card-header {
        font-weight: bold;
    }
    
    .scrollable {
        max-height: 350px;
        overflow-y: scroll;
    }
</style>
