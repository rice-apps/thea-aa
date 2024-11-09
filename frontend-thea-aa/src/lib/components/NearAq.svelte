
<script lang="ts">
	import QualityIndicator from "./QualityIndicator.svelte"

    let props: {name: string, quality: number} = $props();
</script>

<div class="flex flex-row justify-between pt-5">
    <p>{props.name}</p> 
    <QualityIndicator quality={props.quality}/>
</div>

