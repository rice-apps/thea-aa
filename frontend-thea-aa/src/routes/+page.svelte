<script lang="ts">
	import AirQualityRanking from '$lib/components/AirQualityRanking.svelte'
	import EmissionEvents from '$lib/components/EmissionEvents.svelte';
	import ContaminatedSites from '$lib/components/ContaminatedSites.svelte';
	import Map from '$lib/components/Map.svelte'
	import { Button } from '$lib/components/ui/button'
	import SuperfundPreview from '$lib/components/SuperfundPreview.svelte';
	import type { ContaminatedSite } from '$lib/types.js';
	import { Component } from 'lucide-svelte'

  let { data } = $props()

	let showContaminated= $state(true)
	let showEmissionEvents= $state(true)
	let textContent: HTMLElement

	let displayState: "" |ContaminatedSite = $state("")

	let update = (site?: ContaminatedSite) => {
		if(site) {
			displayState = site;
		} else {
			displayState = ""
		}
	}
</script>

<main class="flex">
	<div bind:this={textContent} class="text-content">
		<aside>
			{#if displayState === ""}
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
			{:else}
				<SuperfundPreview superFundInfo={{name: displayState.name, hazardLevel: 25, location: "Texas", background: "fkldjlj dlf jdkljfjd flkjadsfjdkslfkjdslfklad kkfjdsafjkkdsfjdskf jsdjadlkjlfljsdfsdjk fljkasld;fj;lksdajfkljd", regionId: 6, status: "NLP Site", update: update}}/>
			{/if}

		</aside>

	</div>

	<div>
		<Map contaminatedSite={showContaminated ? data.contaminatedSites : null} emissionEvent={showEmissionEvents ? data.emissionEvents : null} {update}/>
	</div>
</main>
