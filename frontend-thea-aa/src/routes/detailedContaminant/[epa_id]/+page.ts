import type { ContaminatedSite } from '$lib/types'
import type { LoadEvent } from '@sveltejs/kit'

export async function load({ params }: LoadEvent) {
	let contaminatedApiData: ContaminatedSite
	const { epa_id } = params
	try {
		const response = await fetch(
			`${import.meta.env.VITE_BASE_URL}/api/superfund/retrieve/?epa_id=` + epa_id
		)
		contaminatedApiData = await response.json() // assuming the response is in the correct format
	} catch (error) {
		console.error('Error fetching contaminated sites:', error)
		throw new Error('Error fetching contaminated sites:')
	}

	interface contaminantRow {
		contaminantName: string
		estQuantity: string
		quantityUnit: string
		emissionLimit: string
		emissionLimitUnit: string
		authorization: string
	}

	const tableInfo: contaminantRow[] = []

	return { contaminatedSite: contaminatedApiData, tableInfo: tableInfo }
}
