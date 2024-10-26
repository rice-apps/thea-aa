<script lang="ts">
    import { Button } from "$lib/components/ui/button";

    let props: {
        onclick: () => void;
    } = $props()
</script>


<Button on:click={props.onclick}>Load More</Button>