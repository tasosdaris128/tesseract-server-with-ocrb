# Credits

This project is based on https://github.com/hertzg/tesseract-server/

# Prerequisites

In order to run this application you need to install:

```
docker
docker-compose
make // If your system has not preinstalled
```

# Operate

In order to startup the server, just run:

```
make
```

In order to stop the server, just run:

```
make clean
```

# Request for OCR

In order to perform OCR on a file, run:

```
curl -F "options={\"languages\":[\"eng+ocrb\"],\"dpi\":100}" -F "file=@/path/to/file.png" http://localhost:5000/tesseract
```

In the options, you can select, `eng+ell+deu+ara+rus+spa+ocrb`, which are the current supported trained models.

The response will look something like this:

```
{
  "errorMessage": "Failed to load any lstm-specific dictionaries for lang ocrb!!\n",
  "results": [
    "me HELLAS =~",
    "- -t Tutog/ Type Xuwpa/Country A ABP N",
    "SA P EAAIGRC XXXXXXXXX",
    "PASSPORT 1. Emwvupo/Surname",
    "DOE",
    "DOE",
    "2. Ovopa/Name",
    "JOHN",
    "JOHN",
    "IBay\u00e9veia/Nationality: EAAHNIKH / HELLENIC",
    "PUA0S M",
    ". Hu. y\u00e9vvnong/Date 0 16 Apr 87",
    "T6T YN AAPIZA",
    "Place LARISA",
    "Hp. \u00e9kdoong/lss. date: XX Sep XX",
    "8. Hp. Afigng/Date of expiry: XX Sep XX",
    "9. ExO. Apxn/iss. AEAJAANPC 10 YH 178",
    "GRC",
    "P<GRCJOHN<<DOE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXX<<<<<<<<<<<<<<00"
  ]
}
```

# Notes

This server seems to be able to perform OCR only on image files.
