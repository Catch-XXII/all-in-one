<template>
  <v-responsive>
    <v-app>
      <NavigationDrawer />
      <AppBar />
      <router-view />
    </v-app>
  </v-responsive>
</template>

<script setup>
  //
  import NavigationDrawer from '@/components/NavigationDrawer.vue';
  import AppBar from '@/components/AppBar.vue';
</script>
