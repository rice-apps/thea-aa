export interface LatLong {
	lat: number
	long: number
}

export interface GeocodeResponse {
	class: string
	display_name: string
	importance: number
	lat: string
	licence: string
	lon: string
	osm_id: number
	osm_type: string
	place_id: number
	type: string
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
	name: string
	// location: string
	epa_id: string
	site_name: string
	city: string
	county: string
	state: string
	street_address: string
	long_lat: LatLong
	zip_code: string
	region: string
	npl_status: string
	partial_npl_deletion: string
	superfund_alternative_approach: string
	site_wide_ready_for_anticipated_use: string
	human_exposure_under_control: string
	groundwater_migration_under_control: string
	construction_complete: string
	construction_completion_date: string // Consider changing this to Date if needed
	non_npl_status_category: string
	non_npl_status_subcategory: string
	site_status: string
	site_type: string
	site_type_subcategory: string
	federal_agency: string
	native_american_interest: string
	indian_entity_nai_status: string
	hrs_score: string
	federal_facility_indicator: string
	alias_alternative_site_name: string
	non_npl_status_date: string // Consider changing this to Date if needed
	superfund_site_profile_page_url: string
	rcra_handler_id_name: string
}

// export interface ContaminatedSite {
// 	status: string
// 	name: string
// 	location: LatLong
// 	hazardScore: number
// }

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
