<script lang="ts">
	/**
	 * UI for the home page
	 * Displays map + data panels (Contaminated Sites, Emission Events, Air Quality).
	 */
	// components
	import EmissionEvents from '$lib/components/EmissionEvents.svelte'
	import ContaminatedSites from '$lib/components/ContaminatedSites.svelte'
	import Map from '$lib/components/Map.svelte'
	import { Button } from '$lib/components/ui/button'
	import AirQualityRanking from '$lib/components/AirQualityRanking.svelte'
	import Toast from '$lib/components/Toast.svelte'

	// Icons
	import Building from 'lucide-svelte/icons/building'
	import Search from 'lucide-svelte/icons/search'
	import { Cloudy } from 'lucide-svelte'
	import { Wind } from 'lucide-svelte'
	import { ListFilter } from 'lucide-svelte'

	import { writable } from 'svelte/store'

	// Toast state and logic
	let toastVisible = writable(false)
	let toastMessage = writable('')

	function showToast(msg: string) {
		toastMessage.set(msg)
		toastVisible.set(true)
		setTimeout(() => toastVisible.set(false), 3000)
	}

	// Props & Reactive State
	let { data } = $props()
	let currentView = $state('')
	let height = $state(0)

	// Reference to Map component for calling methods
	let mapInstance: {
		updateMarkers: () => void
		updateViewCentering: (lat: number, long: number) => void
	} | null = null

	let apiKey = import.meta.env.VITE_PUBLIC_API_KEY

	let searchAddress = $state('')
	let searchRadius = $state('')
	let isLoading = $state(false)

	// Data defined by search
	let filteredData = $state({
		contaminatedSites: data.contaminatedSites,
		emissionEvents: data.emissionEvents,
		airQualitySites: data.airQualitySites
	})

	// Haversine distance between two lat/lon points
	function calculateDistance(lat1: number, long1: number, lat2: number, long2: number): number {
		const R = 3959 // Earth's radius in miles
		const dLat = ((lat2 - lat1) * Math.PI) / 180
		const dLon = ((long2 - long1) * Math.PI) / 180
		const a =
			Math.sin(dLat / 2) * Math.sin(dLat / 2) +
			Math.cos((lat1 * Math.PI) / 180) *
				Math.cos((lat2 * Math.PI) / 180) *
				Math.sin(dLon / 2) *
				Math.sin(dLon / 2)
		const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a))
		return R * c
	}

	// Geocode address → { lat, long }
	async function geocodeAddress(address: string): Promise<{ lat: number; long: number } | null> {
		try {
			const response = await fetch(
				`https://geocode.maps.co/search?q=${encodeURIComponent(address)}&api_key=${encodeURIComponent(apiKey)}`
			)

			if (!response.ok) {
				throw new Error(`Geocoding failed with status: ${response.status}`)
			}

			const data = await response.json()

			if (data && data.length > 0) {
				return {
					lat: parseFloat(data[0].lat),
					long: parseFloat(data[0].lon)
				}
			}
			return null
		} catch (error) {
			console.error('Geocoding error:', error)
			return null
		}
	}

	// Filtering logic
	async function applyFilter() {
		console.log('applyFilter')

		if (!searchAddress || !searchRadius) {
			// Reset to original data if no filter criteria
			filteredData = {
				contaminatedSites: data.contaminatedSites,
				emissionEvents: data.emissionEvents,
				airQualitySites: data.airQualitySites
			}
			return
		}

		isLoading = true

		console.log(data.contaminatedSites)

		try {
			const addressCoords = await geocodeAddress(searchAddress)
			if (!addressCoords) {
				showToast('Could not find the specified address')
				return
			}
			const radius = parseFloat(searchRadius)

			filteredData = {
				contaminatedSites: data.contaminatedSites.filter(
					(site) =>
						calculateDistance(addressCoords.lat, addressCoords.long, site.lat, site.lon) <= radius
				),
				emissionEvents: data.emissionEvents.filter(
					(event) =>
						calculateDistance(addressCoords.lat, addressCoords.long, event.lat, event.lon) <= radius
				),
				airQualitySites: data.airQualitySites.filter(
					(site) =>
						calculateDistance(
							addressCoords.lat,
							addressCoords.long,
							site.location.lat,
							site.location.long
						) <= radius
				)
			}

			// Update map markers
			if (mapInstance?.updateMarkers) {
				mapInstance.updateMarkers()
				mapInstance.updateViewCentering(addressCoords.lat, addressCoords.long)
			}
		} catch (error) {
			console.error('Error during filtering:', error)
			showToast('An error occurred while filtering the data. Please try again.')
		} finally {
			isLoading = false
		}
	}

	// View swtiching
	function handleViewChange(view: string) {
		currentView = view
		// Call updateMarkers after view changes
		if (mapInstance?.updateMarkers) {
			mapInstance.updateMarkers()
		}
	}
</script>

<!-- 
  Bind the window's innerHeight to a reactive variable `height` 
  (can be used to make layout responsive)
-->
<svelte:window bind:innerHeight={height} />

<!-- =====================
      Page Header
     ===================== -->
<header class="block items-center px-12 py-8">
	<h1 class="text-3xl font-bold">Texas Environment Tracker</h1>
</header>

<!-- =====================
     Main Layout (Sidebar + Map)
     ===================== -->
<main class="ph-10 flex h-full space-x-9">
	<!-- Toast popup for errors or feedback -->
	<Toast bind:message={$toastMessage} bind:visible={$toastVisible} duration={3000} />

	<!-- Sidebar Panel (1/3 width)-->
	<aside class="w-1/3 rounded-lg p-8 shadow-lg">
		<!--  Search + Filter Inputs -->
		<div class="mb-4 flex items-center space-x-2">
			<!-- Address input field with search icon -->
			<div class="flex w-full items-center rounded border">
				<Search class="ml-2" />
				<input bind:value={searchAddress} placeholder="Search Address or Site" class="w-full p-2" />
			</div>
			<!-- Radius input (in miles) -->
			<input
				bind:value={searchRadius}
				type="number"
				min="0"
				placeholder="Range (miles)"
				class="w-1/3 rounded border p-2"
			/>
			<!-- Filter button -->
			<Button class="bg-primary-foreground" on:click={applyFilter} disabled={isLoading}
				><ListFilter class="text-primary"></ListFilter></Button
			>
		</div>
		<!--  Show loading state when filtering -->
		{#if isLoading}
			<div class="py-2 text-center text-sm">Loading...</div>
		{/if}

		<!-- View Switch Buttons: Superfund / Emission / Air Quality -->
		<div class="flex space-x-2 overflow-x-auto whitespace-nowrap py-2">
			<!-- Superfund view toggle -->
			<Button
				on:click={() => handleViewChange('superfund')}
				class="bg-primary-foreground grid h-full place-items-center"
			>
				<Building size={20} class="text-primary"></Building>
				<span class="text-primary text-xs">Superfund</span>
			</Button>

			<!-- Emission Events toggle -->
			<Button
				on:click={() => handleViewChange('emission')}
				class="bg-primary-foreground grid h-full place-items-center"
			>
				<Cloudy size={20} class="text-primary"></Cloudy>
				<span class="text-primary text-xs">Emission Events</span>
			</Button>

			<!-- Air Quality toggle -->
			<Button
				on:click={() => handleViewChange('air quality')}
				class="bg-primary-foreground grid h-full place-items-center"
			>
				<Wind size={20} class="text-primary"></Wind>
				<span class="text-primary text-xs">Air Quality</span>
			</Button>
		</div>

		<!--  Conditional Display of Data Panels -->
		{#if currentView === 'superfund'}
			<ContaminatedSites items={filteredData.contaminatedSites} />
		{/if}
		{#if currentView === 'emission'}
			<EmissionEvents items={filteredData.emissionEvents} />
		{/if}
		{#if currentView === 'air quality'}
			<AirQualityRanking items={filteredData.airQualitySites} />
		{/if}
	</aside>

	<!-- =====================
	     Map Panel (2/3 width)
	     ===================== -->
	<div class="w-2/3">
		<Map
			bind:this={mapInstance}
			{currentView}
			contaminatedSite={filteredData.contaminatedSites}
			emissionEvent={filteredData.emissionEvents}
			airQualitySite={filteredData.airQualitySites}
		/>
	</div>
</main>
