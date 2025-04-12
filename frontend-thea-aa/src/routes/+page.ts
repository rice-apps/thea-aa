// ===============================================
// +page.ts
// Server-side load function for the route
// Fetches environmental data for map and panel display
// ===============================================
import type { AirQualitySite, ContaminatedSite, DetailedEmissionEvent } from '$lib/types'

// ===============================================
// `load()` function — called by SvelteKit
// Runs on server before +page.svelte renders
// Returns props: airQualitySites, emissionEvents, contaminatedSites
// ===============================================
export async function load() {
	// ===============================================
	// Static data for air quality monitoring stations
	// Used directly without API call
	// ===============================================
	const airQualitySites: AirQualitySite[] = [
		{ station: 'Green Park', location: { lat: 51.5074, long: -0.1278 }, airQuality: 42 },
		{ station: 'Central Station', location: { lat: 40.7128, long: -74.006 }, airQuality: 58 },
		{ station: 'River View', location: { lat: 34.0522, long: -118.2437 }, airQuality: 30 },
		{ station: 'Sunset Boulevard', location: { lat: 34.0522, long: -118.2437 }, airQuality: 47 },
		{ station: 'Downtown Hub', location: { lat: 41.8781, long: -87.6298 }, airQuality: 55 },
		{ station: 'Seaside', location: { lat: 36.7783, long: -119.4179 }, airQuality: 20 },
		{ station: 'Mountain Peak', location: { lat: 39.7392, long: -104.9903 }, airQuality: 35 },
		{ station: 'City Square', location: { lat: 51.1657, long: 10.4515 }, airQuality: 65 },
		{ station: 'Lakefront', location: { lat: 45.5231, long: -122.6765 }, airQuality: 50 }
	]

	// ===============================================
	// Contaminated Sites + Emission Events (via API)
	// Data fetched from local backend server
	// ===============================================
	let contaminatedApiData: ContaminatedSite[] = []
	let emissionEventsApiData: DetailedEmissionEvent[] = []

	try {
		// 🌐 Fetch contaminated Superfund sites
		const superfundResponse = await fetch('http://127.0.0.1:8000/api/superfund/retrieve/')

		// 🌐 Fetch emission events
		const emissionEventsResponse = await fetch('http://127.0.0.1:8000/api/emission/retrieve/')

		// Parse responses as JSON
		contaminatedApiData = await superfundResponse.json() // assuming the response is in the correct format
		emissionEventsApiData = await emissionEventsResponse.json()
	} catch (error) {
		console.error('Error fetching contaminated sites:', error)
		contaminatedApiData = [] // Return an empty array on error
		emissionEventsApiData = []
	}

	return {
		airQualitySites: airQualitySites,
		emissionEvents: emissionEventsApiData,
		contaminatedSites: contaminatedApiData
	}
}
