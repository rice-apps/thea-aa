import type { DetailedContaminatedSite } from '$lib/types'

export function load() {
	// let airQualitySites: AirQualitySite[] = []
	// let emissionEvents: EmissionEvent[] = []
	// let contaminatedSites: ContaminatedSite[] = []

	// randomly generate some data

	const contaminatedSite: DetailedContaminatedSite = {
		status: 'active',
		name: 'Sol Lynn/Industrial Transformers (Houston TX)',
		location: { lat: 29.678889, long: -95.398611 },
		hazardScore: 39.65,
		regionID: 6,
		siteID: 'TXD980873327 (PDF)',
		locationName: 'Harris County, Houston, Texas',
		constructionComplete: '9/29/1993',
		partialDeletion: 'No',
		proposedDate: '10/15/1984 (PDF)',
		listingDate: '03/31/1989 (PDF)'
	}
	return contaminatedSite
}
