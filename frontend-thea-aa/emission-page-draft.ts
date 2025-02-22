// import type { LoadEvent } from '@sveltejs/kit'

// export async function load({ params }: LoadEvent) {
// 	const { registration } = params
// 	let emissionApiData = null
// 	let tableInfo = []

// 	try {
// 		// get the data for given registration_id of emission data
// 		const response = await fetch(
// 			`http://127.0.0.1:8000/api/emission/retrieve/?registration=${registration}`
// 		)
// 		const emissionsData = await response.json()

// 		// change this to either handle the multiple entries returned for the same site or change the backend
// 		if (emissionsData) {
// 			tableInfo = emissionsData.map((event: any) => ({
// 				contaminantName: event.contaminant,
// 				estQuantity: event.contaminant_est_quantity,
// 				quantityUnit: event.contaminant_est_quantity_units,
// 				emissionLimit: event.contaminant_emissions_limit,
// 				emissionLimitUnit: event.contaminant_emissions_limit_units,
// 				authorization: event.authorization
// 			}))
// 		}
// 	} catch (error) {
// 		console.error('Error fetching emission data:', error)
// 		throw new Error('Error fetching emission data')
// 	}

// 	return { emissionData: emissionApiData, tableInfo: tableInfo }
// }
