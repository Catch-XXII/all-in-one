import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUIStore = defineStore('ui', () => {
  const drawer = ref(false)
  const loginDialog = ref(false)

  const toggleDrawer = () => {
    drawer.value = !drawer.value
  }

  const toggleLoginDialog = () => {
    loginDialog.value = !loginDialog.value
  }

  return {
    drawer,
    loginDialog,
    toggleDrawer,
    toggleLoginDialog,
  }
})
