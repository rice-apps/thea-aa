<script lang="ts">
	import type { EmissionEvent } from '$lib/types'
	import { onMount } from 'svelte'
	import { ArrowLeft } from 'lucide-svelte'
	import { ArrowRight } from 'lucide-svelte'
	import { Button } from '$lib/components/ui/button'
	import { goto } from '$app/navigation'

	let props: { items: EmissionEvent[] } = $props()

	let page = $state(0)
	let allPages = $state<EmissionEvent[][]>([])
	let indices = $state<number[]>([])
	let itemsPerPage = 5

	const paginate = (items: EmissionEvent[]) => {
		const pages = Math.ceil(items.length / itemsPerPage)
		const paginatedItems = Array.from({ length: pages }, (_, index) => {
			const start = index * itemsPerPage
			return items.slice(start, start + itemsPerPage)
		})
		return paginatedItems
	}

	const setPage = (pageNumber: number) => {
		if (pageNumber >= 0 && pageNumber < allPages.length) {
			page = pageNumber
		}
	}

	onMount(() => {
		allPages = paginate(props.items)
		indices = Array.from({ length: allPages.length }, (_, i) => i)
	})

	const goToDetail = (item: EmissionEvent) => {
		goto(`/detailedEmissionEvent/${item.re_name}`) // Navigate to the detailed page with the epaId
	}
</script>

<div class="mx-auto max-w-4xl py-6">
	<h3 class="text-l mb-4 font-bold">Emission Events</h3>

	<table class="min-w-full table-auto border-collapse">
		<thead>
			<tr class="bg-secondary">
				<th class="px-4 py-2 text-left text-sm font-medium text-secondary-foreground">Number</th>
				<th class="px-4 py-2 text-left text-sm font-medium text-secondary-foreground">Site</th>
			</tr>
		</thead>
		<tbody>
			{#each props.items.slice(page * itemsPerPage, (page + 1) * itemsPerPage) as item}
				<tr onclick={() => goToDetail(item)} class="hover cursor-pointer border-b">
					<!-- <td class="px-4 py-2 text-sm">{item.}</td> -->
					<td class="px-4 py-2 text-sm">{item.re_name}</td>
				</tr>
			{/each}
		</tbody>
	</table>

	<div class="content-center pt-4">
		<Button on:click={() => setPage(page - 1)} class="bg-primary-foreground"
			><ArrowLeft size={10} class="text-primary"></ArrowLeft></Button
		>
		{#each indices as i}
			<Button on:click={() => setPage(i)} class="bg-primary-foreground text-primary">{i + 1}</Button
			>
		{/each}
		<Button on:click={() => setPage(page + 1)} class="bg-primary-foreground"
			><ArrowRight size={10} class="text-primary"></ArrowRight></Button
		>
	</div>
</div>
