<script lang="ts">
    import type { ContaminatedSite } from '$lib/types';
	import LoadMore from './LoadMore.svelte'

    let props: {items: ContaminatedSite[]} = $props()

    let amountToShow = $state(3)
</script>

<div class="max-w-4xl mx-auto py-6">
    <h3 class="text-l font-bold mb-4 text-gray-800">Contaminated Sites Update (Superfund)</h3>

    <table class="min-w-full table-auto border-collapse">
        <thead>
            <tr class="bg-gray-100">
                <th class="px-4 py-2 text-left text-sm font-medium text-gray-700">Status</th>
                <th class="px-4 py-2 text-left text-sm font-medium text-gray-700">Site</th>
                <th class="px-4 py-2 text-left text-sm font-medium text-gray-700">Hazard Score</th>
            </tr>
        </thead>
        <tbody>
            {#each props.items.slice(0, amountToShow) as item}
            <tr class="border-b hover:bg-gray-50">
                <td class="px-4 py-2 text-sm text-gray-700">{item.status}</td>
                <td class="px-4 py-2 text-sm text-gray-700">{item.name}</td>
                <td class="px-4 py-2 text-sm text-gray-700">{item.hazardScore}</td>
            </tr>
            {/each}
        </tbody>
    </table>
    <div class="pt-4">
        <LoadMore onclick={() => amountToShow += 3} />
    </div>
</div>