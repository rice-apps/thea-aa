<script lang="ts">
	import QualityIndicator from '$lib/components/QualityIndicator.svelte'
	import Statistic from '$lib/components/Statistic.svelte'
	// import type { ContaminatedSite, DetailedContaminatedSite } from '$lib/types'
	import { onMount } from 'svelte'
	import { ChevronLeft, ChevronRight } from 'lucide-svelte/icons'
	import NearAq from '$lib/components/NearAq.svelte'
	import DetailedContamTable from '$lib/components/DetailedContamTable.svelte'

	let { data } = $props()
	const contaminatedSite = data.contaminatedSite
	const tableInfo = data.tableInfo

	let mapElement: HTMLDivElement | null = $state(null)
	onMount(async () => {
		const L = (await import('leaflet')).default
		if (mapElement) {
			const map = L.map(mapElement).setView(
				[contaminatedSite.location.lat, contaminatedSite.location.long],
				13
			) // change to use props later
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
	<div class="flex-col">
		<a href="/">
			<div class="flex flex-row items-center">
				<ChevronLeft class="text-foreground" />
				<p class="text-lg text-foreground">CONTAMINATED SITES</p>
			</div>
		</a>
		<p class="text-6xl font-bold">{contaminatedSite.name}</p>
		<p class="pt-3 text-sm text-foreground">
			<span class="font-bold">Last Updated at</span> 11:45am CST October 19
		</p>
	</div>
	<div class="mt-3 flex flex-row">
		<div class="w-1/4 flex-col">
			<div bind:this={mapElement} class="h-80 w-full"></div>
			<div class="mt-5 rounded bg-muted p-5">
				<p class="text-xl font-bold">Air Quality in the area</p>
				<p class="font-bold">Station</p>
				<!-- use for each here for real thing -->

				<NearAq name="Houston North Wayside C405" quality={32.07} />
				<NearAq name="Houston Bayland Park" quality={64.04} />
				<NearAq name="Vleux Carre Drive" quality={270.4} />

				<p class="mt-8 text-xl font-bold">Emission Events in the Area</p>
				<p class="mt-3">Brazos Amine Treater Facility</p>
				<p class="mt-3">Wildcat Gas Plant</p>
			</div>
		</div>
		<div class="ml-10 mr-10 w-full rounded bg-muted p-6">
			<div class="flex flex-row">
				<QualityIndicator quality={39.65} name="NPL" />
				<p class="pb-2 pl-4 text-xl font-bold">Site Overview</p>
			</div>
			<div class="grid grid-cols-4 gap-4">
				<Statistic title="Hazard Level" stat={contaminatedSite.hazardScore} />
				<Statistic title="Region ID" stat={contaminatedSite.regionID} />
				<Statistic title="EPA Site ID" stat={contaminatedSite.siteID} />
				<Statistic title="Location" stat={contaminatedSite.locationName} />
				<Statistic title="Latitude" stat={contaminatedSite.location.lat} />
				<Statistic title="Longitude" stat={contaminatedSite.location.long} />
				<Statistic title="Construction Completion" stat={contaminatedSite.constructionComplete} />
				<Statistic title="Partial Deletion" stat={contaminatedSite.partialDeletion} />
				<Statistic title="Proposed" stat={contaminatedSite.proposedDate} />
				<Statistic title="Listing" stat={contaminatedSite.listingDate} />
			</div>
			<div class="flex flex-col pt-8">
				<p class="pb-5 text-xl font-bold">Background</p>
				<p>
					Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi vestibulum elit ac
					pellentesque consectetur. In id enim eu turpis ultricies eleifend at ut nunc. Etiam vel
					congue odio. Proin ac dictum dolor. Sed et volutpat purus. Vestibulum pretium, leo quis
					posuere euismod, metus ipsum iaculis dui, in egestas urna nisi.
				</p>
				<div class="mt-3 flex flex-row items-center">
					<p class="text-lg underline">Learn More</p>
					<ChevronRight />
				</div>
			</div>
			<div class="flex flex-col pt-8">
				<p class="text-xl font-bold">Contaminant List</p>
				<DetailedContamTable items={tableInfo} />
			</div>
		</div>
	</div>
</div>
