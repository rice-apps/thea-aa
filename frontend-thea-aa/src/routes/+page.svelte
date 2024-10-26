<script lang="ts">
	import AirQualityRanking from '$lib/components/AirQualityRanking.svelte'
	import Map from '$lib/components/Map.svelte'
	import { Button } from '$lib/components/ui/button'

    export let data
</script>

<main class="flex">
	<aside>
		<input placeholder="search" />
		<div>
			<Button>Filter 1</Button>
			<Button>Filter 2</Button>
			<Button>Filter 3</Button>
		</div>

		<AirQualityRanking items={data.airQualitySites} />
	</aside>
	<div>
		<Map />
	</div>
</main>
