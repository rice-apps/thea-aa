
<script lang="ts">
	import QualityIndicator from "./QualityIndicator.svelte"

    let props: {name: String, quality: Number} = $props();
</script>

<div class="flex flex-row justify-between pt-5">
    <p>{props.name}</p> 
    <QualityIndicator quality={props.quality}/>
</div>

