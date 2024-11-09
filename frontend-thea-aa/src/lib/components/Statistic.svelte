<script lang="ts">
	let props: { title: string; stat: number | string } = $props()
</script>

<div class="flex flex-col pt-3">
	<p class="pb-2 text-foreground">{props.title}</p>
	<p>{props.stat}</p>
</div>
