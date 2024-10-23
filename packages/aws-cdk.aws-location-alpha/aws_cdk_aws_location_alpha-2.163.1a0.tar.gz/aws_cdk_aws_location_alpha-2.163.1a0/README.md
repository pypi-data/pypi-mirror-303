# AWS::Location Construct Library

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Experimental](https://img.shields.io/badge/cdk--constructs-experimental-important.svg?style=for-the-badge)

> The APIs of higher level constructs in this module are experimental and under active development.
> They are subject to non-backward compatible changes or removal in any future version. These are
> not subject to the [Semantic Versioning](https://semver.org/) model and breaking changes will be
> announced in the release notes. This means that while you may use them, you may need to update
> your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

Amazon Location Service lets you add location data and functionality to applications, which
includes capabilities such as maps, points of interest, geocoding, routing, geofences, and
tracking. Amazon Location provides location-based services (LBS) using high-quality data from
global, trusted providers Esri and HERE. With affordable data, tracking and geofencing
capabilities, and built-in metrics for health monitoring, you can build sophisticated
location-enabled applications.

## Place Index

A key function of Amazon Location Service is the ability to search the geolocation information.
Amazon Location provides this functionality via the Place index resource. The place index includes
which [data provider](https://docs.aws.amazon.com/location/latest/developerguide/what-is-data-provider.html)
to use for the search.

To create a place index, define a `PlaceIndex`:

```python
location.PlaceIndex(self, "PlaceIndex",
    place_index_name="MyPlaceIndex",  # optional, defaults to a generated name
    data_source=location.DataSource.HERE
)
```

Use the `grant()` or `grantSearch()` method to grant the given identity permissions to perform actions
on the place index:

```python
# role: iam.Role


place_index = location.PlaceIndex(self, "PlaceIndex")
place_index.grant_search(role)
```

## Geofence Collection

Geofence collection resources allow you to store and manage geofences—virtual boundaries on a map.
You can evaluate locations against a geofence collection resource and get notifications when the location
update crosses the boundary of any of the geofences in the geofence collection.

```python
# key: kms.Key


location.GeofenceCollection(self, "GeofenceCollection",
    geofence_collection_name="MyGeofenceCollection",  # optional, defaults to a generated name
    kms_key=key
)
```

Use the `grant()` or `grantRead()` method to grant the given identity permissions to perform actions
on the geofence collection:

```python
# role: iam.Role


geofence_collection = location.GeofenceCollection(self, "GeofenceCollection",
    geofence_collection_name="MyGeofenceCollection"
)

geofence_collection.grant_read(role)
```

## Route Calculator

Route calculator resources allow you to find routes and estimate travel time based on up-to-date road network and live traffic information from your chosen data provider.

For more information, see [Routes](https://docs.aws.amazon.com/location/latest/developerguide/route-concepts.html).

To create a route calculator, define a `RouteCalculator`:

```python
location.RouteCalculator(self, "RouteCalculator",
    route_calculator_name="MyRouteCalculator",  # optional, defaults to a generated name
    data_source=location.DataSource.ESRI
)
```

Use the `grant()` or `grantRead()` method to grant the given identity permissions to perform actions
on the route calculator:

```python
# role: iam.Role


route_calculator = location.RouteCalculator(self, "RouteCalculator",
    data_source=location.DataSource.ESRI
)
route_calculator.grant_read(role)
```
