<script lang="ts">
    let props: {title: String, stat: number | string} = $props();
</script>

<div class="flex flex-col pt-3">
    <p class="text-foreground pb-2">{props.title}</p>
    <p>{props.stat}</p>
</div>