<script lang="ts">
	import * as Table from '$lib/components/ui/table/index.js'
	interface ContaminantRow {
		contaminantName: string
		estQuantity: string
		quantityUnit: string
		emissionLimit: string
		emissionLimitUnit: string
		authorization: string
	}
	// Array of contaminants based on the image

	let props: { items: ContaminantRow[] } = $props()
	const contaminants: ContaminantRow[] = props.items
</script>

<Table.Root>
	<Table.Header>
		<Table.Row>
			<Table.Head>Description</Table.Head>
			<Table.Head>Est. Quantity/Opacity</Table.Head>
			<Table.Head>Units</Table.Head>
			<Table.Head>Emission Limit</Table.Head>
			<Table.Head>Emission Limit Units</Table.Head>
			<Table.Head>Authorization</Table.Head>
		</Table.Row>
	</Table.Header>
	<Table.Body>
		{#each contaminants as contaminant}
			<Table.Row>
				<Table.Cell>{contaminant.contaminantName}</Table.Cell>
				<Table.Cell>{contaminant.estQuantity}</Table.Cell>
				<Table.Cell>{contaminant.quantityUnit}</Table.Cell>
				<Table.Cell>{contaminant.emissionLimit}</Table.Cell>
				<Table.Cell>{contaminant.emissionLimitUnit}</Table.Cell>
				<Table.Cell>{contaminant.authorization}</Table.Cell>
			</Table.Row>
		{/each}
	</Table.Body>
</Table.Root>
