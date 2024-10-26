type LatLong = {
    lat: number
    long: number
}

export type AirQualitySite = {
    station: string
    location: LatLong
    airQuality: number
}

export type EmissionEvent = {
    location: LatLong
    number: number
    site: string
}

export type ContaminatedSite = {
    status: string
    name: string
    location: LatLong
    hazardScore: number
}