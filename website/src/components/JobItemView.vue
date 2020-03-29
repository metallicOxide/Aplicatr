<template>
  <div class="JobItem">
    <b-card :title="formattedJobTitle" :sub-title="dayLeftMsg" :class="getPiorityStyling">
      <b-card-text>
        {{jobItem.jobDes}}
      </b-card-text>
      <b-card-text>
        <b-icon-map></b-icon-map>
        {{jobItem.jobLoc}}
      </b-card-text>
      <a :href="jobItem.jobUrl" class="card-link">Link to Job</a>
    </b-card>
  </div>
</template>

<script lang="ts">
  import { Component, Prop, Vue } from 'vue-property-decorator';
  import { JobItem } from '../interfaces/bindingModels';
  import moment from 'moment';

  @Component
  export default class JobItemView extends Vue {
    @Prop() private jobItem!: JobItem;
    // styling array to decide what style the cards should be 
    stylingArr: string[] = ["low-pior", "med-pior", "high-pior", "expired-pior"];

    get formattedJobTitle (): string {
      const job: JobItem = this.jobItem;
      return `${job.jobTitle} - ${job.jobCompany}`;
    }

    get daysTillExpiry(): number {
      const now = moment();
      const endDate = moment(this.jobItem.endDate, "DD/MM/YYYY");
      return endDate.diff(now, 'days');
    }

    get getPiorityStyling(): string {
      const days = this.daysTillExpiry;
      // if the floor is >= 3 then return 2 (low pior)
      // floor is <= 0 then return 0 (high pior)
      if (days >=30) {
        return this.stylingArr[0];
      } else if (days >= 20) {
        return this.stylingArr[1];
      } else if (days >= 10) {
        return this.stylingArr[2];
      } else {
        return this.stylingArr[3];
      }
    }

    get dayLeftMsg(): string {
      const days = this.daysTillExpiry;

      if (days >= 0) {
        return `${this.jobItem.endDate} - ${this.daysTillExpiry} days left!`;
      } else {
        return `${this.jobItem.endDate} - Expired :'(`;
      }
    }

  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .JobItem {
    margin-bottom: 10px;
    font-weight: bold;
  }

  .card-subtitle, .card-title {
    font-weight: bold;
  }

  .card {
    border:1px solid #ccc!important;
    border-radius: 16px;
  }

  .card-subtitle {
    color: inherit !important;
  }

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

  a {
    text-decoration: underline;
    color: #fff;
  }
</style>
