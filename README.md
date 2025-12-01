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
curl -F "options={\"languages\":[\"eng+ocrb\"],\"dpi\":100}" -F "file=@/path/to/file.png" http://localhost:8884/tesseract
```

In the options, you can select, `eng+ell+deu+ara+rus+spa+ocrb`, which are the current supported trained models.

# Notes

This server seems to be able to perform OCR only on image files.
