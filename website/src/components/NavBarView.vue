<template>
  <div class="NavBar">

    <b-navbar toggleable="lg" type="dark" variant="primary">
      <b-navbar-brand href="#"><b>Job Calendar Gen</b></b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">

          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
              <em class="user"><b>Hi, User</b></em>
            </template>
            <b-dropdown-item href="#">Sign Out</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script lang="ts">
  import { Vue, Component, Prop } from 'vue-property-decorator';

  @Component
  export default class NavBarView extends Vue {
    @Prop() private isLoggedIn!: string;
  }
</script>


<style scoped>
  .user {
    color: white;
  } 
</style>
