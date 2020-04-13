<template>
  <div class="CartItem">
    <div :class="getPiorityStyling + ' job-card'">
      <b-row class="job-item-element job-heading-container">
        <b-col cols="9">
          <div class="job-heading float-left">
            {{formattedJobTitle}}
          </div>
        </b-col>
        <b-col cols="3">
          <b-icon-trash class="trash-icon" 
            @click="deleteFromCart"
            font-scale="1.6"
            ></b-icon-trash>
        </b-col>
        <b-col cols="10">
          <div class="job-company float-left">
            {{company}}
          </div>
        </b-col>
        <b-col cols="10">
          <div class="job-days-left float-left">
            {{dayLeftMsg}}
          </div>
        </b-col>
      </b-row>
    </div>
  </div>
</template>

<script lang="ts">
  import { Component, Prop, Vue } from 'vue-property-decorator';
  import { JobItem } from '../interfaces/bindingModels';
  import moment from 'moment';

  @Component
  export default class CartItemView extends Vue {
    @Prop() private jobItem!: JobItem;
    // styling array to decide what style the cards should be 
    stylingArr: string[] = ["low-pior", "med-pior", "high-pior", "expired-pior"];

    get formattedJobTitle (): string {
      // const job: JobItem = this.jobItem;
      // return `${job.jobTitle} - ${job.jobCompany}`;
      const job: JobItem = this.jobItem;
      return job.title;
    }

    get location(): string {
      const job: JobItem = this.jobItem;
      return job.location;
    }

    get daysTillExpiry(): number {
      const now = moment();
      const endDate = moment(this.jobItem.closing_date, "YYYY-MM-DD HH:mm:ss");
      return endDate.diff(now, 'days');
    }

    get company (): string {
      const job: JobItem = this.jobItem;
      return job.company;
    }


    get getPiorityStyling(): string {
      const days = this.daysTillExpiry;
      // if the floor is >= 3 then return 2 (low pior)
      // floor is <= 0 then return 0 (high pior)
      if (days >= 30) {
        return this.stylingArr[0];
      } else if (days >= 15) {
        return this.stylingArr[1];
      } else if (days > 0) {
        return this.stylingArr[2];
      } else {
        return this.stylingArr[3];
      }
    }

    get dayLeftMsg(): string {
      const days = this.daysTillExpiry;
      const endDateObj = moment(this.jobItem.closing_date);
      const endDate = endDateObj.format("DD/MM/YYYY");
      if (days >= 0) {
        return `${endDate} - ${this.daysTillExpiry} days left!`;
      } else {
        return `${endDate} - Expired :'(`;
      }
    }

    deleteFromCart() {
      this.$emit('removeFromCart', this.jobItem);
    }

  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .JobItem {
    padding-bottom: 10px;
  }
  /*Job Item priority styling*/
  .low-pior {
    background-color: #28a745;
    color: #fff;
  }

  .med-pior {
    background-color: #ffc119;
    color: #fff;
  }

  .high-pior {
    background-color: #dc3545;
    color: #fff;
  }

  .expired-pior {
    background-color: #6c757d;
    color: #fff;
  }
  /*Job Item priority styling*/
  .job-item-element {
    padding-left: 5%;
    padding-bottom: 10px;
  }

  a {
    text-decoration: underline;
    color: #fff;
  }

  a:hover {
    color:aqua;
  }

  .trash-icon:hover {
    color:aqua;
  }

  .job-heading-container {
    text-align: left;
    padding-top: 10px;
    font-size: 15px;
  }

  .job-heading {
    font-weight: bold;
  }

  .job-days-left {
    font-size: 12px;
    font-weight: bolder;
  }

  .job-company {
    font-size: 14px;
    text-decoration: underline;
    margin-top: -5px;
    padding-bottom: 5px;
  }
</style>
