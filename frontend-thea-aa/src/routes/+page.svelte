<script lang="ts">
	// import AirQualityRanking from '$lib/components/AirQualityRanking.svelte'
	import EmissionEvents from '$lib/components/EmissionEvents.svelte'
	import ContaminatedSites from '$lib/components/ContaminatedSites.svelte'
	import Map from '$lib/components/Map.svelte'
	import { Button } from '$lib/components/ui/button'
	import Building from 'lucide-svelte/icons/building'
	import Search from 'lucide-svelte/icons/search'
	import { Cloudy } from 'lucide-svelte'
	import { Wind } from 'lucide-svelte'
	import { ListFilter } from 'lucide-svelte'
	import AirQualityRanking from '$lib/components/AirQualityRanking.svelte'
	import Toast from '$lib/components/Toast.svelte'
	import { writable } from 'svelte/store'

	let toastVisible = writable(false)
	let toastMessage = writable('')

	function showToast(msg: string) {
		toastMessage.set(msg)
		toastVisible.set(true)
		setTimeout(() => toastVisible.set(false), 3000)
	}

	let { data } = $props()
	let currentView = $state('')
	let height = $state(0)
	let mapInstance: {
		updateMarkers: () => void
		updateViewCentering: (lat: number, long: number) => void
	} | null = null

	let apiKey = import.meta.env.VITE_PUBLIC_API_KEY

	let searchAddress = $state('')
	let searchRadius = $state('')
	let isLoading = $state(false)
	let filteredData = $state({
		contaminatedSites: data.contaminatedSites,
		emissionEvents: data.emissionEvents,
		airQualitySites: data.airQualitySites
	})

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

	async function applyFilter() {
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

		try {
			const addressCoords = await geocodeAddress(searchAddress)
			if (!addressCoords) {
				showToast('Could not find the specified address')
				return
			}
			const radius = parseFloat(searchRadius)

			filteredData = {
				contaminatedSites: data.contaminatedSites.filter(
					() => calculateDistance(addressCoords.lat, addressCoords.long, 5, 5) <= radius // add back site later site.location.lat
				),
				emissionEvents: data.emissionEvents.filter(
					(event) =>
						calculateDistance(addressCoords.lat, addressCoords.long, event.lat, event.lon) <= radius
				),
				airQualitySites: data.airQualitySites.filter(
					() => calculateDistance(addressCoords.lat, addressCoords.long, 5, 5) <= radius // add back site later with lat, long
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

	function handleViewChange(view: string) {
		currentView = view
		// Call updateMarkers after view changes
		if (mapInstance?.updateMarkers) {
			mapInstance.updateMarkers()
		}
	}
</script>

<svelte:window bind:innerHeight={height} />

<header class="block items-center px-12 py-8">
	<h1 class="text-3xl font-bold">Texas Environment Tracker</h1>
	<h2 class="ml py-4">Last updated at</h2>
</header>

<main class="ph-10 flex h-full space-x-9">
	<Toast bind:message={$toastMessage} bind:visible={$toastVisible} duration={3000} />
	<aside class="w-1/3 rounded-lg p-8 shadow-lg">
		<div class="mb-4 flex items-center space-x-2">
			<div class="flex w-full items-center rounded border">
				<Search class="ml-2" />
				<input bind:value={searchAddress} placeholder="Search Address or Site" class="w-full p-2" />
			</div>
			<input
				bind:value={searchRadius}
				type="number"
				min="0"
				placeholder="Range (miles)"
				class="w-1/3 rounded border p-2"
			/>
			<Button class="bg-primary-foreground" on:click={applyFilter} disabled={isLoading}
				><ListFilter class="text-primary"></ListFilter></Button
			>
		</div>
		{#if isLoading}
			<div class="py-2 text-center text-sm">Loading...</div>
		{/if}
		<div class="flex space-x-2 overflow-x-auto whitespace-nowrap py-2">
			<Button
				on:click={() => handleViewChange('superfund')}
				class="grid h-full place-items-center bg-primary-foreground"
			>
				<Building size={20} class="text-primary"></Building>
				<span class="text-xs text-primary">Superfund</span>
			</Button>
			<Button
				on:click={() => handleViewChange('emission')}
				class="grid h-full place-items-center bg-primary-foreground"
			>
				<Cloudy size={20} class="text-primary"></Cloudy>
				<span class="text-xs text-primary">Emission Events</span>
			</Button>
			<Button
				on:click={() => handleViewChange('air quality')}
				class="grid h-full place-items-center bg-primary-foreground"
			>
				<Wind size={20} class="text-primary"></Wind>
				<span class="text-xs text-primary">Air Quality</span>
			</Button>
		</div>

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
