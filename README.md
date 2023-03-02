# Spherical Map Converter
## Description
A simple Python (version 3.9.13) program that takes in an image and transforms it into something akin to an Equirectangular Projection.  

### Intuition
Some of the key concepts that give clues on how to solve this are:
* The center parallel (or equator) has to encompass the diameter of the sphere.
* The center parallel and center meridian should remain the same after the transform to preserve the width and height of the original image.
* Every scanline corresponds to a layer of the sphere, in other words, every scanline is a circle with the radius corresponding to the distance of the scanline to the equator of the sphere.
* The distortion of the longitude should be more noticeable at the poles. 

## Motivation
This script was written in order to facilitate the creation of spherical textures from already existing images in a relatively quick and easy way. This way we can mitigate the distortion that happens at the poles when applying a texture to a sphere.
