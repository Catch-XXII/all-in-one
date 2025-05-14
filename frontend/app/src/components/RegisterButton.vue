<script setup lang="ts">
  import { useUIStore } from '@/stores/ui'
  const ui = useUIStore()
</script>

<template>
  <v-btn
    class="text-none"
    variant="outlined"
    @click="ui.toggleRegisterDialog"
  >
    Register
  </v-btn>
</template>

<style scoped lang="sass">

</style>
