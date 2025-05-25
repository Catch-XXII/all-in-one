export async function getClientIp () {
  try {
    const response = await fetch('https://api.ipify.org?format=json');
    const data = await response.json();
    return data.ip;
  } catch (error) {
    console.error('Failed to fetch IPv4 address:', error);
    return null;
  }
}
