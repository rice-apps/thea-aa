<script lang="ts">
	let { quality = 0.0, name = '' } = $props()

	const ranges = [
		{ max: 0, color: 'bg-black' }, // Green
		{ max: 50, color: 'bg-green-500' }, // Green
		{ max: 100, color: 'bg-yellow-300' }, // Yellow
		{ max: 150, color: 'bg-orange-500' }, // Orange
		{ max: 200, color: 'bg-red-600' }, // Red
		{ max: 300, color: 'bg-purple-600' }, // Purple
		{ max: Infinity, color: 'bg-rose-900' } // Maroon
	]

	// Calculate the range index based on quality
	let rangeIndex = Math.min(
		ranges.findIndex((r) => quality <= r.max),
		ranges.length - 1 // Ensure it doesn't go out of bounds
	)

	// Access the correct range directly by index
	let range = ranges[rangeIndex]
</script>

<div
	class="flex h-8 w-20 items-center justify-center rounded text-center text-white {range.color} {range.color}"
>
	{#if name === ''}
		<span>{quality}</span>
	{:else}
		<span>{name}</span>
	{/if}
</div>
