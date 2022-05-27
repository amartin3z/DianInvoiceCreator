#!/bin/bash

find /tmp -type f -name '*.csv' -exec rm {} \;
find /tmp -type f -name '*.xlsx' -exec rm {} \;

