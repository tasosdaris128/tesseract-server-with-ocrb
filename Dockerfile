FROM hertzg/tesseract-server:latest
RUN apk add --no-cache tesseract-ocr-data-spa tesseract-ocr-data-ara tesseract-ocr-data-ell
ADD ocrb.traineddata /usr/share/tessdata/
ADD ell.traineddata /usr/share/tessdata/
ADD grc.traineddata /usr/share/tessdata/
ADD ara.traineddata /usr/share/tessdata/
ADD deu.traineddata /usr/share/tessdata/
ADD rus.traineddata /usr/share/tessdata/
ADD spa.traineddata /usr/share/tessdata/
ENV TESSDATA_PREFIX /usr/share/tessdata/
