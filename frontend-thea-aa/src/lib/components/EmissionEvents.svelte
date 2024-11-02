<script lang="ts">
  import type { EmissionEvent } from '$lib/types';
  import LoadMore from './LoadMore.svelte'

  let props: {items: EmissionEvent[]} = $props()

  let amountToShow = $state(3)
</script>

<h3>Emission Events</h3>

<table>
  <thead>
      <tr>
      <th>Number</th>
      <th>Site</th>
      </tr>
  </thead>
  <tbody>
      {#each props.items.slice(0, amountToShow) as item, rank}
      <tr>
          <td>{rank}</td>
          <td>{item.site}</td>
      </tr>
      {/each}
  </tbody>
</table>

<LoadMore onclick={() => amountToShow += 3} />

