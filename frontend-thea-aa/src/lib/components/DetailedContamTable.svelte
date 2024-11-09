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
            <Table.Head >CAS #</Table.Head>
        </Table.Row>
    </Table.Header>
    <Table.Body>
        {#each contaminants as contaminant}
            <Table.Row>
                <Table.Cell>{contaminant.contaminantName}</Table.Cell>
                <Table.Cell>{contaminant.contaminatedMedia}</Table.Cell>
                <Table.Cell>{contaminant.areaOfSiteFound}</Table.Cell>
                <Table.Cell>{contaminant.moreInfo}</Table.Cell>
                <Table.Cell >{contaminant.casNumber}</Table.Cell>
            </Table.Row>
        {/each}
    </Table.Body>
</Table.Root>
