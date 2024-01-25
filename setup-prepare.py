import os
import sys


# Check existence of version file
current_version_path = "./version.txt"
if not os.path.exists(current_version_path):
    raise Exception("Version file missing")


# Reading version and parsing it
try:
    f = open(current_version_path, 'r')
    versions = f.read().split('.')
    f.close()

    major_version = int(versions[0])
    minor_version = int(versions[1])
    patch_version = int(versions[2])
except:
    raise Exception("Error in determining existing version of package")


# Depending on parameter, Get new version number
if len(sys.argv) < 2: raise Exception("No version update specified, should be major, minor, patch or local")
if sys.argv[1] == "major": major_version += 1    
if sys.argv[1] == "minor": minor_version += 1   
if sys.argv[1] == "patch": patch_version += 1   


# New version
new_version = f"{major_version}.{minor_version}.{patch_version}"

# Save locally the version number
f = open(current_version_path, 'w')
f.write(new_version)
f.close()