<script lang="ts">
    import * as Table from "$lib/components/ui/table/index.js";
    interface contaminantRow {
        contaminantName: string
        contaminatedMedia: string
        areaOfSiteFound: string
        moreInfo: string
        casNumber: string
    }
    // Array of contaminants based on the image

    let props: {items: Array<contaminantRow>} = $props()
    const contaminants: Array<contaminantRow> = props.items
</script>

<Table.Root>
    <Table.Header>
        <Table.Row>
            <Table.Head class="w-[200px]">Contaminant Name</Table.Head>
            <Table.Head>Contaminated Media</Table.Head>
            <Table.Head>Area of Site Found (Operable Unit)</Table.Head>
            <Table.Head>More Information</Table.Head>
            <Table.Head class="text-right">CAS #</Table.Head>
        </Table.Row>
    </Table.Header>
    <Table.Body>
        {#each contaminants as contaminant, i (i)}
            <Table.Row>
                <Table.Cell class="font-medium">{contaminant.contaminantName}</Table.Cell>
                <Table.Cell>{contaminant.contaminatedMedia}</Table.Cell>
                <Table.Cell>{contaminant.areaOfSiteFound}</Table.Cell>
                <Table.Cell><a href="#">{contaminant.moreInfo}</a></Table.Cell>
                <Table.Cell class="text-right">{contaminant.casNumber}</Table.Cell>
            </Table.Row>
        {/each}
    </Table.Body>
</Table.Root>
