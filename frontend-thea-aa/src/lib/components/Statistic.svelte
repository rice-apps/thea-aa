<script lang="ts">
    let props: {title: String, stat: any} = $props();
</script>

<div class="flex flex-col pt-3">
    <p class="text-stone-600 pb-2">{props.title}</p>
    <p>{props.stat}</p>
</div>