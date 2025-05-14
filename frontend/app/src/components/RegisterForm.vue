<template>
  <div>
    <v-card
      class="mx-auto pa-12 pb-8"
      elevation="24"
      max-width="568"
      rounded="xl"
    >

      <div class="text-subtitle-1 text-medium-emphasis">Email</div>

      <v-text-field
        density="compact"
        placeholder="Email address"
        prepend-inner-icon="mdi-email-outline"
        variant="outlined"
      />

      <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
        Password

      </div>

      <v-text-field
        :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
        density="compact"
        placeholder="Enter your password"
        prepend-inner-icon="mdi-lock-outline"
        :type="visible ? 'text' : 'password'"
        variant="outlined"
        @click:append-inner="visible = !visible"
      />

      <v-card
        class="mb-12"
        color="surface-variant"
        variant="tonal"
      />

      <v-btn
        block
        class="mb-8"
        color="blue"
        size="large"
        variant="tonal"
      >
        Register
      </v-btn>


    </v-card>
  </div>
</template>
<script setup>
  import { ref } from 'vue'

  const visible = ref(false)
</script>

<style>

</style>
