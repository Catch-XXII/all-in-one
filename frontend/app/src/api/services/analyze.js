import axios from '../axios'

export async function analyzePage (url) {
  try {
    const response = await axios.post('/analyze', { url })
    return response.data
  } catch (error) {
    console.error('Analyze failed:', error)
    return []
  }
}
