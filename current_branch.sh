#!/usr/bin/env bash

current=$(git rev-parse --abbrev-ref HEAD)

echo $current
