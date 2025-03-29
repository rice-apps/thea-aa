<script lang="ts">
	import type { AirQualitySite } from '$lib/types'
	import LoadMore from './LoadMore.svelte'

	let props: { items: AirQualitySite[] } = $props()

	let amountToShow = $state(3)
</script>

<div class="mx-auto max-w-4xl py-6">
	<h3 class="text-l mb-4 font-bold">Air Quality Ranking</h3>
	<table class="min-w-full table-auto border-collapse">
		<thead>
			<tr class="bg-secondary">
				<th class="px-4 py-2 text-left text-sm font-medium text-secondary-foreground">Rank</th>
				<th class="px-4 py-2 text-left text-sm font-medium text-secondary-foreground">City</th>
				<th class="px-4 py-2 text-left text-sm font-medium text-secondary-foreground">Quality</th>
			</tr>
		</thead>
		<tbody>
			{#each props.items.slice(0, amountToShow) as item, rank}
				<tr class="border-b">
					<td class="px-4 py-2 text-sm">{rank}</td>
					<td class="px-4 py-2 text-sm">{item.station}</td>
					<td class="px-4 py-2 text-sm">{item.airQuality}</td>
				</tr>
			{/each}
		</tbody>
	</table>
</div>

<LoadMore onclick={() => (amountToShow += 3)} />
