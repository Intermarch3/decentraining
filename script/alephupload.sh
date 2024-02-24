#usr/bin/env bash

echo | aleph program upload ../uploads main:app > output.txt
mv ../uploads/* ../old/
