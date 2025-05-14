<script setup lang="ts">
  import { ref } from 'vue';
  const rail = ref(true)

  import LoginButton from '@/components/LoginButton.vue';
  import RegisterButton from '@/components/RegisterButton.vue';
  import LoginForm from '@/components/LoginForm.vue';
  import RegisterForm from '@/components/RegisterForm.vue';
  import { useUIStore } from '@/stores/ui'
  const ui = useUIStore()
</script>

<template>
  <v-app-bar class="" :elevation="1" :rail="rail" rounded>
    <template #prepend>
      <v-app-bar-nav-icon @click="ui.toggleDrawer()" />
    </template>

    <v-app-bar-title>QAsis</v-app-bar-title>

    <template #append>
      <LoginButton />
      <RegisterButton />
      <v-btn icon="mdi-heart" />
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
