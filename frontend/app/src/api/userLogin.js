import axios from './axios'
import { useAuthStore } from '@/stores/auth'

export async function login (email, password) {
  const authStore = useAuthStore()

  try {
    const params = new URLSearchParams()
    params.append('username', email)
    params.append('password', password)

    const response = await axios.post('/login', params, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    })

    const { access_token } = response.data

    if (!access_token) {
      return {
        success: false,
        message: 'Unexpected response. No token received.',
      }
    }


    authStore.login({
      user: { email },
      token: access_token,
    })


    return {
      success: true,
    }
  } catch (error) {
    let message = 'An unknown error occurred'

    if (!error.response) {
      message = 'No service available. Please try again later.'
    } else if (error.response.status === 401) {
      message = 'Invalid email or password'
    } else if (error.code === 'ECONNABORTED') {
      message = 'Request timed out'
    } else if (error.response.status >= 500) {
      message = 'Server error. Please contact support.'
    }

    return { success: false, message }
  }
}
