<script lang="ts">
    import QualityIndicator from '$lib/components/QualityIndicator.svelte'
	import Statistic from '$lib/components/Statistic.svelte'
    import type { ContaminatedSite, DetailedContaminatedSite } from '$lib/types';
    import { onMount } from 'svelte'
    import {ChevronLeft, ChevronRight} from "lucide-svelte/icons"
	import NearAq from '$lib/components/NearAq.svelte'


    let { data } = $props()

    let mapElement: HTMLDivElement | null = $state(null)
    onMount(async () => {
		const L = (await import('leaflet')).default
		if (mapElement) {
			const map = L.map(mapElement).setView([data.location.lat, data.location.long], 13) // change to use props later
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

<div class="ml-20 mt-5">
    <div class= "flex-col">
        <a href="/">
            <div class="flex flex-row items-center">
                <ChevronLeft color="#9ca3af" />
                <p class="text-lg text-gray-400">CONTAMINATED SITES</p>
            </div>
        </a>
        <p class="text-6xl"><b>{data.name}</b></p> 
        <p class="text-sm text-gray-600 pt-3"><b>Last Updated at</b> 11:45am CST October 19</p>
    </div>
    <div class="flex flex-row">
        <div class="flex-col w-1/4">
            <div bind:this={mapElement} class="h-80 w-full"></div>
            <div class="bg-slate-100 rounded p-5 mt-10">
                <p class="text-xl"><b>Air Quality in the area</b></p>
                <p><b>Station</b></p>
                <!-- use for each here for real thing -->

                <NearAq name={"Houston North Wayside C405"} quality={32.07}/>
                <NearAq name={"Houston Bayland Park"} quality={64.04}/>
                <NearAq name={"Vleux Carre Drive"} quality={270.40}/>

                <p class="text-xl mt-8"><b>Emission Events in the Area</b></p>
                <p class="mt-3">Brazos Amine Treater Facility</p>
                <p class="mt-3">Wildcat Gas Plant</p>
            </div>
        </div>
        <div class="bg-slate-100 rounded ml-10 w-full mr-10  p-6">
            <div class="flex flex-row">
                <QualityIndicator quality={39.65} name={"NPL"}/>
                <p class="text-xl pb-2 pl-4"><b>Site Overview</b></p>
            </div>
            <div class="grid grid-cols-4 gap-4">
                <Statistic title={"Hazard Level"} stat={data.hazardScore}/>
                <Statistic title={"Region ID"} stat={data.regionID}/>
                <Statistic title={"EPA Site ID"} stat={data.siteID}/>
                <Statistic title={"Location"} stat={data.locationName}/>
                <Statistic title={"Latitude"} stat={data.location.lat}/>
                <Statistic title={"Longitude"} stat={data.location.long}/>
                <Statistic title={"Construction Completion"} stat={data.constructionComplete}/>
                <Statistic title={"Partial Deletion"} stat={data.partialDeletion}/>
                <Statistic title={"Proposed"} stat={data.proposedDate}/>
                <Statistic title={"Listing"} stat={data.listingDate}/>
            </div>
            <div class="flex flex-col pt-8">
                <p class="text-xl pb-5"><b>Background</b></p>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vestibulum elit ac pellentesque consectetur.
                     In id enim eu turpis ultricies eleifend at ut nunc. Etiam vel congue odio. Proin ac dictum dolor. Sed et 
                     volutpat purus. Vestibulum pretium, leo quis posuere euismod, metus ipsum iaculis dui, in egestas urna nisi.</p>
                <div class="flex flex-row items-center mt-3">
                    <p class="text-lg"><u>Learn More</u></p>
                    <ChevronRight/>
                </div>
            </div>
            <div class="flex flex-col pt-8">
                <p class="text-xl"><b>Contaminant List</b></p>
                <!-- some table component from shadcn -->
            </div>
        </div>
        
    </div>
</div>