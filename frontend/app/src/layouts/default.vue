<template>
  <v-main>

    <router-view />

    <v-container class="mx-auto debug-border" style="max-width: 786px">
      <h1>Main Content</h1>
    </v-container>
  </v-main>

  <AppFooter />
</template>

<script setup>
  import AppFooter from '@/components/AppFooter.vue';
</script>
