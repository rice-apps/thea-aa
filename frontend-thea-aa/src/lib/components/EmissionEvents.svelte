<script lang="ts">
	import type { EmissionEvent } from '$lib/types'
	import { onMount } from 'svelte'
	import ArrowLeft from 'lucide-svelte/icons/arrow-left'
	import ArrowRight from 'lucide-svelte/icons/arrow-right'
	import { Button } from '$lib/components/ui/button'
	import { goto } from '$app/navigation'

	let props: { items: EmissionEvent[] } = $props()

	let page = $state(0)
	let allPages = $state<EmissionEvent[][]>([])
	let startPage = $state(0)
	let endPage = $state(0)
	let itemsPerPage = 5
	let numPageButtons = 5

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
			if (
				pageNumber > Math.floor(numPageButtons / 2) &&
				pageNumber < allPages.length - Math.floor(numPageButtons / 2)
			) {
				startPage = Math.max(1, page - Math.floor(numPageButtons / 2))
			} else if (pageNumber <= Math.floor(numPageButtons / 2)) {
				startPage = 0
			} else if (pageNumber >= allPages.length - Math.floor(numPageButtons / 2)) {
				startPage = allPages.length - numPageButtons
			}
			endPage = Math.min(startPage + numPageButtons, allPages.length - 1)
		}
	}

	onMount(() => {
		allPages = paginate(props.items)
		endPage = Math.min(allPages.length, numPageButtons)
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
				<th class="px-4 py-2 text-left text-sm font-medium text-secondary-foreground"
					>Registration Number</th
				>
				<th class="px-4 py-2 text-left text-sm font-medium text-secondary-foreground">Site</th>
			</tr>
		</thead>
		<tbody>
			{#each props.items.slice(page * itemsPerPage, (page + 1) * itemsPerPage) as item}
				<tr onclick={() => goToDetail(item)} class="hover cursor-pointer border-b">
					<td class="px-4 py-2 text-sm">{item.registration}</td>
					<td class="px-4 py-2 text-sm">{item.re_name}</td>
				</tr>
			{/each}
		</tbody>
	</table>

	<div class="content-center pt-4">
		<Button on:click={() => setPage(page - 1)} class="bg-primary-foreground"
			><ArrowLeft size={10} class="text-primary"></ArrowLeft></Button
		>
		{#each Array.from({ length: endPage - startPage }, (_, i) => i + startPage) as i}
			<Button
				on:click={() => setPage(i)}
				class={page === i ? '' : 'bg-primary-foreground text-primary'}>{i + 1}</Button
			>
		{/each}
		<Button on:click={() => setPage(page + 1)} class="bg-primary-foreground"
			><ArrowRight size={10} class="text-primary"></ArrowRight></Button
		>
	</div>
</div>
