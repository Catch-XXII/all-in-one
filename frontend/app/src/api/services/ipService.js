export async function getClientLocation () {
  try {
    const res = await fetch('https://ipwho.is/');
    const data = await res.json();

    return {
      ip: data.ip,
      country: data.country,
      city: data.city,
      latitude: data.latitude,
      longitude: data.longitude,
    };
  } catch (error) {
    console.error('Failed to fetch client location', error);
    return {
      ip: null,
      country: null,
      city: null,
      latitude: null,
      longitude: null,
    };
  }
}
