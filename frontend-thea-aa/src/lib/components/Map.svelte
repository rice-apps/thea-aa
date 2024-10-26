<!-- https://leafletjs.com/reference.html#map-example -->
<!-- https://leafletjs.com/examples/quick-start/ -->
<!-- https://maplibre.org/maputnik/?layer=2587890374%7E0#0.23/0/0 -->

<script lang="ts">
	import { onMount } from 'svelte'

	let mapElement: HTMLDivElement | null = $state(null)

	onMount(async () => {
		const L = (await import('leaflet')).default
		if (mapElement) {
			const map = L.map(mapElement).setView([29.71929, -95.3906], 13)
			L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
				attribution: `&copy;<a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>,
          &copy;<a href="https://carto.com/attributions" target="_blank">CARTO</a>`,
				subdomains: 'abcd',
				maxZoom: 19
			}).addTo(map)
			// L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
			// 	maxZoom: 19,
			// 	attribution:
			// 		'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
			// }).addTo(map)

			const marker = L.marker([59.71929 - 30, -55.3906 - 40]).addTo(map)

			marker.bindPopup('<b>Hello world!</b><br>I am a popup.').openPopup()
		}
	})
</script>

<link
	rel="stylesheet"
	href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
	integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
	crossorigin=""
/>

<div bind:this={mapElement} class="h-96 w-96"></div>
