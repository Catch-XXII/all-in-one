import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUIStore = defineStore('ui', () => {
  const drawer = ref(false)
  const loginDialog = ref(false)
  const registerDialog = ref(false)

  const toggleDrawer = () => {
    drawer.value = !drawer.value
  }
  const toggleRegisterDialog = () => {
    registerDialog.value = !registerDialog.value
  }
  const toggleLoginDialog = () => {
    loginDialog.value = !loginDialog.value
  }

  const switchToRegister = () => {
    loginDialog.value = false
    registerDialog.value = true
  }

  const switchToLogin = () => {
    loginDialog.value = true
    registerDialog.value = false
  }

  return {
    drawer,
    loginDialog,
    registerDialog,
    toggleDrawer,
    toggleLoginDialog,
    toggleRegisterDialog,
    switchToRegister,
    switchToLogin,
  }
})
