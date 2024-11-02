<script lang="ts">
	import AirQualityRanking from '$lib/components/AirQualityRanking.svelte'
	import EmissionEvents from '$lib/components/EmissionEvents.svelte';
	import ContaminatedSites from '$lib/components/ContaminatedSites.svelte';
	import Map from '$lib/components/Map.svelte'
	import { Button } from '$lib/components/ui/button'
	import { Building2 } from 'lucide-svelte';
	import { Cloudy } from 'lucide-svelte';
	import { Wind } from 'lucide-svelte';
	import { ListFilter } from 'lucide-svelte';


  let { data } = $props()

	let currentView = $state('');

	let height = $state(0);
	
</script>

<svelte:window bind:innerHeight={height} />
<main class="flex h-full p-10 space-x-9">
	<aside class="w-1/3 bg-white rounded-lg shadow-lg p-8">
		<input placeholder="Search Address or Site" class="mb-2 p-2 border rounded" />
		<Button>Filter<ListFilter></ListFilter></Button>
		<div class = "overflow-x-auto whitespace-nowrap space-x-2 flex py-2">
			<Button on:click={() => currentView = 'superfund'} class=""><Building2></Building2>Superfund</Button>
			<Button on:click={() => currentView = 'emission'}><Cloudy></Cloudy>Emission Events</Button>
			<Button on:click={() => currentView = 'air quality'}><Wind></Wind>Air Quality</Button>
			<Button on:click={() => currentView = 'air quality'}><Wind></Wind>Air Quality</Button>
			<Button on:click={() => currentView = 'air quality'}><Wind></Wind>Air Quality</Button>
		</div>

		<!-- <AirQualityRanking items={data.airQualitySites} /> -->
		{#if currentView === 'superfund'}
    		<ContaminatedSites items={data.contaminatedSites}/>
		{/if}
		
		{#if currentView === 'emission'}
			<EmissionEvents items={data.emissionEvents}/>
		{/if}

		{#if currentView === 'air quality'}
			<EmissionEvents items={data.emissionEvents}/>
		{/if}
	</aside>

	<div class="w-2/3" style="height: {height*0.8}px">
		<Map currentView={currentView} contaminatedSite={data.contaminatedSites} emissionEvent={data.emissionEvents}/>
	</div>
</main>
