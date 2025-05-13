<template>
  <v-main>

    <router-view />

    <MainResultPage />
  </v-main>

  <AppFooter />
</template>

<script setup>
  import AppFooter from '@/components/AppFooter.vue';
  import MainResultPage from '@/pages/MainResultPage.vue';
</script>
