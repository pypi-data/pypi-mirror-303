# Bibliograpy

Bibliography management to decorate source code.

[![example workflow](https://github.com/SamuelAndresPascal/cosmoloj-py/actions/workflows/bibliograpy.yml/badge.svg)](https://github.com/SamuelAndresPascal/cosmoloj-py/actions)

[![Anaconda-Server Badge](https://anaconda.org/cosmoloj/bibliograpy/badges/version.svg)](https://anaconda.org/cosmoloj/bibliograpy)
[![Anaconda-Server Badge](https://anaconda.org/cosmoloj/bibliograpy/badges/latest_release_date.svg)](https://anaconda.org/cosmoloj/bibliograpy)
[![Anaconda-Server Badge](https://anaconda.org/cosmoloj/bibliograpy/badges/latest_release_relative_date.svg)](https://anaconda.org/cosmoloj/bibliograpy)
[![Anaconda-Server Badge](https://anaconda.org/cosmoloj/bibliograpy/badges/platforms.svg)](https://anaconda.org/cosmoloj/bibliograpy)
[![Anaconda-Server Badge](https://anaconda.org/cosmoloj/bibliograpy/badges/license.svg)](https://anaconda.org/cosmoloj/bibliograpy)

[![PyPI repository Badge](https://badge.fury.io/py/bibliograpy.svg)](https://badge.fury.io/py/bibliograpy)


* [API](#api)
* [Preprocessing tool](#preprocessing-tool)
* [Documentation](#documentation)



## API

The Bibliograpy API allows to manage bibliographic centralized references using decorators.

Hence, is it possible to factorize all bibliographic sources as variables in a single module, using them as arguments of
decorators.

```py
"""The bibliography module."""

from bibliograpy.api import TechReport

IAU_2006_B1 = TechReport.generic(
    cite_key='iau_2006_b1',
    author='',
    institution='iau',
    title='Adoption of the P03 Precession Theory and Definition of the Ecliptic',
    year=2006)
```

```py
"""The bibliography_client module using the bibliography.py module."""

from bibliograpy.api import reference

from bibliography import IAU_2006_B1

@reference(IAU_2006_B1)
def my_function():
    """My my_function documentation."""
    # some implementation here using the reference given as a parameter to the decorator

```

The usage of the decorator has two purposes.

First, to use a bibliographic reference defined once and for all, centralized and reusable.

Second, to implicitly add to the documentation of the decorated entity a bibliographical section.

```
import bibliography_client

>>> help(my_function)
Help on function my_function in module bibliography_client

my_function()
    My my_function documentation.

    Bibliography: Adoption of the P03 Precession Theory and Definition of the Ecliptic [iau_2006_b1]
```

## Preprocessing tool

Bibliograpy allows generating a source code bibliograpy from a resource bibliography file.

Bibliograpy process supports bibliography files in yaml format. Each bibliographic entry contains three fields. 
The `type` field only supports the `misc` value. The `key` fields represents the bibliographic entry unique key (id).
The `title` field represents the readable form or the entry. For instance:

```yml
- entry_type: misc
  cite_key: nasa
  title: NASA
- entry_type: misc
  cite_key: iau
  title: International Astronomical Union
```

This bibliography file can be preprocessend by the `bibliograpy process` tool.

```
bibliograpy process
```

This preprocessing produces the corresponding bibliographic references that can be used as
bibliograpy decorator arguments.

```py
from bibliograpy.api import Misc

NASA = Misc.generic(cite_key='nasa',
                    title='NASA')

IAU = Misc.generic(cite_key='iau',
                   title='International Astronomical Union')
```

### Cross-referencing support

Example:

```json
[
    {
        "entry_type": "misc",
        "cite_key": "ogc",
        "title": "Open Geospatial Consortium",
        "institution": "OGC"
    },
    {
        "entry_type": "misc",
        "cite_key": "iogp",
        "title": "International Association of Oil & Gas Producers",
        "institution": "IOGP"
    },
    {
        "entry_type": "misc",
        "cite_key": "zeitschrift_fur_vermessungswesen",
        "title": "Zeitschrift für Vermessungswesen",
        "journal": "Zeitschrift für Vermessungswesen",
        "issn": "0044-3689"
    },
    {
        "entry_type": "techreport",
        "cite_key": "tga",
        "author": "",
        "institution": "",
        "year": 1989,
        "month": "september",
        "type": "document",
        "title": "TGA File Format",
        "url": "http://tfc.duke.free.fr/coding/tga_specs.pdf"
    },
    {
        "entry_type": "book",
        "cite_key": "real_time_collision_detection",
        "title": "Real-Time Collision Detection",
        "publisher": "",
        "editor": "Sony Computer Entertainment America, CRC Press",
        "year": 2004
    },
    {
        "entry_type": "book",
        "cite_key": "map_projections",
        "title": "Map Projections - A Working Manual",
        "editor": "UNITED STATES GOVERNMENT PRINTING OFFICE, WASHINGTON",
        "publisher": "",
        "url": "https://pubs.usgs.gov/pp/1395/report.pdf",
        "year": 1987
    },
    {
        "entry_type": "techreport",
        "cite_key": "sf_access_part_1_v1_2_1",
        "author": "",
        "type": "standard",
        "title": "OpenGIS Implementation Standard for Geographic information - Simple Feature Access - Part 1: Common architecture",
        "year": 2011,
        "number": "OGC 06-103r4",
        "version": "1.2.1",
        "crossref": "ogc",
        "url": "http://portal.opengeospatial.org/files/?artifact_id=25355"
    },
    {
        "entry_type": "techreport",
        "cite_key": "iogp_guidance_note_7_2_2019",
        "author": "",
        "type": "document",
        "title": "Geomatics Guidance Note 7, part 2 Coordinate Conversions & Transformations including Formulas",
        "crossref": "iogp",
        "year": 2019,
        "url": "https://www.iogp.org/wp-content/uploads/2019/09/373-07-02.pdf",
        "number": "373-7-2"
    },
    {
        "entry_type": "techreport",
        "cite_key": "cts_revision_v1_0",
        "author": "",
        "type": "standard",
        "title": "Coordinate Transformation Services",
        "year": 2001,
        "month": "January",
        "day": 12,
        "number": "OGC 01-009",
        "version": "1.00",
        "crossref": "ogc",
        "url": "https://portal.ogc.org/files/?artifact_id=999"
    },
    {
        "entry_type": "techreport",
        "cite_key": "wkt_crs_v1_0",
        "author": "",
        "type": "standard",
        "title": "Geographic information - Well known text representation of coordinate reference systems",
        "year": 2015,
        "month": "May",
        "day": 1,
        "number": "OGC 12-063r5",
        "version": "1.0",
        "crossref": "ogc",
        "url": "http://docs.opengeospatial.org/is/12-063r5/12-063r5.html"
    },
    {
        "entry_type": "techreport",
        "cite_key": "wkt_crs_v2_1",
        "author": "",
        "type": "standard",
        "title": "Geographic information - Well known text representation of coordinate reference systems",
        "year": 2023,
        "month": "August",
        "day": 16,
        "number": "OGC 18-010r11",
        "version": "2.1.11",
        "crossref": "ogc",
        "url": "https://docs.ogc.org/is/18-010r11/18-010r11.pdf"
    },
    {
        "entry_type": "article",
        "cite_key": "joachim_boljen_2003",
        "author": "",
        "title": "Bezugssystemumstellung DHDN90 ETRS89 in Schleswig-Holstein",
        "crossref": "zeitschrift_fur_vermessungswesen",
        "year": 2003,
        "volume": "128",
        "pages": "244-250",
        "url": "https://geodaesie.info/system/files/privat/zfv_2003_4_Boljen.pdf"
    },
    {
        "entry_type": "article",
        "cite_key": "joachim_boljen_2004",
        "author": "",
        "title": "Zur geometrischen Interpretation und direkten Bestimmung von Formfunktionen",
        "crossref": "zeitschrift_fur_vermessungswesen",
        "year": 2004,
        "volume": "129",
        "pages": "258-260",
        "url": "https://geodaesie.info/system/files/privat/zfv_2004_4_Boljen.pdf"
    }
]
```

```python
from bibliograpy.api import *


OGC = Misc.generic(cite_key='ogc',
                   institution='OGC',
                   title='Open Geospatial Consortium')

IOGP = Misc.generic(cite_key='iogp',
                    institution='IOGP',
                    title='International Association of Oil & Gas Producers')

ZEITSCHRIFT_FUR_VERMESSUNGSWESEN = Misc.generic(cite_key='zeitschrift_fur_vermessungswesen',
                                                journal='Zeitschrift für Vermessungswesen',
                                                title='Zeitschrift für Vermessungswesen',
                                                non_standard=NonStandard(issn='0044-3689'))

TGA = TechReport.generic(cite_key='tga',
                         author='',
                         institution='',
                         month='september',
                         title='TGA File Format',
                         type='document',
                         year=1989,
                         non_standard=NonStandard(url='http://tfc.duke.free.fr/coding/tga_specs.pdf'))

REAL_TIME_COLLISION_DETECTION = Book.generic(cite_key='real_time_collision_detection',
                                             editor='Sony Computer Entertainment America, CRC Press',
                                             publisher='',
                                             title='Real-Time Collision Detection',
                                             year=2004)

MAP_PROJECTIONS = Book.generic(cite_key='map_projections',
                               editor='UNITED STATES GOVERNMENT PRINTING OFFICE, WASHINGTON',
                               publisher='',
                               title='Map Projections - A Working Manual',
                               year=1987,
                               non_standard=NonStandard(url='https://pubs.usgs.gov/pp/1395/report.pdf'))

SF_ACCESS_PART_1_V1_2_1 = TechReport.generic(cite_key='sf_access_part_1_v1_2_1',
                                             author='',
                                             crossref=OGC,
                                             number='OGC 06-103r4',
                                             title='OpenGIS Implementation Standard for Geographic information - Simple Feature Access - Part 1: Common architecture',
                                             type='standard',
                                             year=2011,
                                             non_standard=NonStandard(url='http://portal.opengeospatial.org/files/?artifact_id=25355'))

IOGP_GUIDANCE_NOTE_7_2_2019 = TechReport.generic(cite_key='iogp_guidance_note_7_2_2019',
                                                 author='',
                                                 crossref=IOGP,
                                                 number='373-7-2',
                                                 title='Geomatics Guidance Note 7, part 2 Coordinate Conversions & Transformations including Formulas',
                                                 type='document',
                                                 year=2019,
                                                 non_standard=NonStandard(url='https://www.iogp.org/wp-content/uploads/2019/09/373-07-02.pdf'))

CTS_REVISION_V1_0 = TechReport.generic(cite_key='cts_revision_v1_0',
                                       author='',
                                       crossref=OGC,
                                       month='January',
                                       number='OGC 01-009',
                                       title='Coordinate Transformation Services',
                                       type='standard',
                                       year=2001,
                                       non_standard=NonStandard(url='https://portal.ogc.org/files/?artifact_id=999'))

WKT_CRS_V1_0 = TechReport.generic(cite_key='wkt_crs_v1_0',
                                  author='',
                                  crossref=OGC,
                                  month='May',
                                  number='OGC 12-063r5',
                                  title='Geographic information - Well known text representation of coordinate reference systems',
                                  type='standard',
                                  year=2015,
                                  non_standard=NonStandard(url='http://docs.opengeospatial.org/is/12-063r5/12-063r5.html'))

WKT_CRS_V2_1 = TechReport.generic(cite_key='wkt_crs_v2_1',
                                  author='',
                                  crossref=OGC,
                                  month='August',
                                  number='OGC 18-010r11',
                                  title='Geographic information - Well known text representation of coordinate reference systems',
                                  type='standard',
                                  year=2023,
                                  non_standard=NonStandard(url='https://docs.ogc.org/is/18-010r11/18-010r11.pdf'))

JOACHIM_BOLJEN_2003 = Article.generic(cite_key='joachim_boljen_2003',
                                      author='',
                                      crossref=ZEITSCHRIFT_FUR_VERMESSUNGSWESEN,
                                      pages='244-250',
                                      title='Bezugssystemumstellung DHDN90 ETRS89 in Schleswig-Holstein',
                                      volume='128',
                                      year=2003,
                                      non_standard=NonStandard(url='https://geodaesie.info/system/files/privat/zfv_2003_4_Boljen.pdf'))

JOACHIM_BOLJEN_2004 = Article.generic(cite_key='joachim_boljen_2004',
                                      author='',
                                      crossref=ZEITSCHRIFT_FUR_VERMESSUNGSWESEN,
                                      pages='258-260',
                                      title='Zur geometrischen Interpretation und direkten Bestimmung von Formfunktionen',
                                      volume='129',
                                      year=2004,
                                      non_standard=NonStandard(url='https://geodaesie.info/system/files/privat/zfv_2004_4_Boljen.pdf'))
```

## Documentation

[Latest release](https://cosmoloj.com/mkdocs/bibliograpy/latest/)

[Trunk](https://cosmoloj.com/mkdocs/bibliograpy/master/)