#!/bin/bash

ruff format
ruff check --select=I --fix
