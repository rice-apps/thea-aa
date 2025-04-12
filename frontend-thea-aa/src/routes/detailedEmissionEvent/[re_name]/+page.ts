import type { DetailedEmissionEvent } from '$lib/types'

export async function load({ params }: { params: { re_name: string } }) {
	let tableInfo: ContaminantRow[] = []
	let emissionEventData: DetailedEmissionEvent
	const { re_name } = params

	try {
		const response = await fetch('http://127.0.0.1:8000/api/emission/retrieve/?re_name=' + re_name)
		if (!response.ok) {
			throw new Error(`HTTP error! Status: ${response.status}`)
		}

		const data = await response.json()
		console.log('response', data)

		if (Array.isArray(data) && data.length > 0) {
			emissionEventData = data[0]
			tableInfo = emissionEventData.contaminants.map((contaminant) => ({
				contaminantName: contaminant.name,
				estQuantity: contaminant.est_quantity,
				quantityUnit: contaminant.quantity_unit,
				emissionLimit: contaminant.emission_limit,
				emissionLimitUnit: contaminant.emission_limit_unit,
				authorization: contaminant.authorization
			}))
			return { emissionEventData, tableInfo }
		} else {
			throw new Error('Data is empty')
		}
	} catch (error) {
		console.error('Error fetching contaminated sites:', error)
		throw new Error('Error fetching contaminated sites:')
	}
}

interface ContaminantRow {
	contaminantName: string
	estQuantity: string
	quantityUnit: string
	emissionLimit: string
	emissionLimitUnit: string
	authorization: string
}
