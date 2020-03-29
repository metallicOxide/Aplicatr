<template>
  <div class="NavBar">

    <b-navbar toggleable="lg" type="dark" variant="primary">
      <b-navbar-brand href="#">Job Calendar Gen</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">

          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
              <em>Hi, User</em>
            </template>
            <b-dropdown-item href="#">Sign Out</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script lang="ts">
  import { Vue } from 'vue-property-decorator';

  export default class NavBar extends Vue {

  }
</script>


<style scoped>

</style>
