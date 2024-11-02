<!-- https://leafletjs.com/reference.html#map-example -->
<!-- https://leafletjs.com/examples/quick-start/ -->
<!-- https://maplibre.org/maputnik/?layer=2587890374%7E0#0.23/0/0 -->

<script lang="ts">
	import { onMount } from 'svelte'
    import type { ContaminatedSite, EmissionEvent } from '$lib/types';
	import L from 'leaflet'

	let mapElement: HTMLDivElement | null = $state(null)

    let map: L.Map; 
	let props: {currentView: string, contaminatedSite: ContaminatedSite[] | null, emissionEvent: EmissionEvent[]|null} = $props()

	onMount(async () => {
		const L = (await import('leaflet')).default
		if (mapElement) {
			map = L.map(mapElement).setView([29.71929, -95.3906], 13)
			L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
				attribution: `&copy;<a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>,
          &copy;<a href="https://carto.com/attributions" target="_blank">CARTO</a>`,
				subdomains: 'abcd',
				maxZoom: 19
			}).addTo(map)
		}
		updateMarkers()
	})

    function updateMarkers() {
        if (map) {
            map.eachLayer((layer: any) => {
                if (layer instanceof L.Marker) {
                    map.removeLayer(layer);
                }
            });

            if (props.contaminatedSite) {
                props.contaminatedSite.forEach((site) => {
                    const marker = L.marker([site.location.lat, site.location.long]).addTo(map);
                    marker.bindPopup(`Contaminated site: ${site.name}`).openPopup();
                });
            }

            if (props.emissionEvent) {
                props.emissionEvent.forEach((event) => {
                    const marker = L.marker([event.location.lat, event.location.long]).addTo(map);
                    marker.bindPopup(`Emission Event: ${event.site}`).openPopup();
                });
            }
        }
    }
</script>

<link
	rel="stylesheet"
	href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
	integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
	crossorigin=""
/>

<div bind:this={mapElement} class="h-96 w-96"></div>
