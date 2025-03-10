#!/bin/sh

tr -d '|' | tr -s ' ' | tr ' ' '+'| cut -c 2-| rev | cut -c 2- |rev | bc
