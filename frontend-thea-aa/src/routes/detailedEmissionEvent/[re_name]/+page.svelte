<script lang="ts">
	import QualityIndicator from '$lib/components/QualityIndicator.svelte'
	import Statistic from '$lib/components/Statistic.svelte'
	// import type { ContaminatedSite, DetailedContaminatedSite } from '$lib/types'
	// import { onMount } from 'svelte'
	import { ChevronLeft } from 'lucide-svelte/icons'
	import NearAq from '$lib/components/NearAq.svelte'
	import DetailedEmissionTable from '$lib/components/DetailedEmissionTable.svelte'

	let { data } = $props()

	const contaminatedSite = data.emissionEventData
	const tableInfo = data.tableInfo

	let mapElement: HTMLDivElement | null = $state(null)

	// onMount(async () => {
	// 	const L = (await import('leaflet')).default

	// 	if (mapElement) {
	// 		const map = L.map(mapElement)
	// 		if (!emissionSite.lon || !emissionSite.lat) {
	// 			map.setView([29.71929, -95.3906], 13)
	// 		} else {
	// 			map.setView([emissionSite.lat, emissionSite.lon], 13)
	// 		}

	// 		L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
	// 			attribution: `&copy;<a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>,
	// 	&copy;<a href="https://carto.com/attributions" target="_blank">CARTO</a>`,
	// 			subdomains: 'abcd',
	// 			maxZoom: 19
	// 		}).addTo(map)

	// 		// ✅ Add a marker at the contaminated site
	// 		L.marker([emissionSite.lat, emissionSite.lon])
	// 			.addTo(map)
	// 			.bindPopup(emissionSite.site_name) // Optional: Add a popup
	// 			.openPopup() // Open popup by default
	// 	}
	// })
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
				<p class="text-foreground text-lg">EMISSION EVENTS</p>
			</div>
		</a>
		<p class="text-6xl font-bold">{emissionSite?.re_name}</p>
		<p class="text-foreground pt-3 text-sm">
			<span class="font-bold">Last Updated at</span> 11:45am CST October 19
		</p>
	</div>
	<div class="mt-3 flex flex-row">
		<div class="w-1/4 flex-col">
			<div bind:this={mapElement} class="h-80 w-full"></div>
			<div class="bg-muted mt-5 rounded p-5">
				<p class="text-xl font-bold">Pollution in the area</p>
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
		<div class="bg-muted ml-10 mr-10 w-full rounded p-6">
			<div class="flex flex-row">
				<QualityIndicator quality={39.65} name="Open" />
				<p class="pb-2 pl-4 text-xl font-bold">Site Overview</p>
			</div>
			<div class="grid grid-cols-4 gap-4">
				<!-- <Statistic
					title="Incident Tracking Num"
					stat={emissionSite.}
				/> -->
				<Statistic title="RN" stat={emissionSite.registration} />
				<Statistic title="Start time" stat={emissionSite.start_date_time} />
				<Statistic title="End time" stat={emissionSite.end_date_time} />
				<Statistic title="Duration" stat={emissionSite.hours_elapsed} />
				<Statistic title="Location" stat={emissionSite.physical_location} />
				<Statistic title="Latitude" stat={emissionSite.lat ? emissionSite.lat : 'Nan'} />
				<Statistic title="Longitude" stat={emissionSite.lon ? emissionSite.lon : 'Nan'} />
				<Statistic title="Cause" stat={emissionSite.cause} />
			</div>
			<!-- <div class="flex flex-col pt-8">
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
			</div> -->
			<div class="flex flex-col pt-8">
				<p class="text-xl font-bold">Contaminant List</p>
				<DetailedEmissionTable items={tableInfo} />
			</div>
		</div>
	</div>
</div>
