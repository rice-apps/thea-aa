<script lang="ts">
    let {quality = 0.0, name = ""} = $props();
   
    const ranges = [
       { max: 0, color: 'bg-black'},    // Green
       { max: 50, color: 'bg-green-500'},    // Green
       { max: 100, color: 'bg-yellow-300'},  // Yellow
       { max: 150, color: 'bg-orange-500'},  // Orange
       { max: 200, color: 'bg-red-600'},     // Red
       { max: 300, color: 'bg-purple-600'},  // Purple
       { max: Infinity, color: 'bg-rose-900'} // Maroon
    ];
   
    let range = ranges.find(r => quality <= r.max) || ranges[ranges.length - 1];
</script>

<div class="text-white rounded w-20 h-8 flex text-center items-center justify-center {range.color} {range.textColor}">
    {#if name == ""}
        <span>{quality}</span>
    {:else}
        <span>{name}</span>
    {/if}
</div>