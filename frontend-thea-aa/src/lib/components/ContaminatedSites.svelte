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

<h3>Contaminated Sites</h3>

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
			<tr onclick={() => goToDetail(item)}>
				<td>{item.site_status}</td>
				<td>{item.site_name}</td>
				<td>{item.hrs_score}</td>
			</tr>
		{/each}
	</tbody>
</table>

<LoadMore onclick={() => (amountToShow += 3)} />
