<template>
  <v-container class="mx-auto my-5" style="max-width: 786px">
    <v-row align="center" justify="center">
      <v-col cols="12">
        <div class="text-center mb-8">
          <div class="text-body-2 font-weight-light mb-n1">Welcome to</div>
          <h1 class="text-h2 font-weight-bold mb-8">QAsis</h1>

          <div id="search">
            <v-overlay class="align-center justify-center" :model-value="loading" persistent>
              <v-progress-circular color="primary" indeterminate size="64" width="6" />
            </v-overlay>
            <v-form ref="formRef" @submit.prevent>
              <v-text-field
                ref="inputRef"
                v-model="URL"
                clearable
                density="compact"
                hide-details="true"
                placeholder="Search"
                prepend-inner-icon="mdi-magnify"
                rounded
                :rules="rules"
                variant="outlined"
                @click:prepend-inner="search"
                @keyup.enter="search"
              />
            </v-form>
          </div>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'
  import { analyzePage } from '@/api/services/analyze'

  const URL = ref('')
  const formRef = ref(null)
  const loading = ref(false)

  const rules = [
    value => (value ? value.length <= 200 : true) || 'Max 200 characters.',
    value => {
      if (!value) return true
      const pattern = /^(https?:\/\/)?([\w\-]+\.)+[\w\-]+(\/[\w\-./?%&=]*)?$/i
      return pattern.test(value.trim()) || 'Invalid URL.'
    },
  ]

  function handleKeyDown (event) {
    if (event.key === 'Escape') {
      URL.value = ''
    }
  }
  async function search () {
    const { valid } = await formRef.value.validate()
    if (!valid) return

    loading.value = true
    const trimmedUrl = URL.value.trim()

    try {
      const results = await analyzePage(trimmedUrl)
      console.log(trimmedUrl)
      console.log('Analyze results:', results)

    } catch (e) {
      console.error('Error during analysis:', e)
    } finally {
      loading.value = false
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
