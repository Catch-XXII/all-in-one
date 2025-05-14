<script setup lang="ts">
  import { ref } from 'vue';
  const rail = ref(true)
  import { useUIStore } from '@/stores/ui'
  import LoginButton from '@/components/LoginButton.vue';
  import RegisterButton from '@/components/RegisterButton.vue';
  import LoginForm from '@/components/LoginForm.vue';
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

    </template>
  </v-app-bar>
</template>

<style scoped lang="sass">

</style>
