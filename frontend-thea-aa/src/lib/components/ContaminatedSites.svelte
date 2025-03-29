<script lang="ts">
	import type { ContaminatedSite } from '$lib/types'
	import LoadMore from './LoadMore.svelte'
	import { goto } from '$app/navigation'
	let props: { items: ContaminatedSite[] } = $props()
	console.log(props)

	let amountToShow = $state(3)

	const goToDetail = (item: ContaminatedSite) => {
		goto(`/detailedContaminant/${item.epa_id}`) // Navigate to the detailed page with the epaId
	}
</script>

<div class="mx-auto max-w-4xl py-6">
	<h3 class="text-l mb-4 font-bold">Contaminated Sites Update (Superfund)</h3>

	<table>
		<thead>
			<tr>
				<th>Status</th>
				<th>Site</th>
				<th>Hazard Score</th>
			</tr>
		</thead>
		<tbody>
			{#each props.items.slice(0, amountToShow) as item}
				<tr onclick={() => goToDetail(item)} class="hover cursor-pointer border-b">
					<td class="px-4 py-2 text-sm">{item.site_status}</td>
					<td class="px-4 py-2 text-sm">{item.site_name}</td>
					<td class="px-4 py-2 text-sm">{item.hrs_score == 'nan' ? 'No data' : item.hrs_score}</td>
				</tr>
			{/each}
		</tbody>
	</table>

	<div class="pt-4">
		<LoadMore onclick={() => (amountToShow += 3)} />
	</div>
</div>
