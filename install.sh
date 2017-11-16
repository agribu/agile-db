#!/bin/bash
PROJECT_DIR = $('pwd')

git clone https://github.com/Agile-IoT/agile-sdk.git $PROJECT_DIR/src/js/agile-sdk
cd $PROJECT_DIR/src/js/agile-sdk
npm install
cd $PROJECT_DIR/src/js/agile-sdk-proxy
npm install
cd $PROJECT_DIR/src/js/agile-sdk-handler
npm install
