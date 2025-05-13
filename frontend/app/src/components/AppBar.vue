<script setup lang="ts">
  import { ref } from 'vue';
  const rail = ref(true)
  import { useUIStore } from '@/stores/ui'
  import LoginButton from '@/components/LoginButton.vue';
  import RegisterButton from '@/components/RegisterButton.vue';
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

      <v-btn icon="mdi-magnify" />

      <v-btn icon="mdi-dots-vertical" />
    </template>
  </v-app-bar>
</template>

<style scoped lang="sass">

</style>
