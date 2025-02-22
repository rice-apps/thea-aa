import type { DetailedEmissionEvent } from '$lib/types'

export async function load({ params }) {
	// let airQualitySites: AirQualitySite[] = []
	// let emissionEvents: EmissionEvent[] = []
	// let contaminatedSites: ContaminatedSite[] = []

	// randomly generate some data

	// const contaminatedSite: DetailedContaminatedSite = {
	// 	status: 'active',
	// 	name: 'Sol Lynn/Industrial Transformers (Houston TX)',
	// 	location: { lat: 29.678889, long: -95.398611 },
	// 	hazardScore: 39.65,
	// 	regionID: 6,
	// 	siteID: 'TXD980873327 (PDF)',
	// 	locationName: 'Harris County, Houston, Texas',
	// 	constructionComplete: '9/29/1993',
	// 	partialDeletion: 'No',
	// 	proposedDate: '10/15/1984 (PDF)',
	// 	listingDate: '03/31/1989 (PDF)'
	// }
	let bruh: DetailedEmissionEvent[]
	let emissionEventData: DetailedEmissionEvent
	console.log('params', params)
	const { re_name } = params
	console.log('re_name', re_name)

	try {
		const response = await fetch('http://127.0.0.1:8000/api/emission/retrieve/?re_name=' + re_name)
		console.log('bruh', response)
		bruh = await response.json() // assuming the response is in the correct format
		emissionEventData = bruh[0]
	} catch (error) {
		console.error('Error fetching contaminated sites:', error)
		throw new Error('Error fetching contaminated sites:')
	}

	interface EmissionRow {
		description: string
		estimatedQuantity: number
		units: string
		emissionLimit: number
		emissionUnits: string
		authorization: string
	}

	const tableInfo: EmissionRow[] = [
		{
			description: 'CO',
			estimatedQuantity: 45.16,
			units: 'Pounds',
			emissionLimit: 0.0,
			emissionUnits: 'Pounds',
			authorization: 'NRSP 175554'
		},
		{
			description: 'CO',
			estimatedQuantity: 45.16,
			units: 'Pounds',
			emissionLimit: 0.0,
			emissionUnits: 'Pounds',
			authorization: 'NRSP 175554'
		},
		{
			description: 'CO',
			estimatedQuantity: 45.16,
			units: 'Pounds',
			emissionLimit: 0.0,
			emissionUnits: 'Pounds',
			authorization: 'NRSP 175554'
		},
		{
			description: 'CO',
			estimatedQuantity: 45.16,
			units: 'Pounds',
			emissionLimit: 0.0,
			emissionUnits: 'Pounds',
			authorization: 'NRSP 175554'
		}
	]

	return { emissionSite: emissionEventData, tableInfo: tableInfo }
}
