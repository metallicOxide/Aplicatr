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
  import { JobItem, CalendarBindingModel } from '../interfaces/bindingModels';
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

    clearCart(){
      this.cart = [];
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

      const calendarCart = this.getCalendarItemsFromJobCart();

      const calenderBindingModel: CalendarBindingModel = {
        jobs: calendarCart
      };

      console.log("about ot post", calenderBindingModel);

      const calendarRoute = ApiRoutes.calendarRoute;

      try 
      {
        const response = await axios.post(calendarRoute,
          calenderBindingModel,
          {params: {"token": this.jwtToken}}
        );
        console.log(response.data.calendar);
        this.createDownloadCalender(response.data.calendar);
        this.clearCart();
      } 

      catch (error) 
      {
        console.log(error);
        this.showAlert = true;
        this.error = error.data.message;
      }
    }

    // create a deep clone of the
    // cart and change date to choosen date
    getCalendarItemsFromJobCart() {
      // create a deep clone
      const cartClone: Array<JobItem> = JSON.parse(JSON.stringify(this.cart));
      cartClone.map(job => job.closing_date = this.selectedDate);
      return cartClone;
    }

    createDownloadCalender(calendarString: string) {
        const blob = new Blob([calendarString], { type: 'text/calender' })
        const link = document.createElement('a')
        link.href = URL.createObjectURL(blob)
        link.download= "calendar.ics"
        link.click()
        URL.revokeObjectURL(link.href)
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
