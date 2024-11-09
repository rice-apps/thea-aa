import type { AirQualitySite, EmissionEvent, ContaminatedSite } from '$lib/types'

export function load() {
	// let airQualitySites: AirQualitySite[] = []
	// let emissionEvents: EmissionEvent[] = []
	// let contaminatedSites: ContaminatedSite[] = []

	// randomly generate some data
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
	const emissionEvents: EmissionEvent[] = [
		{ location: { lat: 51.5074, long: -0.1278 }, number: 120, site: 'Green Park' },
		{ location: { lat: 40.7128, long: -74.006 }, number: 95, site: 'Central Station' },
		{ location: { lat: 34.0522, long: -118.2437 }, number: 76, site: 'River View' },
		{ location: { lat: 34.0522, long: -118.2437 }, number: 88, site: 'Sunset Boulevard' },
		{ location: { lat: 41.8781, long: -87.6298 }, number: 54, site: 'Downtown Hub' },
		{ location: { lat: 36.7783, long: -119.4179 }, number: 40, site: 'Seaside' },
		{ location: { lat: 39.7392, long: -104.9903 }, number: 30, site: 'Mountain Peak' },
		{ location: { lat: 51.1657, long: 10.4515 }, number: 85, site: 'City Square' },
		{ location: { lat: 45.5231, long: -122.6765 }, number: 50, site: 'Lakefront' }
	]
	const contaminatedSites: ContaminatedSite[] = [
		{
			status: 'active',
			name: 'Old Factory Site',
			location: { lat: 52.5074, long: -0.1278 },
			hazardScore: 75
		},
		{
			status: 'remediated',
			name: 'Abandoned Warehouse',
			location: { lat: 41.7128, long: -74.006 },
			hazardScore: 40
		},
		{
			status: 'active',
			name: 'Chemical Spill Area',
			location: { lat: 86.0522, long: -117.2437 },
			hazardScore: 80
		},
		{
			status: 'active',
			name: 'Landfill Site',
			location: { lat: 35.0522, long: -119.2437 },
			hazardScore: 60
		},
		{
			status: 'remediated',
			name: 'Old Mining Site',
			location: { lat: 40.8781, long: -88.6298 },
			hazardScore: 30
		},
		{
			status: 'active',
			name: 'Toxic Waste Dump',
			location: { lat: 37.7783, long: -119.4179 },
			hazardScore: 90
		},
		{
			status: 'active',
			name: 'Contaminated River Bank',
			location: { lat: 39.7392, long: -105.9903 },
			hazardScore: 70
		},
		{
			status: 'remediated',
			name: 'Industrial Park',
			location: { lat: 51.1657, long: 11.4515 },
			hazardScore: 20
		},
		{
			status: 'active',
			name: 'Polluted Lake',
			location: { lat: 45.5231, long: -123.6765 },
			hazardScore: 85
		}
	]

	return {
		airQualitySites: airQualitySites,
		emissionEvents: emissionEvents,
		contaminatedSites: contaminatedSites
	}
}
