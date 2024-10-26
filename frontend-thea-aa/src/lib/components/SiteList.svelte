<!-- <script lang="ts">
	import type { Snippet } from 'svelte'
    import { Button } from '$lib/components/ui/button'


	type siteListProps = {
		tableRenderer: Snippet<[
            items: object[], 
            loadMore: (amount: number) => void,
            initialRenderCount?: number
        ]>
		items: object[]
		name: string
		initialRenderCount?: number
	}

	let props: siteListProps = $props()
</script>

<h3>{props.name}</h3>

{@render props.tableRenderer(props.items, props.initialRenderCount)}

<Button>Load More</Button> -->
