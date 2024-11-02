<script lang="ts">
    import * as Table from "$lib/components/ui/table/index.js";

    // Array of contaminants based on the image
    const contaminants = [
        {
            contaminantName: "CHLORETHENE (VINYL CHLORIDE)",
            contaminatedMedia: "Groundwater",
            areaOfSiteFound: "GROUNDWATER (02)",
            moreInfo: "ATSDR Profile",
            casNumber: "75-01-4"
        },
        {
            contaminantName: "CHLORETHENE (VINYL CHLORIDE)",
            contaminatedMedia: "Air",
            areaOfSiteFound: "GROUNDWATER (02)",
            moreInfo: "ATSDR Profile",
            casNumber: "75-01-4"
        },
        {
            contaminantName: "CIS-1,2-DICHLOROETHENE",
            contaminatedMedia: "Groundwater",
            areaOfSiteFound: "GROUNDWATER (02)",
            moreInfo: "ATSDR Profile",
            casNumber: "156-59-2"
        },
        {
            contaminantName: "CIS-1,2-DICHLOROETHENE",
            contaminatedMedia: "Air",
            areaOfSiteFound: "GROUNDWATER (02)",
            moreInfo: "ATSDR Profile",
            casNumber: "156-59-2"
        },
        {
            contaminantName: "POLYCHLORINATED BIPHENYLS (PCBs)",
            contaminatedMedia: "Buildings/Structures",
            areaOfSiteFound: "SOURCE (01)",
            moreInfo: "ATSDR Profile",
            casNumber: "1336-36-3"
        },
        {
            contaminantName: "POLYCHLORINATED BIPHENYLS (PCBs)",
            contaminatedMedia: "Groundwater",
            areaOfSiteFound: "GROUNDWATER (02)",
            moreInfo: "ATSDR Profile",
            casNumber: "1336-36-3"
        },
        {
            contaminantName: "POLYCHLORINATED BIPHENYLS (PCBs)",
            contaminatedMedia: "Soil",
            areaOfSiteFound: "SOURCE (01)",
            moreInfo: "ATSDR Profile",
            casNumber: "1336-36-3"
        },
        {
            contaminantName: "TRICHLOROETHENE",
            contaminatedMedia: "Groundwater",
            areaOfSiteFound: "GROUNDWATER (02)",
            moreInfo: "ATSDR Profile",
            casNumber: "79-01-6"
        },
        {
            contaminantName: "TRICHLOROETHENE",
            contaminatedMedia: "Air",
            areaOfSiteFound: "GROUNDWATER (02)",
            moreInfo: "ATSDR Profile",
            casNumber: "79-01-6"
        },
        {
            contaminantName: "TRICHLOROETHENE",
            contaminatedMedia: "Soil",
            areaOfSiteFound: "SOURCE (01)",
            moreInfo: "ATSDR Profile",
            casNumber: "79-01-6"
        }
    ];
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
