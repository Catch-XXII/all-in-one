<script setup lang="ts">
  import { useUIStore } from '@/stores/ui'
  const ui = useUIStore()
</script>

<template>
  <v-btn
    class="text-none mx-2"
    :disabled="loading"
    :loading="loading"
    variant="outlined"
    @click="ui.toggleLoginDialog"
  >
    Login
  </v-btn>
</template>

<style scoped lang="sass">

</style>
