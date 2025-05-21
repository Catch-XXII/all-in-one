<script setup lang="ts">
  import { ref } from 'vue';
  const rail = ref(true)

  import LoginButton from '@/components/LoginButton.vue';
  import RegisterButton from '@/components/RegisterButton.vue';
  import LoginForm from '@/components/LoginForm.vue';
  import RegisterForm from '@/components/RegisterForm.vue';
  import { useUIStore } from '@/stores/ui'
  const ui = useUIStore()

  import { useAuthStore } from '@/stores/auth'
  const auth = useAuthStore()
</script>

<template>
  <v-app-bar class="" :elevation="1" :rail="rail" rounded>
    <template #prepend>
      <v-app-bar-nav-icon v-if="auth.isLoggedIn" @click="ui.toggleDrawer()" />
    </template>

    <v-app-bar-title>QAsis</v-app-bar-title>

    <template #append>
      <LoginButton v-if="!auth.isLoggedIn" />
      <RegisterButton v-if="!auth.isLoggedIn" />

      <v-btn icon="mdi-heart" rounded="xl" />

      <v-dialog v-model="ui.loginDialog" max-width="500">
        <LoginForm />
      </v-dialog>

      <v-dialog v-model="ui.registerDialog" max-width="500">
        <RegisterForm />
      </v-dialog>

    </template>
  </v-app-bar>
</template>

<style scoped lang="sass">

</style>
