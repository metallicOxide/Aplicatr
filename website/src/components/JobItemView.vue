<template>
  <div class="JobItem">
    <div :class="getPiorityStyling + ' job-card'">
      <b-row class="job-item-element job-heading-container">
        <b-col cols="10">
          <div class="job-heading float-left">
            {{formattedJobTitle}}
          </div>
        </b-col>
        <b-col cols="2">
          <b-icon-bookmark class="bookmark-icon" 
            font-scale="1.8"
            ></b-icon-bookmark>
        </b-col>
        <b-col cols="10">
          <div class="job-days-left float-left">
            {{dayLeftMsg}}
          </div>
        </b-col>
      </b-row>
      <b-row class="job-item-element">
        <b-col sm="10">
          <div class="float-left job-description">
            {{description}}
          </div>
        </b-col>
      </b-row>
      <b-row class="job-item-element">
        <b-col sm="10">
          <div class="job-location float-left">
            <b-icon-map></b-icon-map>
            {{location}}
          </div>
        </b-col>
        <b-col sm="2">
          <div class="float-left">
            <a :href="url" class="card-link">Link to Job</a>
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
  export default class JobItemView extends Vue {
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

    get description (): string {
      const job: JobItem = this.jobItem;
      return job.summary;
    }

    get url (): string {
      const job: JobItem = this.jobItem;
      return job.link;
    }

    get daysTillExpiry(): number {
      const now = moment();
      const endDate = moment(this.jobItem.closing_Date);
      return endDate.diff(now, 'days');
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
      const endDateObj = moment(this.jobItem.closing_Date);
      const endDate = endDateObj.format("DD/MM/YYYY");
      if (days >= 0) {
        return `${endDate} - ${this.daysTillExpiry} days left!`;
      } else {
        return `${endDate} - Expired :'(`;
      }
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

  .job-card {
    border-radius: 20px;
  }

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

  .bookmark-icon:hover {
    color:aqua;
  }

  .job-heading-container {
    padding-top: 10px;
    font-size: 20px;
  }

  .job-heading {
    font-weight: bold;
  }

  .job-description {
    text-align: left;
  }

  .job-days-left {
    font-size: 12px;
    font-weight: bolder;
  }

  .job-location {
    font-weight: bold;
  }
</style>
