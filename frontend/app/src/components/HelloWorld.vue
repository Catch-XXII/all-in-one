<template>
  <v-container class="mx-auto debug-border my-5" style="max-width: 786px">
    <v-row>
      <v-col cols="12">
        <div class="text-center mb-8">
          <div class="text-body-2 font-weight-light mb-n1">Welcome to</div>
          <h1 class="text-h2 font-weight-bold mb-8">QAsis</h1>

          <v-form ref="formRef" @submit.prevent>
            <v-text-field
              ref="inputRef"
              v-model="URL"
              :class="{ 'glowing-border': loading }"
              clearable
              density="compact"
              hide-details="true"
              prepend-inner-icon="mdi-magnify"
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

.glowing-border {
  padding: 1px 1px;
  font-size: 2rem;
  color: #5f6368;
  border-radius: 5px;

  border: 2px solid #4285f4;
  animation: glow-border 2s infinite alternate;
}

@keyframes glow-border {
  0% {
    border-color: #4285f4;
  }
  25% {
     border-color: #ea4335;
  }
  50% {
  border-color: #4285f4;
  }
  100% {
       border-color: #ea4335;
  }
}

</style>
