<template>
  <div class="LoginModal">
    <b-button v-b-modal.modal-login>Open Modal</b-button>
    <b-modal
      id="modal-login"
      ref="modal"
      size="lg"
      title="Login"
      header-bg-variant="primary"
      header-text-variant="light"
      centered = "true"
      @show="resetModal"
      @hidden="resetModal"
      @ok="handleOk"
    >
      <form ref="form" @submit.stop.prevent="handleSubmit">
        <b-form-group
          :state="nameState"
          label="Login Name"
          label-for="id-input"
          invalid-feedback="Login Name is required"
        >
          <b-form-input
            id="id-input"
            v-model="name"
            :state="nameState"
            required
          ></b-form-input>
        </b-form-group>
        <b-form-group
          :state="nameState"
          label="Login Name"
          label-for="id-input"
          invalid-feedback="Login Name is required"
        >
          <b-form-input
            id="id-input"
            v-model="name"
            :state="nameState"
            required
          ></b-form-input>
        </b-form-group>
      </form>
    </b-modal>
  </div>
</template>

<script lang="ts">
  import { Component, Prop, Vue } from 'vue-property-decorator';

  @Component
  export default class LoginModal extends Vue {
    @Prop() private username!: string;
    @Prop() private password!: string;

    resetModal() {
      console.log("OPen modal");
    }
  }
</script>