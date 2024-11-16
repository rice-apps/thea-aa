<script lang="ts">
	// import AirQualityRanking from '$lib/components/AirQualityRanking.svelte'
	import EmissionEvents from '$lib/components/EmissionEvents.svelte'
	import ContaminatedSites from '$lib/components/ContaminatedSites.svelte'
	import Map from '$lib/components/Map.svelte'
	import { Button } from '$lib/components/ui/button'
	import { Building, Building2, Search } from 'lucide-svelte';
	import { Cloudy } from 'lucide-svelte';
	import { Wind } from 'lucide-svelte';
	import { ListFilter } from 'lucide-svelte';
	import AirQualityRanking from '$lib/components/AirQualityRanking.svelte'
   
	let { data } = $props()
	let currentView = $state('');
	let height = $state(0);
	let mapInstance: any;
	let apiKey = "672fc9cf41928442178811nqtede4fc"

	let searchAddress = $state('');
	let searchRadius = $state('');
	let isLoading = $state(false);
	let filteredData = $state({
		contaminatedSites: data.contaminatedSites,
		emissionEvents: data.emissionEvents,
		airQualitySites: data.airQualitySites
	});

	function calculateDistance(lat1: number, long1: number, lat2: number, long2: number): number {
		const R = 3959; // Earth's radius in miles
		const dLat = (lat2 - lat1) * Math.PI / 180;
		const dLon = (long2 - long1) * Math.PI / 180;
		const a = 
			Math.sin(dLat/2) * Math.sin(dLat/2) +
			Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) * 
			Math.sin(dLon/2) * Math.sin(dLon/2);
		const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
		return R * c;
	}

	async function geocodeAddress(address: string): Promise<{lat: number, long: number} | null> {
		try {
			const response = await fetch(
				`https://geocode.maps.co/search?q=${encodeURIComponent(address)}&api_key=${encodeURIComponent(apiKey)}`
			);
			
			if (!response.ok) {
				throw new Error(`Geocoding failed with status: ${response.status}`);
			}

			const data = await response.json();
			
			if (data && data.length > 0) {
				return {
					lat: parseFloat(data[0].lat),
					long: parseFloat(data[0].lon)
				};
			}
			return null;
		} catch (error) {
			console.error('Geocoding error:', error);
			return null;
		}
	}

	async function applyFilter() {
		if (!searchAddress || !searchRadius) {
			// Reset to original data if no filter criteria
			filteredData = {
				contaminatedSites: data.contaminatedSites,
				emissionEvents: data.emissionEvents,
				airQualitySites: data.airQualitySites
			};
			return;
		}

		isLoading = true;

		try {
			const addressCoords = await geocodeAddress(searchAddress);
			if (!addressCoords) {
				alert('Could not find the specified address');
				return;
			}
			const radius = parseFloat(searchRadius);
			
			filteredData = {
				contaminatedSites: data.contaminatedSites.filter(site => calculateDistance(addressCoords.lat, addressCoords.long, site.location.lat, site.location.long) <= radius),
				emissionEvents: data.emissionEvents.filter(event => calculateDistance(addressCoords.lat, addressCoords.long, event.location.lat, event.location.long) <= radius),
				airQualitySites: data.airQualitySites.filter(site => calculateDistance(addressCoords.lat, addressCoords.long, site.location.lat, site.location.long) <= radius)
			};

			// Update map markers
			if (mapInstance?.updateMarkers) {
				mapInstance.updateMarkers();
				mapInstance.updateViewCentering(addressCoords.lat, addressCoords.long);
			}
		} catch (error) {
			console.error('Error during filtering:', error);
			alert('An error occurred while filtering the data. Please try again.');
		} finally {
			isLoading = false;
		}
	}
   
	function handleViewChange(view: string) {
	  currentView = view;
	  // Call updateMarkers after view changes
	  if (mapInstance?.updateMarkers) {
		mapInstance.updateMarkers();
	  }
	}
   </script>
   
   <svelte:window bind:innerHeight={height} />
   
   <header class="flex items-center px-12 py-8">
	 <h1 class="text-3xl font-bold">Texas Environment Tracker</h1>
   </header>
   
   <main class="flex h-full p-10 space-x-9">
	 <aside class="w-1/3 bg-white rounded-lg shadow-lg p-8">
	   <div class="flex items-center space-x-2 mb-4">
		<div class="flex items-center border rounded w-full">
			<Search class="ml-2" />
			<input bind:value={searchAddress} placeholder="Search Address or Site" class="p-2 w-full" />
		</div>
		<input bind:value={searchRadius} type="number" min="0" placeholder="Range (miles)" class="p-2 border rounded w-1/3" />
		<Button on:click={applyFilter} disabled={isLoading}><ListFilter></ListFilter></Button>
	   </div>
	   {#if isLoading}
			<div class="text-center py-2 text-sm text-gray-600">
				Loading...
			</div>
		{/if}
	   <div class="overflow-x-auto whitespace-nowrap space-x-2 flex py-2">
		 <Button 
		   on:click={() => handleViewChange('superfund')} 
		   class="flex flex-col items-center"
		 >
		   <Building></Building>
		   <span class="text-xs">Superfund</span>
		 </Button>
		 <Button 
		   on:click={() => handleViewChange('emission')} 
		   class="flex flex-col items-center"
		 >
		   <Cloudy></Cloudy>
		   <span class="text-xs">Emission Events</span>
		 </Button>
		 <Button 
		   on:click={() => handleViewChange('air quality')} 
		   class="flex flex-col items-center"
		 >
		   <Wind></Wind>
		   <span class="text-xs">Air Quality</span>
		 </Button>
	   </div>
	   
	   {#if currentView === 'superfund'}
		 <ContaminatedSites items={filteredData.contaminatedSites}/>
	   {/if}
	   {#if currentView === 'emission'}
		 <EmissionEvents items={filteredData.emissionEvents}/>
	   {/if}
	   {#if currentView === 'air quality'}
		 <AirQualityRanking items={filteredData.airQualitySites}/>
	   {/if}
	 </aside>
	 
	 <div class="w-2/3">
	   <Map 
		 bind:this={mapInstance}
		 currentView={currentView} 
		 contaminatedSite={filteredData.contaminatedSites} 
		 emissionEvent={filteredData.emissionEvents} 
		 airQualitySite={filteredData.airQualitySites}
	   />
	 </div>
   </main>