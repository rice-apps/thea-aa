<script lang="ts">
	import AirQualityRanking from '$lib/components/AirQualityRanking.svelte'
	import EmissionEvents from '$lib/components/EmissionEvents.svelte';
	import ContaminatedSites from '$lib/components/ContaminatedSites.svelte';
	import Map from '$lib/components/Map.svelte'
	import { Button } from '$lib/components/ui/button'
	import { Building, Building2 } from 'lucide-svelte';
	import { Cloudy } from 'lucide-svelte';
	import { Wind } from 'lucide-svelte';
	import { ListFilter } from 'lucide-svelte';
   
	let { data } = $props()
	let currentView = $state('');
	let height = $state(0);
	let mapInstance: any; // Reference to Map component
   
	function handleViewChange(view: string) {
	  currentView = view;
	  // Call updateMarkers after view changes
	  if (mapInstance?.updateMarkers) {
		mapInstance.updateMarkers();
	  }
	}
   </script>
   
   <svelte:window bind:innerHeight={height} />
   
   <header class="flex items-center p-4">
	 <h1 class="text-3xl font-bold">Texas Environment Tracker</h1>
   </header>
   
   <main class="flex h-full p-10 space-x-9">
	 <aside class="w-1/3 bg-white rounded-lg shadow-lg p-8">
	   <div class="flex items-center space-x-2 mb-4">
		 <input placeholder="Search Address or Site" class="p-2 border rounded w-full" />
		 <input type="text" placeholder="Range (miles)" class="p-2 border rounded w-1/3" />
		 <Button><ListFilter class="w-5 h-5" /></Button>
	   </div>
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
		 <ContaminatedSites items={data.contaminatedSites}/>
	   {/if}
	   {#if currentView === 'emission'}
		 <EmissionEvents items={data.emissionEvents}/>
	   {/if}
	   {#if currentView === 'air quality'}
		 <AirQualityRanking items={data.airQualitySites}/>
	   {/if}
	 </aside>
	 
	 <div class="w-2/3">
	   <Map 
		 bind:this={mapInstance}
		 currentView={currentView} 
		 contaminatedSite={data.contaminatedSites} 
		 emissionEvent={data.emissionEvents} 
	   />
	 </div>
   </main>