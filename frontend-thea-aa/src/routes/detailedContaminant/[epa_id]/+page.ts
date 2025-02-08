import type { ContaminatedSite, GeocodeResponse } from '$lib/types'

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
	let contaminatedApiData: ContaminatedSite
	const { epa_id } = params
	try {
		const response = await fetch('http://127.0.0.1:8000/api/superfund/retrieve/?epa_id=' + epa_id)
		console.log(response)
		contaminatedApiData = await response.json() // assuming the response is in the correct format
	} catch (error) {
		console.error('Error fetching contaminated sites:', error)
		throw new Error('Error fetching contaminated sites:')
	}

	try {
		let street_address: string = contaminatedApiData.street_address
		street_address = street_address.replaceAll(' ', '+')
		console.log(street_address)
		const zip_code: string = contaminatedApiData.zip_code
		const city: string = contaminatedApiData.city
		const county: string = contaminatedApiData.county
		const state = 'TX'
		const country = 'US'
		const apiKey = import.meta.env.VITE_PUBLIC_API_KEY

		const url = `https://geocode.maps.co/search?street=${street_address}&city=${city}&county=${county}&state=${state}&postalcode=${zip_code}&country=${country}&api_key=${apiKey}`
		const response = await fetch(url)

		console.log(response)
		const addressResponse: GeocodeResponse[] = await response.json() // assuming the response is in the correct format
		console.log('address response', addressResponse)
		if (addressResponse.length) {
			contaminatedApiData.long_lat = {
				lat: parseFloat(addressResponse[0].lat),
				long: parseFloat(addressResponse[0].lon)
			}
			console.log('bruh changed', contaminatedApiData)
		}
	} catch (error) {
		console.error('Error fetching contaminated sites:', error)
		throw new Error('Error fetching contaminated sites:')
	}
	console.log('data', contaminatedApiData)

	interface contaminantRow {
		contaminantName: string
		contaminatedMedia: string
		areaOfSiteFound: string
		moreInfo: string
		casNumber: string
	}

	const tableInfo: contaminantRow[] = [
		{
			contaminantName: 'CHLORETHENE (VINYL CHLORIDE)',
			contaminatedMedia: 'Groundwater',
			areaOfSiteFound: 'GROUNDWATER (02)',
			moreInfo: 'ATSDR Profile',
			casNumber: '75-01-4'
		},
		{
			contaminantName: 'CHLORETHENE (VINYL CHLORIDE)',
			contaminatedMedia: 'Air',
			areaOfSiteFound: 'GROUNDWATER (02)',
			moreInfo: 'ATSDR Profile',
			casNumber: '75-01-4'
		},
		{
			contaminantName: 'CIS-1,2-DICHLOROETHENE',
			contaminatedMedia: 'Groundwater',
			areaOfSiteFound: 'GROUNDWATER (02)',
			moreInfo: 'ATSDR Profile',
			casNumber: '156-59-2'
		},
		{
			contaminantName: 'CIS-1,2-DICHLOROETHENE',
			contaminatedMedia: 'Air',
			areaOfSiteFound: 'GROUNDWATER (02)',
			moreInfo: 'ATSDR Profile',
			casNumber: '156-59-2'
		},
		{
			contaminantName: 'POLYCHLORINATED BIPHENYLS (PCBs)',
			contaminatedMedia: 'Buildings/Structures',
			areaOfSiteFound: 'SOURCE (01)',
			moreInfo: 'ATSDR Profile',
			casNumber: '1336-36-3'
		},
		{
			contaminantName: 'POLYCHLORINATED BIPHENYLS (PCBs)',
			contaminatedMedia: 'Groundwater',
			areaOfSiteFound: 'GROUNDWATER (02)',
			moreInfo: 'ATSDR Profile',
			casNumber: '1336-36-3'
		},
		{
			contaminantName: 'POLYCHLORINATED BIPHENYLS (PCBs)',
			contaminatedMedia: 'Soil',
			areaOfSiteFound: 'SOURCE (01)',
			moreInfo: 'ATSDR Profile',
			casNumber: '1336-36-3'
		},
		{
			contaminantName: 'TRICHLOROETHENE',
			contaminatedMedia: 'Groundwater',
			areaOfSiteFound: 'GROUNDWATER (02)',
			moreInfo: 'ATSDR Profile',
			casNumber: '79-01-6'
		},
		{
			contaminantName: 'TRICHLOROETHENE',
			contaminatedMedia: 'Air',
			areaOfSiteFound: 'GROUNDWATER (02)',
			moreInfo: 'ATSDR Profile',
			casNumber: '79-01-6'
		},
		{
			contaminantName: 'TRICHLOROETHENE',
			contaminatedMedia: 'Soil',
			areaOfSiteFound: 'SOURCE (01)',
			moreInfo: 'ATSDR Profile',
			casNumber: '79-01-6'
		}
	]
	return { contaminatedSite: contaminatedApiData, tableInfo: tableInfo }
}
