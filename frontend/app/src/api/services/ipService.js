export async function getClientLocation () {
  try {
    const ipRes = await fetch('https://api.ipify.org?format=json');
    const { ip } = await ipRes.json();

    const geoRes = await fetch(`https://ipapi.co/${ip}/json`);
    const geoData = await geoRes.json();

    return {
      ip,
      country: geoData.country_name,
      city: geoData.city,
      latitude: geoData.latitude,
      longitude: geoData.longitude,
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
