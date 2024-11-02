<script lang="ts">
    let props: {quality: Number} = $props();
   
    const ranges = [
       { max: 50, color: 'bg-green-500', textColor: 'text-white' },    // Green
       { max: 100, color: 'bg-yellow-200', textColor: 'text-black' },  // Yellow
       { max: 150, color: 'bg-orange-500', textColor: 'text-white' },  // Orange
       { max: 200, color: 'bg-red-600', textColor: 'text-white' },     // Red
       { max: 300, color: 'bg-purple-600', textColor: 'text-white' },  // Purple
       { max: Infinity, color: 'bg-rose-900', textColor: 'text-white' } // Maroon
    ];
   
    let range = ranges.find(r => props.quality <= r.max) || ranges[ranges.length - 1];
</script>

<div class="rounded p-4 w-20 h-8 flex items-center justify-between {range.color} {range.textColor}">
    <span>{props.quality}</span>
</div>