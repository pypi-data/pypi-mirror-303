
# yasfs - Yet Another Simple File Sorter

**Version:** 1.0  
**Description:** yasfs is a Python-based command-line tool that organizes and sorts files by their extension types.

## Installation
You can install this repo directly from PyPI using `pip`:
```bash
pip install yasfs
```
Or, you can install directly from this repository:
```bash
pip install git+https://github.com/ashaider/yet-another-simple-file-sorter.git
```

## Usage
### To get help with commandline arguments
```bash
yasfs --help
```
### Basic Usage
```bash
yasfs -s /path/to/source -d /path/to/destination
```
### Optional Arguments
- `--source` or `-s`: The path to the directory where the files will be read from
- `--destination` or `-d`: The path to the directory where the files will be moved to and sorted at
- `--subfolder_only_sort` or `-sf`: When provided, does not sort files if they have no pre-made destination folder
All of the above optional arguments, if not provided, will pull their value from `config.ini`.
- `--use_current_dir` or `-u`: When provided, overrides `source` and `destination` with the current directory in the commandline. (Using `-s` and `-d` alongside this will render their values useless)
- `--config` or `-c`: Opens the config file and exits

## Configuration
By default, `yasfs` looks for a configuration file named `config.ini` located in the parent directory of the script. The settings in this file can be overrriden through the use of optional arguments in the command line. However,the config file also specifies custom sorting rules, allowing you to map specific file types to custom subfolders, which cannot be done from the command line.

The following is an example of how a `config.ini` file could look like:
```ini
[Settings]
source: /path/to/source
destination: /path/to/destination
sort_only_if_destination_subfolder_exists: False

[Overwrite Destinations]
Audio_Files: MP3, WAV, OGG, M4A, FLAC, AIFF, WMA, AAC
Image_Files: PNG, JPG, JPEG, HEIF, WEBP, TIF, TIFF, BMP, GIF, EPS
Text_Files: DOCX, PDF, PPT, PPTX, XLS, XLSX, XML, ODT, TXT, RTF, CSV, DOC, WPS, WPD, MSG. JSON, INI, LOG, YML, YAML, CONF
Video_Files: MP4, MPG, MOV, AVI, WMV, AVCHD, WEBM, FLV, F4V, SWF, MKV, WEBM, 3GP
Executable_Files: EXE, BAT, COM, CMD, INF, IPA, OSX, PIF, RUN, WSH, SH
Code_Files: C, CPP, JAVA, PY, JS, TS, CS, SWIFT, DTA, PL
Compressed_Files: RAR, ZIP, HQX, ARJ, TAR, ARC, SIT, GZ, Z
Webpage_Files: HTML, HTM, XHTML, ASP, CSS, ASPX, RSS,
3D_Files: OBJ, FBX, GLTF, USD, USDZ, CAD, BLEND, SBSAR, AMF, STL
```
In this example, we scan files from `/path/to/source`, move them to `/path/to/destination`, and sort them into custom subfolders if they match any of the file extension types defined under `[Overwrite Destinations]`.

## Examples
### Base Use case
To just run the program using the settings from `config.ini`
```bash
yasfs
```
### Using Arguments
Perhaps we want to keep `config.ini` untouched, and want to change the its settings just for this command... this is where arguments become handy.  
Here we override the source and destination file paths from `config.ini`:
```bash
yasfs -s /path/to/source -d /path/to/destination
```
Here we just override the destination file path from `config.ini`:
```bash
yasfs -d /path/to/destination
```
We can do the same for the source file path, of course:
```bash
yasfs -s /path/to/source
```
When we sort files, subfolders for their file extension type are automatically created, but what if we don't want to sort files unless their subfolders already exist?
```bash
yasfs -sf
```

## Contributing
1. Fork this repository (https://github.com/ashaider/yet-another-simple-file-sorter/fork)
2. Create your feature branch (git checkout -b feature/fooBar)
3. Commit your changes (git commit -am 'Add some fooBar')
4. Push to the branch (git push origin feature/fooBar)
5. Create a new Pull Request

## Meta
A. Haider – ahmedsyedh1+gh@gmail.com

https://github.com/ashaider/yet-another-simple-file-sorter/

Distributed under the MIT license. See LICENSE for more information.