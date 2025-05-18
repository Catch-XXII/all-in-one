<template>
  <v-form ref="formRef" @submit.prevent="submit">
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
          v-model="password"
          :append-inner-icon="showPassword ? 'mdi-eye-off' : 'mdi-eye'"
          density="compact"
          placeholder="Enter your password"
          prepend-inner-icon="mdi-lock-outline"
          :rules="passwordRules"
          :type="showPassword ? 'text' : 'password'"
          variant="outlined"

          @click:append-inner="showPassword = !showPassword"
        />

        <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
          Confirm Password

        </div>
        <v-text-field
          v-model="confirmPassword"
          :append-inner-icon="showConfirmPassword ? 'mdi-eye-off' : 'mdi-eye'"
          density="compact"
          placeholder="Confirm your password"
          prepend-inner-icon="mdi-lock-outline"
          :rules="confirmPasswordRules"
          :type="showConfirmPassword ? 'text' : 'password'"
          variant="outlined"

          @click:append-inner="showConfirmPassword = !showConfirmPassword"
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
          type="submit"
          variant="tonal"
        >
          Register
        </v-btn>
        <v-card-text class="text-center">
          <a
            class="text-blue text-decoration-none"
            href="#"
            rel="noopener noreferrer"
            target="_blank"
            @click.prevent="ui.switchToLogin"
          >
            <v-icon icon="mdi-chevron-left" /> Go back
          </a>
        </v-card-text>

      </v-card>
    </div>
  </v-form>
</template>
<script setup>
  import { ref } from 'vue'
  import { useUIStore } from '@/stores/ui.js';
  const ui = useUIStore()
  const password = ref('')
  const confirmPassword = ref('')
  const showPassword = ref(false)
  const showConfirmPassword = ref(false)
  const formRef = ref(null)

  const submit = () => {
    if (formRef.value?.validate()) {
    // Send registration request
    }
  }
  const passwordRules = [
    v => !!v || 'Password is required',
    v => v.length >= 6 || 'Password must be at least 6 characters',
  ]

  const confirmPasswordRules = [
    v => !!v || 'Please confirm your password',
    v => v === password.value || 'Passwords must match',
  ]
</script>

<style>

</style>
