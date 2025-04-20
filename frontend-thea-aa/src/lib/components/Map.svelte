<script lang="ts">
	import { onMount } from 'svelte'
	import type { AirQualitySite, ContaminatedSite, DetailedEmissionEvent } from '$lib/types'

	let mapElement: HTMLDivElement | null = null

	// Initialize `L` as undefined and assign it later
	let L: typeof import('leaflet') | undefined
	let map: import('leaflet').Map | null = null

	let windowWidth = $state(0)
	let windowHeight = $state(0)

	let props: {
		currentView: string
		contaminatedSite: ContaminatedSite[] | null
		emissionEvent: DetailedEmissionEvent[] | null
		airQualitySite: AirQualitySite[] | null
	} = $props()

	// Update map size and invalidate Leaflet dimensions
	function updateMapSize(windowWidth: number, windowHeight: number) {
		if (mapElement) {
			mapElement.style.width = `${0.6 * windowWidth}px`
			mapElement.style.height = `${0.7 * windowHeight}px`
		}

		if (map) {
			map.invalidateSize()
		}
	}

	// Use $effect to listen for changes in windowWidth or windowHeight
	$effect(() => {
		updateMapSize(windowWidth, windowHeight)
	})

	onMount(async () => {
		// Import Leaflet dynamically and assign it to `L`
		const leaflet = await import('leaflet')
		L = leaflet

		if (mapElement && L) {
			map = L.map(mapElement).setView([31.71929, -99.3906], 13)
			L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
				attribution: `&copy;<a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>,
        &copy;<a href="https://carto.com/attributions" target="_blank">CARTO</a>`,
				subdomains: 'abcd',
				maxZoom: 19
			}).addTo(map)
		}

		// Ensure the map is resized properly
		updateMapSize(windowWidth, windowHeight)
	})

	export function updateViewCentering(lat: number, long: number) {
		if (!map) return
		map.setView([lat, long], 8)
	}

	export function updateMarkers() {
		if (!map || !L) return

		// Clear existing markers
		map.eachLayer((layer: import('leaflet').Layer) => {
			if (L && layer instanceof L.Marker) {
				map!.removeLayer(layer)
			}
		})

		// Add markers based on current view
		if (props.currentView === 'superfund' && props.contaminatedSite) {
			props.contaminatedSite.forEach((site) => {
				if (site.lat && site.lon) {
					// Add null check
					try {
						if (!L) return
						const marker = L.marker([site.lat, site.lon])
						marker
							.addTo(map!)
							.bindPopup(
								`<a href="/detailedContaminant/${site.epa_id}">${site.site_name}</a><br>Status: ${site.site_status}<br>Score: ${site.hrs_score}<br>`
							)
					} catch (error) {
						console.error('Error adding marker for site:', site.site_name, error)
					}
				}
			})
		} else if (props.currentView === 'emission' && props.emissionEvent) {
			props.emissionEvent.forEach((event) => {
				if (event.lat && event.lon) {
					// Add null check
					try {
						if (!L) return
						const marker = L.marker([event.lat, event.lon])
						marker
							.addTo(map!)
							.bindPopup(
								`<a href="/detailedContaminant/${event.re_name}">${event.re_name}</a><br>Location: ${event.physical_location}`
							)
					} catch (error) {
						console.error('Error adding marker for event:', event.re_name, error)
					}
				}
			})
		} else if (props.currentView === 'air quality' && props.airQualitySite) {
			props.airQualitySite.forEach((site) => {
				if (site.location.lat && site.location.long) {
					// Add null check
					try {
						if (!L) return
						const marker = L.marker([site.location.lat, site.location.long])
						marker.addTo(map!).bindPopup(`${site.station}<br>Air Quality: ${site.airQuality}`)
					} catch (error) {
						console.error('Error adding marker for site:', site.station, error)
					}
				}
			})
		}
	}

	// Watch for props changes
	$effect(() => {
		if (
			map &&
			(props.currentView || props.contaminatedSite || props.emissionEvent || props.airQualitySite)
		) {
			updateMarkers()
		}
	})
</script>

<!-- Style for Leaflet -->
<link
	rel="stylesheet"
	href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
	integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
	crossorigin=""
/>

<!-- Map container -->
<div bind:this={mapElement}></div>

<!-- Bind window size -->
<svelte:window bind:innerWidth={windowWidth} bind:innerHeight={windowHeight} />
