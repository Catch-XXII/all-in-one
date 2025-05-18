<template>
  <v-form ref="formRef" @submit.prevent="submit">
    <div>
      <v-card
        class="mx-auto pa-12 pb-8"
        elevation="24"
        max-width="568"
        rounded="xl"
      >
        <div class="text-subtitle-1 text-medium-emphasis">Account</div>

        <v-text-field
          v-model="email"
          density="compact"
          label="Email"
          placeholder="Email address"
          prepend-inner-icon="mdi-email-outline"
          :rules="emailRules"
          variant="outlined"
        />

        <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
          Password

          <a
            class="text-caption text-decoration-none text-blue"
            href="/reset-password"
            rel="noopener noreferrer"
            target="_blank"
          >
            Forgot login password?
          </a>
        </div>

        <v-text-field
          v-model="password"
          :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
          density="compact"
          label="Password"
          placeholder="Enter your password"
          prepend-inner-icon="mdi-lock-outline"
          :rules="passwordRules"
          :type="visible ? 'text' : 'password'"
          variant="outlined"
          @click:append-inner="visible = !visible"
        />

        <v-card
          class="mb-12"
          color="surface-variant"
          variant="tonal"
        >
          <v-card-text class="text-medium-emphasis text-caption">
            Warning: After 3 consecutive failed login attempts, your account will be temporarily locked for three hours. If you must login now, you can also click "Forgot login password?" below to reset the login password.
          </v-card-text>
        </v-card>

        <v-btn
          block
          class="mb-8"
          color="blue"
          size="large"
          type="submit"
          variant="tonal"
        >
          Log In
        </v-btn>

        <v-card-text class="text-center">
          <a
            class="text-blue text-decoration-none"
            href="#"
            rel="noopener noreferrer"
            target="_blank"
            @click.prevent="ui.switchToRegister"
          >
            Sign up now <v-icon icon="mdi-chevron-right" />
          </a>
        </v-card-text>
      </v-card>
    </div>
  </v-form>
</template>

<script setup>
  import { ref } from 'vue'
  import { useUIStore } from '@/stores/ui'

  const ui = useUIStore()
  const formRef = ref(null)

  const email = ref('')
  const password = ref('')
  const visible = ref(false)

  const emailRules = [
    v => !!v || 'Email is required',
    v => /.+@.+\..+/.test(v) || 'Email must be valid',
  ]

  const passwordRules = [
    v => !!v || 'Password is required',
    v => v.length >= 6 || 'Password must be at least 6 characters',
  ]

  const submit = () => {
    if (formRef.value?.validate()) {
      // Proceed with login request
    }
  }
</script>
