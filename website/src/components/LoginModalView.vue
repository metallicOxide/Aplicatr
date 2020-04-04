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
      centered
      ok-only
      @show="resetModal"
      @hidden="resetModal"
      @ok="postLoginModalData"
    >
      <form ref="loginForm" @submit.stop.prevent="handleSubmit">
        <b-form-group>
          <b-alert v-model="errorMessage" v-show="errorMessage !== ''" variant="danger" fade dismissible>
            {{errorMessage}}
          </b-alert>
        </b-form-group>

        <b-form-group
          label="Login Name"
          label-for="id-input"
          invalid-feedback="Login Name is required"
        >
          <b-form-input
            id="id-input"
            v-model="credentials.Username"
            :state="formState.nameState"
            placeholder="Login Name"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group
          label="Password"
          label-for="id-input"
          invalid-feedback="Login Password is required"
        >
          <b-form-input
            id="id-input"
            v-model="credentials.Password"
            :state="formState.passwordState"
            placeholder="Password"
            required
          ></b-form-input>
        </b-form-group>

      </form>
    </b-modal>
  </div>
</template>

<script lang="ts">
  import { Component, Prop, Vue } from 'vue-property-decorator';
  import { Credentials, LoginBindingModel } from '../interfaces/bindingModels';
  import { errorMessages } from '../interfaces/messages';
  import { ApiRoutes } from '../interfaces/apiRoutes';
  import axios from 'axios';

  @Component
  export default class LoginModal extends Vue {
    @Prop() private credentials!: Credentials;

    errorMessage = "";

    formState = {
      nameState: true,
      passwordState: true
    };

    // Generates job request object to post to backend
    generateLoginRequest(): LoginBindingModel {
      const bindingModel: LoginBindingModel = {
        Username: this.credentials.Username,
        Password: this.credentials.Password,
        Uni: this.credentials.Uni
      }

      return bindingModel;
    }

    // 
    async postLoginModalData(e: Event): Promise<void> {
      e.preventDefault();
      this.errorMessage = "";

      if (!this.checkLoginModalValidity()) {
        return;
      }

      const isSuccess = await this.LoginAsync();
      console.log('isSuccess', isSuccess);
      if (isSuccess) {
        this.closeModal();
      }
    }

    // checks if the input userrname and pass are valid
    checkLoginModalValidity(): boolean {
        const isValidUser = !(!this.credentials.Username);
        const isvalidPass = !(!this.credentials.Password);
        this.formState = {
          nameState: isValidUser,
          passwordState: isvalidPass
        }
        return isValidUser && isvalidPass
    }

    // handles login and emitting of jobs to APP.vue
    async LoginAsync() {
      // create login model
      const bindingModel: LoginBindingModel = this.generateLoginRequest();
      const loginUrl: string = ApiRoutes.loginRoute;
      try {
        const response = await axios.post(loginUrl, bindingModel);
        // emit the scrapped job items back
        this.$emit('token', response.data.token);
        return true;
      } catch (error) {
        if (error.response.data.message) {
          this.errorMessage = error.response.data.message;
          console.log(this.errorMessage, error.response.data.message);
        } else {
          this.errorMessage = errorMessages.loginErrorMessage;
        }
        return false;
      }
    }

    // closes the modal
    closeModal() {
      this.$nextTick(() => {
        this.$bvModal.hide('modal-login');
      })
    }

    //TODO: see ifwe need to reset the username and password fields after
    resetModal() {
      console.log("credentials", this.credentials, this.credentials.Username, this.credentials.Password);
    }
  }
</script>