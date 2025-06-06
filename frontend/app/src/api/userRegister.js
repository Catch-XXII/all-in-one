import axios from './axios'
import { getClientLocation } from '@/api/services/ipService'

export async function register (email, password) {
  try {
    const location = await getClientLocation()

    await axios.post('/register', {
      email,
      password,
      ip: location.ip,
      country: location.country,
      city: location.city,
      latitude: location.latitude,
      longitude: location.longitude,
    })

    return { success: true }
  } catch (error) {
    let message = 'An unknown error occurred'

    if (!error.response) {
      message = 'No service available. Please try again later.'
    } else if (error.response.status === 400) {
      message = 'Invalid registration attempt.'
    } else if (error.response.status === 409) {
      message = 'This email is already registered.'
    } else if (error.code === 'ECONNABORTED') {
      message = 'Request timed out'
    } else if (error.response.status >= 500) {
      message = 'Server error. Please contact support.'
    }

    return { success: false, message }
  }
}
