<template>
  <v-responsive>
    <v-app>
      <NavigationDrawer v-if="auth.isLoggedIn" />
      <AppBar />
      <router-view />
    </v-app>
  </v-responsive>
</template>

<script setup>

  import NavigationDrawer from '@/components/NavigationDrawer.vue';
  import AppBar from '@/components/AppBar.vue';

  import { useAuthStore } from '@/stores/auth'
  const auth = useAuthStore()
  auth.init()
</script>
