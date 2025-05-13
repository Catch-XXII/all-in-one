import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUIStore = defineStore('ui', () => {
  const drawer = ref(false)
  const toggleDrawer = () => {
    drawer.value = !drawer.value
  }

  return { drawer, toggleDrawer }
})
