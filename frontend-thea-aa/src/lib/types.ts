export interface LatLong {
	lat: number
	long: number
}

export interface AirQualitySite {
	station: string
	location: LatLong
	airQuality: number
}

export interface EmissionEvent {
	location: LatLong
	number: number
	site: string
}

export interface ContaminatedSite {
	status: string
	name: string
	location: LatLong
	hazardScore: number
}

export interface DetailedContaminatedSite {
	status: string
	name: string
	location: LatLong
	hazardScore: number
	regionID: number
	siteID: string
	locationName: string
	constructionComplete: string
	partialDeletion: string
	proposedDate: string
	listingDate: string
}

export interface DetailedContaminatedSite {
	status: string
	name: string
	location: LatLong
	hazardScore: number
	regionID: number
	siteID: string
	locationName: string
	constructionComplete: string
	partialDeletion: string
	proposedDate: string
	listingDate: string
}
