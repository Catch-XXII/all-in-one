import axios from './axios'
import { useAuthStore } from '@/stores/auth'

export async function loginUser (email, password) {
  const authStore = useAuthStore()

  try {
    const params = new URLSearchParams()
    params.append('username', email)
    params.append('password', password)

    const response = await axios.post('/v1/login', params, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    })

    const { access_token } = response.data

    authStore.login({
      user: { email },
      token: access_token,
    })


    return true
  } catch (error) {
    console.error('Login failed:', error)
    return false
  }
}
