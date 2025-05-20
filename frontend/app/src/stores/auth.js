import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isLoggedIn: false,
    user: null,
    token: null,
  }),
  actions: {
    login ({ user, token }) {
      this.isLoggedIn = true
      this.user = user
      this.token = token
      localStorage.setItem('auth_token', token)
      localStorage.setItem('auth_user', JSON.stringify(user))
    },
    logout () {
      this.isLoggedIn = false
      this.user = null
      this.token = null
      localStorage.removeItem('auth_token')
      localStorage.removeItem('auth_user')
    },
    init () {
      const token = localStorage.getItem('auth_token')
      const user = localStorage.getItem('auth_user')

      if (token && user) {
        this.token = token
        this.user = JSON.parse(user)
        this.isLoggedIn = true
      }
    },
  },
})
