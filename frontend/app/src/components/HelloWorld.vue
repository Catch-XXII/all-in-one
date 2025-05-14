<template>
  <v-container class="mx-auto my-5" style="max-width: 786px">
    <v-row align="center" justify="center">
      <v-col cols="12">
        <div class="text-center mb-8">
          <div class="text-body-2 font-weight-light mb-n1">Welcome to</div>
          <h1 class="text-h2 font-weight-bold mb-8">QAsis</h1>

          <v-form ref="formRef" @submit.prevent>
            <v-text-field
              ref="inputRef"
              v-model="URL"
              clearable
              density="compact"
              hide-details="true"
              label="Search"
              prepend-inner-icon="mdi-magnify"
              rounded
              :rules="rules"
              variant="outlined"
              @click:prepend-inner="search"
              @keyup.enter="search"
            />
          </v-form>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const URL = ref('')
  const formRef = ref(null)
  const loading = ref(false)

  const rules = [
    value => (value ? value.length <= 100 : true) || 'Max 100 characters.',
    value => {
      if (!value) return true // boşsa geç, validasyon uygulama
      const pattern = /^(?:https?:\/\/)?(?:[\w-]+\.)+[a-z]{2,6}$/i
      return pattern.test(value.trim()) || 'Invalid domain or URL.'
    },
  ]

  async function search () {
    const { valid } = await formRef.value.validate()
    if (!valid) return

    loading.value = true
    console.log('Searching for:', URL.value.trim())

    setTimeout(() => {
      loading.value = false
      console.log('Simulated search complete.')
    }, 5000)
  }

  function handleKeyDown (event) {
    if (event.key === 'Escape') {
      URL.value = ''
    }
  }

  onMounted(() => {
    window.addEventListener('keydown', handleKeyDown)
  })

  onBeforeUnmount(() => {
    window.removeEventListener('keydown', handleKeyDown)
  })
</script>

<style>

</style>
