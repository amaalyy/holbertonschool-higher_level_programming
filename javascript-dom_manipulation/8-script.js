document.addEventListener('DOMContentLoaded', () => {
  const helloElement = document.getElementById('hello');

  async function fetchAndDisplayTranslation() {
    try {
      const response = await fetch(
        'https://hellosalut.stefanbohacek.dev/?lang=fr'
      );
      if (!response.ok)
        throw new Error(`HTTP error! Status: ${response.status}`);
      const translation = await response.text();
      helloElement.textContent = translation;
    } catch (error) {
      console.error('Fetch error:', error);
    }
  }

  fetchAndDisplayTranslation();
});
