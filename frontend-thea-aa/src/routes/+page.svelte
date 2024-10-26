<script lang="ts">
	import AirQualityRanking from '$lib/components/AirQualityRanking.svelte'
	import EmissionEvents from '$lib/components/EmissionEvents.svelte';
	import ContaminatedSites from '$lib/components/ContaminatedSites.svelte';
	import Map from '$lib/components/Map.svelte'
	import { Button } from '$lib/components/ui/button'

  let { data } = $props()

	let showContaminated= $state(true)
	let showEmissionEvents= $state(true)
</script>

<main class="flex">
	<aside>
		<input placeholder="search" />
		<div>
			<Button on:click={()=>{showContaminated=!showContaminated}}>Contaminated Sites</Button>
			<Button on:click={()=>{showEmissionEvents=!showEmissionEvents}}>Emission Events</Button>
		</div>

		<!-- <AirQualityRanking items={data.airQualitySites} /> -->
		{#if showContaminated}
    		<ContaminatedSites items={data.contaminatedSites}/>
		{/if}
		
		{#if showEmissionEvents}
			<EmissionEvents items={data.emissionEvents}/>
		{/if}
	</aside>
	<div>
		<Map contaminatedSite={showContaminated ? data.contaminatedSites : null} emissionEvent={showEmissionEvents ? data.emissionEvents : null}/>
	</div>
</main>
