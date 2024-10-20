#!/bin/bash

update_software() {
    echo "Aktualizacja oprogramowania..."
    pip install price_updater --upgrade
}

start_program() {
    python -m price_updater
}

update_software
start_program