<script lang="ts">
    import type { AirQualitySite } from '$lib/types';
	import LoadMore from './LoadMore.svelte'

    let props: {items: AirQualitySite[]} = $props()

    let amountToShow = $state(3)
</script>

<h3>Air Quality Ranking</h3>

<table>
    <thead>
        <tr>
        <th>Rank</th>
        <th>City</th>
        <th>Quality</th>
        </tr>
    </thead>
    <tbody>
        {#each props.items.slice(0, amountToShow) as item, rank}
        <tr>
            <td>{rank}</td>
            <td>{item.station}</td>
            <td>{item.airQuality}</td>
        </tr>
        {/each}
    </tbody>
</table>

<LoadMore onclick={() => amountToShow += 3} />

