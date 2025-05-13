<script setup lang="ts">
  import { ref } from 'vue';

  const rail = ref(true)
  import { useUIStore } from '@/stores/ui'

  const ui = useUIStore()
</script>

<template>
  <v-app-bar :elevation="1" :rail="rail" rounded>
    <template #prepend>
      <v-app-bar-nav-icon @click="ui.toggleDrawer()" />
    </template>

    <v-app-bar-title>QAsis</v-app-bar-title>

    <template #append>
      <v-btn icon="mdi-heart" />

      <v-btn icon="mdi-magnify" />

      <v-btn icon="mdi-dots-vertical" />
    </template>
  </v-app-bar>
</template>

<style scoped lang="sass">

</style>
