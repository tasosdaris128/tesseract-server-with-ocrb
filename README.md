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

# Notes

This server seems to be able to perform OCR only on image files.
