<script lang="ts">
	import type { ContaminatedSite } from '$lib/types'
	import LoadMore from './LoadMore.svelte'

	let props: { items: ContaminatedSite[] } = $props()

	let amountToShow = $state(3)
</script>

<div class="mx-auto max-w-4xl py-6">
	<h3 class="text-l mb-4 font-bold">Contaminated Sites Update (Superfund)</h3>

	<table class="min-w-full table-auto border-collapse">
		<thead>
			<tr class="bg-secondary">
				<th class="px-4 py-2 text-left text-sm font-medium text-secondary-foreground">Status</th>
				<th class="px-4 py-2 text-left text-sm font-medium text-secondary-foreground">Site</th>
				<th class="px-4 py-2 text-left text-sm font-medium text-secondary-foreground"
					>Hazard Score</th
				>
			</tr>
		</thead>
		<tbody>
			{#each props.items.slice(0, amountToShow) as item}
				<tr class="hover border-b">
					<td class="px-4 py-2 text-sm">{item.status}</td>
					<td class="px-4 py-2 text-sm">{item.name}</td>
					<td class="px-4 py-2 text-sm">{item.hazardScore}</td>
				</tr>
			{/each}
		</tbody>
	</table>
	<div class="pt-4">
		<LoadMore onclick={() => (amountToShow += 3)} />
	</div>
</div>
