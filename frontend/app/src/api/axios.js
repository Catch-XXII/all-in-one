import axios from 'axios'
import { useAuthStore } from '@/stores/auth'


const axiosInstance = axios.create({
  baseURL: import.meta.env.VITE_API_URL + '/api/v1/',
  withCredentials: true,
})

// Add request interceptor to attach token
axiosInstance.interceptors.request.use(config => {
  let token = sessionStorage.getItem('auth_token')

  if (!token) {
    const authStore = useAuthStore()
    token = authStore.token
  }

  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }

  return config
})


export default axiosInstance
