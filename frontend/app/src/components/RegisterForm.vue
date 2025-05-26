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
          v-model="email"
          density="compact"
          placeholder="Email address"
          prepend-inner-icon="mdi-email-outline"
          :rules="emailRules"
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
          :disabled="loading"
          :loading="loading"
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
      <v-snackbar
        v-model="snackbarVisible"
      >
        {{ snackbarMessage }}

        <template #actions>
          <v-btn
            color="pink"
            :timeout="timeout"
            variant="text"
            @click="snackbarVisible = false"
          >
            Close
          </v-btn>
        </template>
      </v-snackbar>

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
  const loading = ref(false)
  const showConfirmPassword = ref(false)
  const formRef = ref(null)
  const email = ref('')
  const snackbarVisible = ref(false)
  const snackbarMessage = ref('')
  const timeout = ref(2000)
  import { useRouter } from 'vue-router'
  import { register } from '@/api/userRegister'

  const router = useRouter()


  const submit = async () => {
    const validationIs = await formRef.value?.validate()
    if (!validationIs?.valid) return

    if (password.value !== confirmPassword.value) {
      snackbarMessage.value = 'Passwords do not match'
      snackbarVisible.value = true
      return
    }

    loading.value = true

    try {
      const { success, message } = await register(email.value, password.value)

      loading.value = false

      if (success) {
        snackbarMessage.value = message || 'Registration successful!'
        snackbarVisible.value = true
        ui.closeRegisterDialog()
        ui.openLoginDialog()
        await router.push('/')
      } else if (message) {
        snackbarMessage.value = message
        snackbarVisible.value = true
      }
    } catch (error) {
      loading.value = false

      snackbarMessage.value =
        error?.response?.data?.message || error.message || 'Unexpected error occurred'

      snackbarVisible.value = true
    }
  }

  const passwordRules = [
    v => !!v || 'Password is required',
    v => v.length >= 8 || 'Password must be at least 8 characters',
    v => /[0-9]/.test(v) || 'Must contain at least one number',
    v => /[A-Z]/.test(v) || 'Must contain at least one uppercase letter',
    v => /[!@#$%^&*]/.test(v) || 'Must contain at least one special character',
  ]

  const emailRules = [
    v => !!v || 'Email is required',
    v => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) || 'Email must be valid',
    v => v.length <= 255 || 'Email too long',
  ]
  const confirmPasswordRules = [
    v => !!v || 'Password is required',
    v => v.length >= 8 || 'Password must be at least 8 characters',
    v => /[0-9]/.test(v) || 'Must contain at least one number',
    v => /[A-Z]/.test(v) || 'Must contain at least one uppercase letter',
    v => /[!@#$%^&*]/.test(v) || 'Must contain at least one special character',
  ]
</script>

<style>

</style>
