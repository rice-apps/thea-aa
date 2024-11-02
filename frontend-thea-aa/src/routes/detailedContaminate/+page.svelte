<script lang="ts">
    import QualityIndicator from '$lib/components/QualityIndicator.svelte'
    import type { ContaminatedSite } from '$lib/types';
    import { onMount } from 'svelte'

    let props: {item: ContaminatedSite} = $props()

    let amountToShow = $state(3)

    let mapElement: HTMLDivElement | null = $state(null)
    onMount(async () => {
		const L = (await import('leaflet')).default
		if (mapElement) {
			const map = L.map(mapElement).setView([29.71929, -95.3906], 13) // change to use props later
			L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
				attribution: `&copy;<a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>,
          &copy;<a href="https://carto.com/attributions" target="_blank">CARTO</a>`,
				subdomains: 'abcd',
				maxZoom: 19
			}).addTo(map)
		}
	})
</script>

<link
	rel="stylesheet"
	href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
	integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
	crossorigin=""
/>

<div class="ml-20">
    
    <div class="flex flex-col">
        <p class="text-base"><a href="/">Contaminated Sites</a></p>
        <p class="text-4xl"><b>Sol Lynn/Industrial Transformers</b></p> 
        <p class="text-sm"><b>Last Updated at</b> 11:45am CST October 19</p>
            
        
    </div>
    <div class="flex-col w-1/4">
        <div bind:this={mapElement} class="h-96 w-full"></div>
        <div class="bg-slate-300 rounded p-5 mt-10">
            <p class="text-lg"><b>Air Quality in the area</b></p>
            <p><b>Station</b></p>
            <!-- use for each here for real thing -->
            <div class="flex flex-row justify-between pt-5">
                <p>Houston North Wayside C405</p> 
                <QualityIndicator quality={32.07}/>
            </div>
            <div class="flex flex-row justify-between pt-5">
                <p>Houston Bayland Park</p> 
                <QualityIndicator quality={64.0}/>
            </div>
            <p class="text-lg"><b>Emission Events in the Area</b></p>
            <p>Brazos Amine Treater Facility</p>
            <p>Wildcat Gas Plant</p>
        </div>
    </div>

</div>
<!-- <table>
    <thead>
        <tr>
        <th>Status</th>
        <th>Site</th>
        <th>Hazard Score</th>
        </tr>
    </thead>
    <tbody>
        {#each props.items.slice(0, amountToShow) as item}
        <tr>
            <td>{item.status}</td>
            <td>{item.name}</td>
            <td>{item.hazardScore}</td>
        </tr>
        {/each}
    </tbody>
</table> -->

