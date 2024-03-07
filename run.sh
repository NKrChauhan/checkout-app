#!/bin/bash

docker build -t checkout-app .
docker run -it checkout-app /bin/bash
