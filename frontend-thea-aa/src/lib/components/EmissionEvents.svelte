<script lang="ts">
  import type { EmissionEvent } from '$lib/types';
import LoadMore from './LoadMore.svelte'

  let props: {items: EmissionEvent[]} = $props()

  let amountToShow = $state(3)
</script>

<div class="max-w-4xl mx-auto py-6">
  <h3 class="text-l font-bold mb-4 text-gray-800">Emission Events</h3>

  <table class="min-w-full table-auto border-collapse">
    <thead>
        <tr class="bg-gray-100">
        <th class="px-4 py-2 text-left text-sm font-medium text-gray-700">Number</th>
        <th class="px-4 py-2 text-left text-sm font-medium text-gray-700">Site</th>
        </tr>
    </thead>
    <tbody>
        {#each props.items.slice(0, amountToShow) as item, rank}
        <tr>
            <td class="px-4 py-2 text-sm text-gray-700">{rank}</td>
            <td class="px-4 py-2 text-sm text-gray-700">{item.site}</td>
        </tr>
        {/each}
    </tbody>
  </table>

  <div class="pt-4">
    <LoadMore onclick={() => amountToShow += 3} />
  </div>
</div>
