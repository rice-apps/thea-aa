<script lang="ts">
	import type { ContaminatedSite } from '$lib/types'
	import LoadMore from './LoadMore.svelte'

	let props: { items: ContaminatedSite[] } = $props()

	let amountToShow = $state(3)
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
			<tr>
				<td>{item.status}</td>
				<td>{item.name}</td>
				<td>{item.hazardScore}</td>
			</tr>
		{/each}
	</tbody>
</table>

<LoadMore onclick={() => (amountToShow += 3)} />
