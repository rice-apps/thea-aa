import type { ContaminatedSite } from '$lib/types'

export async function load({ params }) {
	let contaminatedApiData: ContaminatedSite
	const { epa_id } = params
	try {
		const response = await fetch('http://127.0.0.1:8000/api/superfund/retrieve/?epa_id=' + epa_id)
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

	const tableInfo: contaminantRow[] = [
	]
	
	return { contaminatedSite: contaminatedApiData, tableInfo: tableInfo }
}
