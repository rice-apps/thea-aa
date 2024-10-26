<!-- https://leafletjs.com/reference.html#map-example -->
<!-- https://leafletjs.com/examples/quick-start/ -->
<!-- https://maplibre.org/maputnik/?layer=2587890374%7E0#0.23/0/0 -->

<script lang="ts">
	import { onMount } from 'svelte'
    import type { ContaminatedSite, EmissionEvent } from '$lib/types';


	let mapElement: HTMLDivElement | null = $state(null)

	let props: {contaminatedSite: ContaminatedSite[] | null, emissionEvent: EmissionEvent[]|null} = $props()

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
			
			if (props.emissionEvent){
				props.emissionEvent.forEach((event) => {
					const marker = L.marker([event.location.lat, event.location.long]).addTo(map)
					marker.bindPopup(`Emission Event: ${event.site}`).openPopup()
				})
			}
			if (props.contaminatedSite) {
				props.contaminatedSite.forEach((event) => {
					const marker = L.marker([event.location.lat, event.location.long]).addTo(map)
					marker.bindPopup(`Contaminated site: ${event.name}`).openPopup()
				})
			}
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
