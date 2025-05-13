<script setup lang="ts">
  import { ref } from 'vue';

  const loading = ref(false)
  watch(loading, val => {
    if (!val) return
    setTimeout(() => (loading.value = false), 2000)
  })
</script>

<template>
  <v-btn
    class="text-none mx-2"
    :disabled="loading"
    :loading="loading"
    variant="outlined"
    @click="loading = !loading"
  >
    Login
  </v-btn>
</template>

<style scoped lang="sass">

</style>
